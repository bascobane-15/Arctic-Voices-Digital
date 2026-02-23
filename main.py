import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

st.set_page_config(page_title="Arctic Voices Digital", page_icon="🌍", layout="wide")

# -------------------------
# GLASSMORPHISM CSS
# -------------------------
st.markdown("""
<style>

.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
    margin: 15px 0px;
    border: 1px solid rgba(255,255,255,0.2);
    transition: all 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 15px 35px rgba(0,0,0,0.5);
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

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="glass-card">
            <h2>Inuit</h2>
            <img src="inuit.jpg" width="100%">
            <p>Kanada, Alaska ve Grönland bölgesinde yaşayan Arktik yerli halkıdır.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="glass-card">
            <h2>Sami</h2>
            <img src="sami.jpg" width="100%">
            <p>İskandinavya'nın kuzeyinde yaşayan yerli topluluktur.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card">
        <h2>Nenets</h2>
        <img src="nenets.jpg" width="100%">
        <p>Rusya tundra bölgesinde göçebe ren geyiği çobanlarıdır.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# HARİTA
# -------------------------
elif menu == "Kültürel Harita":

    st.header("🗺️ Yerli Halkların Coğrafi Dağılımı")

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

    view_state = pdk.ViewState(latitude=68, longitude=20, zoom=2)

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{Topluluk}"}
    ))

# -------------------------
# NASA GERÇEK VERİ
# -------------------------
elif menu == "NASA İklim Verisi":

    st.header("📈 NASA GISTEMP Arktik Sıcaklık Anomalisi")

    # NASA GISTEMP veri seti (gerçek veri)
    url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
    df = pd.read_csv(url, skiprows=1)

    df = df[["Year", "J-D"]]
    df.columns = ["Year", "Temperature Anomaly"]
    df = df.dropna()

    fig = px.line(df, x="Year", y="Temperature Anomaly",
                  title="NASA Küresel Sıcaklık Anomalisi (1880-Günümüz)")

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white")
    )

    st.plotly_chart(fig, use_container_width=True)
