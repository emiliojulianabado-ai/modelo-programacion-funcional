import streamlit as st

from services.jubilacion import (
    calcular_dinero_jubilacion,
    calcular_dinero_jubilacion_lambda,
    demostracion_funcional
)


st.set_page_config(
    page_title="Dinero para jubilarme",
    page_icon="💼",
    layout="centered"
)


# --------------------------------------------------
# ESTILOS
# --------------------------------------------------

st.markdown("""
<style>

/* Fondo general */
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

/* Descripción */
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

/* Tarjetas de resultados */
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
    font-size: 27px;
    font-weight: bold;
    margin: 0;
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

/* Expanders */
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

st.title("💼 Dinero para jubilarme")

st.markdown(
    """
    <div class="descripcion">
        Calcula una estimación del dinero necesario
        para mantener una pensión mensual durante tus años de retiro.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# DATOS DE ENTRADA
# --------------------------------------------------

st.subheader("Datos de retiro")

col1, col2 = st.columns(2)

with col1:
    pension_mensual = st.number_input(
        "Pensión mensual deseada ($)",
        min_value=0.0,
        value=20000.0,
        step=1000.0
    )

with col2:
    anios_retiro = st.number_input(
        "Años de retiro",
        min_value=1,
        max_value=60,
        value=20,
        step=1
    )


# --------------------------------------------------
# BOTÓN
# --------------------------------------------------

if st.button(
    "Calcular dinero necesario",
    use_container_width=True
):

    if pension_mensual <= 0:

        st.error(
            "La pensión mensual debe ser mayor que cero."
        )

    elif anios_retiro <= 0:

        st.error(
            "Los años de retiro deben ser mayores que cero."
        )

    else:

        # --------------------------------------------------
        # CÁLCULOS
        # --------------------------------------------------

        dinero_normal = calcular_dinero_jubilacion(
            pension_mensual,
            anios_retiro
        )

        dinero_lambda = calcular_dinero_jubilacion_lambda(
            pension_mensual,
            anios_retiro
        )

        st.divider()


        # --------------------------------------------------
        # RESULTADOS
        # --------------------------------------------------

        st.subheader("Resultados")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"""
                <div class="resultado">
                    <h3>Función normal</h3>
                    <p>${dinero_normal:,.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="resultado">
                    <h3>Función lambda</h3>
                    <p>${dinero_lambda:,.2f}</p>
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
            "El cálculo multiplica la pensión mensual por "
            "los 12 meses del año y por los años de retiro."
        )

        st.latex(
            r"\text{Dinero necesario} = "
            r"\text{Pensión mensual} \times 12 \times "
            r"\text{Años de retiro}"
        )

        st.code(
            f"""
Pensión mensual = ${pension_mensual:,.2f}
Años de retiro = {anios_retiro}
Meses por año = 12

Dinero necesario =
${pension_mensual:,.2f} × 12 × {anios_retiro}

Resultado = ${dinero_normal:,.2f}
"""
        )


        # --------------------------------------------------
        # PROCEDIMIENTO LAMBDA
        # --------------------------------------------------

        with st.expander("λ Ver procedimiento con lambda"):

            st.write(
                "La función lambda recibe la pensión mensual "
                "y los años de retiro, y realiza el cálculo directamente."
            )

            st.code(
                """calcular_dinero_jubilacion_lambda = (
    lambda pension_mensual, anios_retiro:
    pension_mensual * 12 * anios_retiro
    if pension_mensual > 0 and anios_retiro > 0
    else 0
)""",
                language="python"
            )

            st.write("Aplicando la función lambda:")

            st.code(
                f"""
${pension_mensual:,.2f} × 12 × {anios_retiro}

= ${dinero_lambda:,.2f}
"""
            )


        # --------------------------------------------------
        # CASO BASE
        # --------------------------------------------------

        with st.expander("! Ver caso base"):

            st.write(
                "La pensión mensual y los años de retiro "
                "deben ser mayores que cero."
            )

            st.code(
                "Si pensión <= 0 o años <= 0 → no se realiza el cálculo."
            )


        # --------------------------------------------------
        # COMPARACIÓN
        # --------------------------------------------------

        if dinero_normal == dinero_lambda:

            st.success(
                "✓ Ambas versiones producen el mismo resultado."
            )


        # --------------------------------------------------
        # AVISO
        # --------------------------------------------------

        st.warning(
            "Esta es una estimación simplificada con fines académicos. "
            "No considera inflación, rendimientos, impuestos, AFORE, "
            "IMSS/ISSSTE ni otros factores financieros."
        )

# --------------------------------------------------
# EVIDENCIA DE PROGRAMACIÓN FUNCIONAL (RÚBRICA)
# --------------------------------------------------
st.divider()
st.subheader("🧩 Programación funcional aplicada")
st.caption("Esta sección evidencia lambda, map, filter, reduce, evaluación perezosa y valores inmutables cargados desde JSON.")

try:
    datos_pf, map_pf, filter_pf, reduce_pf, tipo_map_pf, tipo_filter_pf = demostracion_funcional(pension_mensual)
    st.write("**Datos originales:**", datos_pf)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🔵 MAP — Transformación**")
        st.write("Montos acumulados:", map_pf)
    with c2:
        st.markdown("**🟠 FILTER — Selección**")
        st.write("Montos filtrados:", filter_pf)
    st.markdown("**🟣 REDUCE — Acumulación**")
    st.write("Suma de escenarios:", reduce_pf)
    with st.expander("⚡ Ver Lazy Evaluation y JSON"):
        st.write("`map()` y `filter()` crean iteradores; los datos se producen al consumirlos.")
        st.code(f"Tipo antes de consumir map: {tipo_map_pf}\nTipo antes de consumir filter: {tipo_filter_pf}")
        st.write("Los valores de prueba y umbrales se cargan desde `data/constantes.json` mediante la clase `Configuracion`.")
    with st.expander("λ ¿Dónde se usa lambda?"):
        st.write("Las funciones anónimas `lambda` se utilizan dentro de `map`, `filter` y `reduce`, además de la versión lambda del cálculo principal.")
except Exception as e:
    st.warning(f"No fue posible generar la demostración funcional: {e}")
