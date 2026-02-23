import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Arctic Voices Digital", page_icon="🌍", layout="wide")

# -------------------------
# GLASSMORPHISM CSS
# -------------------------
st.markdown("""
<style>

/* Ana arka plan */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Sidebar arka plan */
[data-testid="stSidebar"] {
    background: #0f2027;
}

/* Sidebar yazılar */
[data-testid="stSidebar"] * {
    color: white !important;
}

/* Radio buton yazıları */
div[role="radiogroup"] label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🌍 Arctic Voices Digital")
st.markdown("### Arktik Yerli Kültürleri | Kültür • Coğrafya • İklim")

menu = st.sidebar.radio("Menü", ["Ana Sayfa", "Kültürel Harita", "NASA İklim Verisi"])

# -------------------------
# ANA SAYFA - KART TASARIMI
# -------------------------
if menu == "Ana Sayfa":

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Inuit")
    st.image("inuit.jpg", use_container_width=True)
    st.write("Kanada, Alaska ve Grönland bölgesinde yaşayan Arktik yerli halkıdır.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Sami")
    st.image("sami.jpg", use_container_width=True)
    st.write("İskandinavya'nın kuzeyinde yaşayan yerli topluluktur.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Nenets")
    st.image("nenets.jpg", use_container_width=True)
    st.write("Rusya tundra bölgesinde göçebe ren geyiği çobanlarıdır.")
    st.markdown('</div>', unsafe_allow_html=True)
# -------------------------
# HARİTA
# -------------------------

if menu == "Kültürel Harita":

    st.title("🗺️ Arktik Yerli Kültür Haritası")

    # Harita merkezi (Arktik bölge)
    m = folium.Map(
        location=[70, 0],
        zoom_start=3,
        tiles="CartoDB dark_matter"
    )

    # Inuit
    folium.Marker(
        location=[64.2, -51.7],  # Grönland
        popup="""
        <b>Inuit</b><br>
        Kanada, Alaska ve Grönland'da yaşayan Arktik halk.
        """,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    # Sami
    folium.Marker(
        location=[68.5, 23.6],  # Norveç-Finlandiya bölgesi
        popup="""
        <b>Sami</b><br>
        İskandinavya'nın kuzeyinde yaşayan yerli topluluk.
        """,
        icon=folium.Icon(color="green", icon="info-sign")
    ).add_to(m)

    # Nenets
    folium.Marker(
        location=[67.5, 53.0],  # Rusya tundra
        popup="""
        <b>Nenets</b><br>
        Sibirya tundrasında göçebe ren geyiği çobanları.
        """,
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

    # Haritayı göster
    st_folium(m, width=900, height=600)

# -------------------------
# NASA GERÇEK VERİ
# -------------------------
    st.subheader("🧊 NOAA Arctic Sea Ice Extent")

    try:
        noaa_url = "https://noaadata.apps.nsidc.org/NOAA/G02135/north/monthly/data/N_09_extent_v3.0.csv"
        sea_ice = pd.read_csv(noaa_url)

        sea_ice = sea_ice[["Year", "Extent"]]

        fig2 = px.line(
            sea_ice,
            x="Year",
            y="Extent",
            title="NOAA Arctic Sea Ice Extent (1979–Günümüz)"
        )

        fig2.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white", size=14),
    title=dict(
        text="NASA GISTEMP Küresel Sıcaklık Anomalisi (1880–Günümüz)",
        font=dict(size=22, color="white"),
        x=0.5
    ),
    xaxis=dict(
        title="Yıl",
        title_font=dict(size=16, color="white"),
        tickfont=dict(color="white"),
        gridcolor="rgba(255,255,255,0.2)"
    ),
    yaxis=dict(
        title="Sıcaklık Anomalisi (°C)",
        title_font=dict(size=16, color="white"),
        tickfont=dict(color="white"),
        gridcolor="rgba(255,255,255,0.2)"
    )
)
        st.plotly_chart(fig2, use_container_width=True)

    except:
        st.error("NOAA deniz buzu verisine erişilemedi.")
