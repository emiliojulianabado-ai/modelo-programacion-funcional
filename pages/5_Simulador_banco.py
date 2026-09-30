import streamlit as st

from services.servicio_banco import (
    depositar,
    retirar,
    depositar_lambda,
    retirar_lambda,
    demostracion_funcional
)


st.set_page_config(
    page_title="Simulador de banco",
    page_icon="🏦",
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

/* Tarjetas de resultado */
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

st.title("🏦 Simulador de banco")

st.markdown(
    """
    <div class="descripcion">
        Simula depósitos y retiros utilizando
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
# DATOS DE ENTRADA
# --------------------------------------------------

st.subheader("Datos de la operación")

col1, col2 = st.columns(2)

with col1:
    saldo = st.number_input(
        "Saldo inicial ($)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

with col2:
    cantidad = st.number_input(
        "Cantidad ($)",
        min_value=0.0,
        value=100.0,
        step=50.0
    )

operacion = st.selectbox(
    "Selecciona una operación",
    [
        "Depositar",
        "Retirar"
    ]
)


# --------------------------------------------------
# BOTÓN
# --------------------------------------------------

if st.button(
    "Ejecutar operación",
    use_container_width=True
):

    # --------------------------------------------------
    # VALIDACIONES
    # --------------------------------------------------

    if cantidad <= 0:

        st.warning(
            "La cantidad debe ser mayor que cero."
        )

    elif operacion == "Retirar" and cantidad > saldo:

        st.error(
            "No se puede retirar una cantidad mayor "
            "al saldo disponible."
        )

    else:

        # --------------------------------------------------
        # CÁLCULO
        # --------------------------------------------------

        if operacion == "Depositar":

            resultado_normal = depositar(
                saldo,
                cantidad
            )

            resultado_lambda = depositar_lambda(
                saldo,
                cantidad
            )

        else:

            resultado_normal = retirar(
                saldo,
                cantidad
            )

            resultado_lambda = retirar_lambda(
                saldo,
                cantidad
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
                    <p>${resultado_normal:,.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"""
                <div class="resultado">
                    <h3>Función lambda</h3>
                    <p>${resultado_lambda:,.2f}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.divider()


        # --------------------------------------------------
        # PROCEDIMIENTO
        # --------------------------------------------------

        st.subheader("ƒ Procedimiento")

        st.code(
            f"""
Saldo inicial = ${saldo:,.2f}
Operación = {operacion}
Cantidad = ${cantidad:,.2f}
"""
        )

        if operacion == "Depositar":

            st.write(
                "En un depósito, la cantidad se suma "
                "al saldo disponible."
            )

            st.latex(
                r"\text{Saldo final} = "
                r"\text{Saldo inicial} + \text{Cantidad}"
            )

            st.code(
                f"""
Saldo final = ${saldo:,.2f} + ${cantidad:,.2f}

Saldo final = ${resultado_normal:,.2f}
"""
            )

        else:

            st.write(
                "En un retiro, la cantidad se resta "
                "del saldo disponible."
            )

            st.latex(
                r"\text{Saldo final} = "
                r"\text{Saldo inicial} - \text{Cantidad}"
            )

            st.code(
                f"""
Saldo final = ${saldo:,.2f} - ${cantidad:,.2f}

Saldo final = ${resultado_normal:,.2f}
"""
            )


        # --------------------------------------------------
        # PROCEDIMIENTO LAMBDA
        # --------------------------------------------------

        with st.expander("λ Ver procedimiento con lambda"):

            if operacion == "Depositar":

                st.write(
                    "La función lambda suma la cantidad al saldo "
                    "si la cantidad es mayor que cero."
                )

                st.code(
                    """depositar_lambda = lambda saldo, cantidad: (
    saldo + cantidad
    if cantidad > 0
    else saldo
)""",
                    language="python"
                )

            else:

                st.write(
                    "La función lambda resta la cantidad solo si "
                    "es válida y no supera el saldo disponible."
                )

                st.code(
                    """retirar_lambda = lambda saldo, cantidad: (
    saldo - cantidad
    if cantidad > 0 and cantidad <= saldo
    else saldo
)""",
                    language="python"
                )

            st.write("Aplicando la función lambda:")

            if operacion == "Depositar":

                st.code(
                    f"""
${saldo:,.2f} + ${cantidad:,.2f}

= ${resultado_lambda:,.2f}
"""
                )

            else:

                st.code(
                    f"""
${saldo:,.2f} - ${cantidad:,.2f}

= ${resultado_lambda:,.2f}
"""
                )


        # --------------------------------------------------
        # CASO BASE
        # --------------------------------------------------

        with st.expander("! Ver condiciones de validación"):

            st.write(
                "Para realizar una operación bancaria válida:"
            )

            st.code(
                """Cantidad > 0

Para retirar:
Cantidad <= Saldo disponible"""
            )


        # --------------------------------------------------
        # COMPARACIÓN
        # --------------------------------------------------

        if resultado_normal == resultado_lambda:

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
    datos_pf, map_pf, filter_pf, reduce_pf, tipo_map_pf, tipo_filter_pf = demostracion_funcional(saldo)
    st.write("**Datos originales:**", datos_pf)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🔵 MAP — Transformación**")
        st.write("Saldo tras cada movimiento:", map_pf)
    with c2:
        st.markdown("**🟠 FILTER — Selección**")
        st.write("Depósitos filtrados:", filter_pf)
    st.markdown("**🟣 REDUCE — Acumulación**")
    st.write("Movimiento neto:", reduce_pf)
    with st.expander("⚡ Ver Lazy Evaluation y JSON"):
        st.write("`map()` y `filter()` crean iteradores; los datos se producen al consumirlos.")
        st.code(f"Tipo antes de consumir map: {tipo_map_pf}\nTipo antes de consumir filter: {tipo_filter_pf}")
        st.write("Los valores de prueba y umbrales se cargan desde `data/constantes.json` mediante la clase `Configuracion`.")
    with st.expander("λ ¿Dónde se usa lambda?"):
        st.write("Las funciones anónimas `lambda` se utilizan dentro de `map`, `filter` y `reduce`, además de la versión lambda del cálculo principal.")
except Exception as e:
    st.warning(f"No fue posible generar la demostración funcional: {e}")
