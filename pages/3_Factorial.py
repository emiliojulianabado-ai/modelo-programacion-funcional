import streamlit as st

from services.factorial import factorial, factorial_lambda, demostracion_funcional


st.set_page_config(
    page_title="Factorial",
    page_icon="∏",
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

st.title("∏ Factorial")

st.markdown(
    """
    <div class="descripcion">
        Calcula el factorial de un número utilizando
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
# ENTRADA
# --------------------------------------------------

st.subheader("Entrada")

numero = st.number_input(
    "Ingresa un número entero no negativo",
    min_value=0,
    max_value=100,
    value=5,
    step=1
)


# --------------------------------------------------
# BOTÓN
# --------------------------------------------------

if st.button(
    "Calcular factorial",
    use_container_width=True
):

    resultado_normal = factorial(numero)
    resultado_lambda = factorial_lambda(numero)

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
                <p>{numero}! = {resultado_normal:,}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="resultado">
                <h3>Función lambda</h3>
                <p>{numero}! = {resultado_lambda:,}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()


    # --------------------------------------------------
    # PROCEDIMIENTO
    # --------------------------------------------------

    st.subheader("ƒ Procedimiento")

    if numero == 0:

        st.code(
            "0! = 1\n\n"
            "Caso base → 0! = 1"
        )

    else:

        procedimiento = f"{numero}! = "

        for i in range(numero, 0, -1):
            procedimiento += f"{i} × "

        procedimiento = procedimiento[:-3]

        procedimiento += f"\n\nResultado = {resultado_normal:,}"

        st.code(procedimiento)


    # --------------------------------------------------
    # CASO BASE
    # --------------------------------------------------

    with st.expander("! Ver caso base"):

        st.write(
            "Cuando el número es 0, el factorial tiene "
            "como resultado 1."
        )

        st.code("0! = 1")


    # --------------------------------------------------
    # PROCEDIMIENTO LAMBDA
    # --------------------------------------------------

    with st.expander("λ Ver procedimiento con lambda"):

        st.write(
            "La función lambda utiliza una condición para "
            "manejar el caso base y `reduce` para realizar "
            "las multiplicaciones."
        )

        st.code(
            """factorial_lambda = lambda n: (
    1 if n == 0
    else reduce(
        lambda x, y: x * y,
        range(1, n + 1),
        1
    )
)""",
            language="python"
        )

        if numero > 0:

            st.write(
                f"Para **{numero}**, la función lambda realiza:"
            )

            elementos = " × ".join(
                str(i) for i in range(1, numero + 1)
            )

            st.code(
                f"{elementos}\n\n"
                f"Resultado = {resultado_lambda:,}"
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
    datos_pf, map_pf, filter_pf, reduce_pf, tipo_map_pf, tipo_filter_pf = demostracion_funcional(numero)
    st.write("**Datos originales:**", datos_pf)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🔵 MAP — Transformación**")
        st.write("Cuadrados con map:", map_pf)
    with c2:
        st.markdown("**🟠 FILTER — Selección**")
        st.write("Números filtrados:", filter_pf)
    st.markdown("**🟣 REDUCE — Acumulación**")
    st.write("Factorial con reduce:", reduce_pf)
    with st.expander("⚡ Ver Lazy Evaluation y JSON"):
        st.write("`map()` y `filter()` crean iteradores; los datos se producen al consumirlos.")
        st.code(f"Tipo antes de consumir map: {tipo_map_pf}\nTipo antes de consumir filter: {tipo_filter_pf}")
        st.write("Los valores de prueba y umbrales se cargan desde `data/constantes.json` mediante la clase `Configuracion`.")
    with st.expander("λ ¿Dónde se usa lambda?"):
        st.write("Las funciones anónimas `lambda` se utilizan dentro de `map`, `filter` y `reduce`, además de la versión lambda del cálculo principal.")
except Exception as e:
    st.warning(f"No fue posible generar la demostración funcional: {e}")
