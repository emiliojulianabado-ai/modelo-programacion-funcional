import streamlit as st
from datetime import date

from services.dias import (
    calcular_dias_vividos,
    calcular_dias_vividos_lambda,
    demostracion_funcional
)

st.set_page_config(
    page_title="Días vividos",
    page_icon="📅",
    layout="centered"
)

# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #172033 100%
    );
}

.block-container {
    max-width: 950px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

h1 {
    color: #f8fafc;
    font-size: 2.5rem !important;
}

h2, h3 {
    color: #f8fafc;
}

.descripcion {
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 25px;
}

.linea {
    height: 4px;
    width: 65px;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #6366f1
    );
    border-radius: 10px;
    margin-bottom: 30px;
}

.resultado {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

.resultado h3 {
    color: #cbd5e1;
    font-size: 17px;
    margin-bottom: 8px;
}

.resultado p {
    color: #38bdf8;
    font-size: 28px;
    font-weight: bold;
    margin: 0;
}

div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(
        90deg,
        #38bdf8,
        #6366f1
    );
    color: white;
    border: none;
    border-radius: 8px;
    height: 45px;
    font-weight: 600;
}

div[data-testid="stFormSubmitButton"] > button:hover {
    opacity: 0.9;
}

[data-testid="stExpander"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
}

hr {
    border-color: #334155;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.title("📅 Días vividos")

st.markdown(
    """
    <div class="descripcion">
        Calcula cuántos días has vivido utilizando
        una función normal y una función lambda.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# FORMULARIO
# --------------------------------------------------

st.subheader("🗓️ Fecha de nacimiento")

with st.form("formulario_calculo"):

    fecha_nacimiento = st.date_input(
        "Selecciona tu fecha de nacimiento",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today(),
        format="DD/MM/YYYY"
    )

    enviar = st.form_submit_button(
        "Calcular días vividos",
        use_container_width=True
    )

# --------------------------------------------------
# RESULTADOS
# --------------------------------------------------

if enviar:

    dias_normal = calcular_dias_vividos(
        fecha_nacimiento
    )

    dias_lambda = calcular_dias_vividos_lambda(
        fecha_nacimiento
    )

    fecha_actual = date.today()

    st.divider()

    st.subheader("▣ Resultados")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            f"""
            <div class="resultado">
                <h3>Función normal</h3>
                <p>{dias_normal:,} días</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="resultado">
                <h3>Función lambda</h3>
                <p>{dias_lambda:,} días</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # --------------------------------------------------
    # PROCEDIMIENTO
    # --------------------------------------------------

    st.subheader("ƒ Procedimiento")

    st.write(
        "El cálculo se realiza restando la fecha de nacimiento "
        "a la fecha actual."
    )

    st.code(
        f"""
Fecha actual = {fecha_actual.strftime('%d/%m/%Y')}

Fecha de nacimiento = {fecha_nacimiento.strftime('%d/%m/%Y')}

Días vividos = Fecha actual - Fecha de nacimiento

Resultado = {dias_normal:,} días
"""
    )

    # --------------------------------------------------
    # LAMBDA
    # --------------------------------------------------

    with st.expander("λ Ver procedimiento con lambda"):

        st.write(
            "La función lambda recibe la fecha de nacimiento "
            "y calcula directamente la diferencia con la fecha actual."
        )

        st.code(
            """calcular_dias_vividos_lambda = (
    lambda fecha_nacimiento:
    (date.today() - fecha_nacimiento).days
)""",
            language="python"
        )

        st.write("Aplicando lambda:")

        st.code(
            f"""
({fecha_actual.strftime('%d/%m/%Y')} -
 {fecha_nacimiento.strftime('%d/%m/%Y')}).days

= {dias_lambda:,} días
"""
        )

    # --------------------------------------------------
    # CASO BASE
    # --------------------------------------------------

    with st.expander("! Ver caso base"):

        st.write(
            "La fecha de nacimiento debe encontrarse dentro "
            "del rango permitido."
        )

        st.code(
            "Fecha mínima permitida = 01/01/1900\n"
            "Fecha máxima permitida = Fecha actual"
        )

    # --------------------------------------------------
    # COMPARACIÓN
    # --------------------------------------------------

    if dias_normal == dias_lambda:
        st.success(
            "✓ Ambas versiones producen el mismo resultado."
        )

# --------------------------------------------------
# EVIDENCIA DE PROGRAMACIÓN FUNCIONAL (RÚBRICA)
# --------------------------------------------------
st.divider()
st.subheader("🧩 Programación funcional aplicada")
st.caption("Esta sección evidencia lambda, map, filter, reduce, evaluación perezosa y valores inmutables cargados desde JSON.")

try:
    datos_pf, map_pf, filter_pf, reduce_pf, tipo_map_pf, tipo_filter_pf = demostracion_funcional()
    st.write("**Datos originales:**", datos_pf)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🔵 MAP — Transformación**")
        st.write("Días vividos:", map_pf)
    with c2:
        st.markdown("**🟠 FILTER — Selección**")
        st.write("Días filtrados:", filter_pf)
    st.markdown("**🟣 REDUCE — Acumulación**")
    st.write("Total de días:", reduce_pf)
    with st.expander("⚡ Ver Lazy Evaluation y JSON"):
        st.write("`map()` y `filter()` crean iteradores; los datos se producen al consumirlos.")
        st.code(f"Tipo antes de consumir map: {tipo_map_pf}\nTipo antes de consumir filter: {tipo_filter_pf}")
        st.write("Los valores de prueba y umbrales se cargan desde `data/constantes.json` mediante la clase `Configuracion`.")
    with st.expander("λ ¿Dónde se usa lambda?"):
        st.write("Las funciones anónimas `lambda` se utilizan dentro de `map`, `filter` y `reduce`, además de la versión lambda del cálculo principal.")
except Exception as e:
    st.warning(f"No fue posible generar la demostración funcional: {e}")
