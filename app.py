import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------------
st.set_page_config(
    page_title="Programación Funcional",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# ESTILOS CSS
# ---------------------------------------------------------
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

/* Ocultar elementos de Streamlit */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263244;
}

/* Texto del sidebar */
[data-testid="stSidebar"] * {
    color: #f8fafc;
}

/* Contenedor principal */
.block-container {
    padding-top: 3rem;
    max-width: 1200px;
}

/* Título principal */
.titulo-principal {
    font-size: 48px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 5px;
}

/* Subtítulo */
.subtitulo {
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 35px;
}

/* Tarjeta */
.tarjeta {
    background: rgba(30, 41, 59, 0.85);
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #334155;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.25);
}

/* Tarjeta pequeña */
.mini-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 14px;
    border: 1px solid #334155;
    min-height: 145px;
    transition: 0.3s;
}

.mini-card:hover {
    transform: translateY(-5px);
    border-color: #38bdf8;
}

/* Iconos */
.icono {
    font-size: 32px;
}

/* Texto de las tarjetas */
.mini-card h3 {
    color: #f8fafc;
    margin-top: 10px;
}

.mini-card p {
    color: #94a3b8;
    font-size: 14px;
}

/* Línea decorativa */
.linea {
    height: 4px;
    width: 70px;
    background: linear-gradient(
        90deg,
        #38bdf8,
        #6366f1
    );
    border-radius: 10px;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# ENCABEZADO
# ---------------------------------------------------------
st.markdown(
    '<div class="titulo-principal">λ Programación Funcional</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Aplicaciones prácticas desarrolladas mediante funciones, '
    'expresiones lambda y programación funcional.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# TARJETA DE BIENVENIDA
# ---------------------------------------------------------
st.markdown("""
<div class="tarjeta">

<h2 style="color:white;">
👋 Bienvenido
</h2>

<p style="
color:#cbd5e1;
font-size:17px;
line-height:1.7;
">
Selecciona una aplicación desde el menú lateral para comenzar.
Cada módulo demuestra diferentes conceptos de programación
funcional mediante ejercicios prácticos.
</p>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ---------------------------------------------------------
# TARJETAS DE APLICACIONES
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="mini-card">
        <div class="icono">⛽</div>
        <h3>Consumo de gasolina</h3>
        <p>
        Calcula rendimiento, consumo y costos de combustible.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="mini-card">
        <div class="icono">📅</div>
        <h3>Días vividos</h3>
        <p>
        Calcula los días transcurridos desde una fecha determinada.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="mini-card">
        <div class="icono">🧮</div>
        <h3>Factorial</h3>
        <p>
        Obtén el factorial de un número mediante funciones.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="mini-card">
        <div class="icono">🎓</div>
        <h3>Jubilación</h3>
        <p>
        Realiza cálculos relacionados con edad y retiro laboral.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="mini-card">
        <div class="icono">🏦</div>
        <h3>Simulador bancario</h3>
        <p>
        Simula operaciones y cálculos financieros.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="mini-card">
        <div class="icono">🚗</div>
        <h3>Tiempo de viaje</h3>
        <p>
        Calcula tiempos de traslado utilizando distancia y velocidad.
        </p>
    </div>
    """, unsafe_allow_html=True)