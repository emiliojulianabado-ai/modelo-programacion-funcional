import streamlit as st

from services.gasolineria import (
    calcular_consumo_gasolina,
    calcular_consumo_gasolina_lambda,
    demostracion_funcional
)

st.set_page_config(
    page_title="Consumo de gasolina",
    page_icon="⛽",
    layout="centered"
)

# --------------------------------------------------
# ESTILO GENERAL
# --------------------------------------------------
st.markdown("""
<style>

/* Fondo igual al de la página principal */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #172033 100%
    );
}

/* Contenedor principal */
.block-container {
    max-width: 950px;
    padding-top: 2.5rem;
    padding-bottom: 3rem;
}

/* Título */
h1 {
    color: #f8fafc;
    font-size: 2.5rem !important;
}

/* Subtítulos */
h2, h3 {
    color: #f8fafc;
}

/* Texto secundario */
.descripcion {
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 25px;
}

/* Línea decorativa */
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

/* Caja de datos */
.caja {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 15px;
}

/* Resultados */
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
    font-size: 30px;
    font-weight: bold;
    margin: 0;
}

/* Inputs */
div[data-testid="stNumberInput"] input {
    background-color: #1e293b;
    border-radius: 8px;
}

/* Botón */
div.stButton > button {
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

div.stButton > button:hover {
    opacity: 0.9;
}

/* Expander */
[data-testid="stExpander"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    border-radius: 10px;
}

/* Separadores */
hr {
    border-color: #334155;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ENCABEZADO
# --------------------------------------------------

st.title("⛽ Consumo de gasolina")

st.markdown(
    """
    <div class="descripcion">
        Calcula cuántos litros de gasolina se necesitan
        para recorrer una distancia determinada.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# DATOS
# --------------------------------------------------

st.subheader("📌 Datos del viaje")

col1, col2 = st.columns(2)

with col1:
    distancia = st.number_input(
        "📏 Distancia del viaje (km)",
        min_value=0.0,
        value=300.0,
        step=10.0
    )

with col2:
    rendimiento = st.number_input(
        "🚗 Rendimiento del automóvil (km/L)",
        min_value=0.0,
        value=15.0,
        step=1.0
    )


# --------------------------------------------------
# BOTÓN
# --------------------------------------------------

if st.button(
    "Calcular consumo",
    use_container_width=True
):

    if rendimiento <= 0:

        st.error(
            "❌ El rendimiento debe ser mayor que cero."
        )

    else:

        consumo_normal = calcular_consumo_gasolina(
            distancia,
            rendimiento
        )

        consumo_lambda = calcular_consumo_gasolina_lambda(
            distancia,
            rendimiento
        )

        st.divider()


        # --------------------------------------------------
        # RESULTADOS
        # --------------------------------------------------

        st.subheader("📊 Resultados")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="resultado">
                    <h3>Versión normal</h3>
                    <p>{consumo_normal:.2f} L</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="resultado">
                    <h3>Versión lambda</h3>
                    <p>{consumo_lambda:.2f} L</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()


        # --------------------------------------------------
        # PROCEDIMIENTO
        # --------------------------------------------------

        st.subheader("📐 Procedimiento")

        st.latex(
            r"\text{Consumo} = "
            r"\frac{\text{Distancia}}{\text{Rendimiento}}"
        )

        st.code(
            f"""
Distancia = {distancia:.2f} km
Rendimiento = {rendimiento:.2f} km/L

Consumo = {distancia:.2f} / {rendimiento:.2f}

Resultado = {consumo_normal:.2f} litros
"""
        )


        # --------------------------------------------------
        # LAMBDA
        # --------------------------------------------------

        with st.expander("🟢 Ver procedimiento con lambda"):

            st.code(
                """calcular_consumo_gasolina_lambda = (
    lambda distancia, rendimiento:
    distancia / rendimiento
    if rendimiento > 0 else 0
)""",
                language="python"
            )

            st.write(
                f"Resultado: **{consumo_lambda:.2f} litros**"
            )


        # --------------------------------------------------
        # CASO BASE
        # --------------------------------------------------

        with st.expander("🟡 Ver caso base"):

            st.write(
                "El rendimiento debe ser mayor que cero "
                "para evitar una división entre cero."
            )

            st.code(
                "Si rendimiento <= 0 → no se realiza el cálculo."
            )


        # --------------------------------------------------
        # COMPARACIÓN
        # --------------------------------------------------

        if consumo_normal == consumo_lambda:
            st.success(
                "✅ Ambas versiones producen el mismo resultado."
            )

# --------------------------------------------------
# EVIDENCIA DE PROGRAMACIÓN FUNCIONAL (RÚBRICA)
# --------------------------------------------------
st.divider()
st.subheader("🧩 Programación funcional aplicada")
st.caption("Esta sección evidencia lambda, map, filter, reduce, evaluación perezosa y valores inmutables cargados desde JSON.")

try:
    datos_pf, map_pf, filter_pf, reduce_pf, tipo_map_pf, tipo_filter_pf = demostracion_funcional(rendimiento)
    st.write("**Datos originales:**", datos_pf)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🔵 MAP — Transformación**")
        st.write("Consumos (L):", map_pf)
    with c2:
        st.markdown("**🟠 FILTER — Selección**")
        st.write("Consumos filtrados:", filter_pf)
    st.markdown("**🟣 REDUCE — Acumulación**")
    st.write("Consumo total (L):", reduce_pf)
    with st.expander("⚡ Ver Lazy Evaluation y JSON"):
        st.write("`map()` y `filter()` crean iteradores; los datos se producen al consumirlos.")
        st.code(f"Tipo antes de consumir map: {tipo_map_pf}\nTipo antes de consumir filter: {tipo_filter_pf}")
        st.write("Los valores de prueba y umbrales se cargan desde `data/constantes.json` mediante la clase `Configuracion`.")
    with st.expander("λ ¿Dónde se usa lambda?"):
        st.write("Las funciones anónimas `lambda` se utilizan dentro de `map`, `filter` y `reduce`, además de la versión lambda del cálculo principal.")
except Exception as e:
    st.warning(f"No fue posible generar la demostración funcional: {e}")
