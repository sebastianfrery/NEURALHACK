
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="NeuralHack Traffic Analytics", layout="wide")

st.title("🛸 Sistema Inteligente de Tráfico - NEURALHACK")
st.markdown("""
Esta interfaz permite visualizar las métricas de movilidad automatizadas y verificar la integridad de los datos en Blockchain.
""")

# Carga de datos
@st.cache_data
def load_data():
    # Carga el CSV que generó tu pipeline
    return pd.read_csv("output/estudio_final_neuralhack_v2.csv")

try:
    df = load_data()

    # --- FILTROS ---
    st.sidebar.header("Filtros de Análisis")
    dataset_sel = st.sidebar.multiselect("Dataset", df['dataset'].unique(), default=df['dataset'].unique())
    df_filtered = df[df['dataset'].isin(dataset_sel)]

    # --- MÉTRICAS GENERALES ---
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Secuencias", len(df_filtered))
    col2.metric("Promedio Intensidad", f"{df_filtered['ia_intensidad'].mean():.2f}")
    col3.metric("Ocupación Media", f"{df_filtered['ia_ocupacion_%'].mean():.2f}%")
    col4.metric("Alertas Críticas", len(df_filtered[df_filtered['riesgo_vial'] == 'CRÍTICO']))

    # --- VISUALIZACIÓN ---
    tab1, tab2, tab3 = st.tabs(["📊 Gráficos de Tráfico", "🗺️ Mapa de Intensidad", "🔗 Verificación Blockchain"])

    with tab1:
        st.subheader("Distribución de Tipología de Vehículos")
        fig = px.bar(df_filtered, x='id_secuencia', y=['avg_turismos', 'avg_motos', 'avg_pesados'], 
                     title="Conteo por Categoría", barmode='group')
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Geolocalización de Escenas")
        # Filtrar coordenadas válidas
        df_map = df_filtered[df_filtered['latitud'] != 0]
        if not df_map.empty:
            st.map(df_map, latitude='latitud', longitude='longitud', size='ia_intensidad')
        else:
            st.info("No hay coordenadas GPS disponibles para mapear.")

    with tab3:
        st.subheader("Registro Inmutable de Resultados (Blockchain)")
        st.write("Cada fila representa un análisis certificado con tecnología BSV Association.")
        st.dataframe(df_filtered[['id_secuencia', 'timestamp', 'ia_intensidad', 'riesgo_vial', 'blockchain_hash']], 
                     use_container_width=True)

except FileNotFoundError:
    st.error("⚠️ No se encontró el archivo 'estudio_final_neuralhack_v2.csv'. Ejecuta primero el pipeline 'main.py'.")

# Para correr la aplicacion : streamlit run app.py
