import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

# -------------------------
# SAYFA AYARLARI
# -------------------------
st.set_page_config(
    page_title="Arctic Voices Digital",
    page_icon="🌍",
    layout="wide"
)

# -------------------------
# MODERN CSS TASARIM
# -------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: #4FC3F7;
}
.stMarkdown {
    font-size: 18px;
}
.sidebar .sidebar-content {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# BAŞLIK
# -------------------------
st.title("🌍 Arctic Voices Digital")
st.markdown("### Arktik Yerli Kültürlerini Tanıma Platformu")

st.markdown("---")

# -------------------------
# SIDEBAR MENU
# -------------------------
menu = st.sidebar.radio(
    "Menü",
    [
        "Ana Sayfa",
        "Kültürel Harita",
        "İklim Değişikliği Grafiği"
    ]
)

# -------------------------
# ANA SAYFA
# -------------------------
if menu == "Ana Sayfa":
    st.header("Proje Hakkında")
    st.write("""
    Arctic Voices Digital, Arktik yerli halklarının kültürlerini
    akademik ve saygı temelli bir yaklaşımla tanıtmayı amaçlayan
    dijital bir platformdur.
    """)

    st.info("Platform; kültür, coğrafya ve iklim verilerini bir arada sunar.")

# -------------------------
# HARİTA BÖLÜMÜ
# -------------------------
elif menu == "Kültürel Harita":

    st.header("🗺️ Arktik Yerli Halkları Haritası")

    data = pd.DataFrame({
        "Topluluk": ["Inuit", "Sami", "Nenets"],
        "lat": [64.2008, 68.9690, 67.5000],
        "lon": [-149.4937, 23.2710, 63.0000]
    })

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=data,
        get_position='[lon, lat]',
        get_radius=200000,
        get_fill_color=[79, 195, 247],
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=68,
        longitude=20,
        zoom=2,
        pitch=0,
    )

    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{Topluluk}"}
    )

    st.pydeck_chart(r)

# -------------------------
# İKLİM GRAFİĞİ
# -------------------------
elif menu == "İklim Değişikliği Grafiği":

    st.header("📊 Arktik Sıcaklık Artışı")

    # Örnek veri (temsilî)
    df = pd.DataFrame({
        "Yıl": [1980, 1990, 2000, 2010, 2020],
        "Sıcaklık Artışı (°C)": [0.3, 0.6, 0.9, 1.4, 2.1]
    })

    fig = px.line(
        df,
        x="Yıl",
        y="Sıcaklık Artışı (°C)",
        markers=True,
        title="Arktik Bölgesinde Ortalama Sıcaklık Artışı"
    )

    fig.update_layout(
        plot_bgcolor="#0E1117",
        paper_bgcolor="#0E1117",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)
