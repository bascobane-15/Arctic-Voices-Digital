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

menu = st.sidebar.selectbox(
    "Sayfa Seç",
    ["Ana Sayfa", "Kültürel Harita", "NASA İklim Verisi", "🎮 Kültür Keşfi"]
)

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

elif menu == "NASA İklim Verisi":

    st.title("📈 NASA GISTEMP Küresel Sıcaklık Anomalisi")

    try:
        url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
        df = pd.read_csv(url, skiprows=1)

        df = df[["Year", "J-D"]]
        df.columns = ["Year", "Temperature"]
        df = df.dropna()

        fig = px.line(
            df,
            x="Year",
            y="Temperature",
            title="NASA GISTEMP Küresel Sıcaklık Anomalisi (1880–Günümüz)"
        )

        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            title=dict(font=dict(size=22, color="white"), x=0.5),
            xaxis=dict(
                title="Yıl",
                gridcolor="rgba(255,255,255,0.2)"
            ),
            yaxis=dict(
                title="Sıcaklık Anomalisi (°C)",
                gridcolor="rgba(255,255,255,0.2)"
            )
        )

        st.plotly_chart(fig, use_container_width=True)

    except:
        st.error("NASA verisine erişilemedi.")
# -------------------------
# KÜLTÜRKEŞFİ
# -------------------------

elif menu == "🎮 Kültür Keşfi":

    st.title("🧭 Arctic Voices - Kültür Keşfi")

    st.write("Bir Arktik topluluğu seç ve kültürünü keşfet.")

    culture = st.selectbox(
        "Topluluk Seç:",
        ["Seçiniz", "Inuit", "Sami", "Nenets"]
    )

    # ===================== SAMI =====================

    if culture == "Sami":

        st.header("🎭 Sami Kültürü")

        st.subheader("👘 Geleneksel Kıyafet: Gákti")

        st.write("""
        Gákti, Sami halkının geleneksel kıyafetidir.
        Renkler ve desenler kişinin bölgesini ve aile bağlarını gösterebilir.
        Törenlerde ve günlük yaşamda farklı versiyonları kullanılır.
        """)

        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/5/5e/Sami_people_traditional_clothing.jpg",
            use_container_width=True
        )

        st.divider()

        st.subheader("🎵 Joik Müziği")

        st.write("""
        Joik, Sami kültürüne özgü geleneksel bir vokal müzik formudur.
        Bir kişiyi, hayvanı ya da doğa unsurunu temsil eder.
        Şarkı söylemekten çok, 'varlığı sesle ifade etme' geleneğidir.
        """)

        st.video("https://www.youtube.com/watch?v=4YFJxZ3kzv4")

        st.divider()

        st.subheader("🧠 Mini Quiz")

        answer = st.radio(
            "Gákti hangi topluluğa aittir?",
            ["Inuit", "Sami", "Nenets"]
        )

        if answer == "Sami":
            st.success("🎉 Doğru! Sami kültürünü keşfettin!")
            st.balloons()
        elif answer:
            st.error("❌ Tekrar dene!")

    # ===================== DİĞERLERİ =====================

    elif culture == "Inuit":
        st.header("Inuit Kültürü")
        st.write("Yakında eklenecek...")

    elif culture == "Nenets":
        st.header("Nenets Kültürü")
        st.write("Yakında eklenecek...")

