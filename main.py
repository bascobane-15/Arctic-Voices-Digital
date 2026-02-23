import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Arctic Culture", page_icon="🌍", layout="wide")

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

st.title("🌍 Arctic Culture")
st.markdown("### Arktik Yerli Kültürleri | Kültür • Coğrafya • İklim")

menu = st.sidebar.selectbox(
    "Sayfa Seç",
    ["Ana Sayfa", "Kültürel Harita", "NASA İklim Verisi", " Kültür Keşfi", "🎮Eğlenerek Öğrenelim" ]
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
# KÜLTÜR KEŞFİ
# -------------------------

elif menu == "Kültür Keşfi":

    st.title("🧭 Arctic Culture - Kültür Keşfi")
    st.write("Bir Arktik topluluğu seç ve kültürünü keşfet.")

    # 🎨 RADIO YAZI RENGİ DÜZELTME (BURAYA EKLENDİ)
    st.markdown("""
    <style>
    div[data-testid="stRadio"] label {
        color: white !important;
        font-weight: 500;
    }
    div[data-testid="stRadio"] div[role="radiogroup"] label {
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

    culture = st.selectbox(
        "Topluluk Seç:",
        ["Seçiniz", "Sami", "Inuit", "Nenets"]
    )

    # ===================== SAMI =====================
    if culture == "Sami":

        st.header("🎭 Sami Kültürü")

        # ================= Kıyafet =================
        st.subheader("👘 Geleneksel Kıyafet: Gákti")

        st.write("""
        Gákti, Sami halkının geleneksel kıyafetidir.
        Renkler ve desenler kişinin bölgesini ve aile bağlarını gösterebilir.
        """)

        st.image("gakti.jpg", use_container_width=True)

        st.divider()

        # ================= Müzik =================
        st.subheader("🎵 Joik Müziği")

        st.write("""
        Joik, Sami kültürüne özgü geleneksel bir vokal müzik formudur.
        Bir kişiyi, doğayı veya bir varlığı temsil eder.
        """)

        st.video("https://www.youtube.com/watch?v=bLhmmChzkl0")

        st.divider()

       
    # ===================== INUIT =====================
    elif culture == "Inuit":

        st.header("🧊 Inuit Kültürü")

        st.subheader("👘 Geleneksel Kıyafet")

        st.write("""
        Inuitler aşırı soğuk koşullara uyum sağlayan kürk parkalar giyerler.
        Bu parkalar genellikle fok veya karibu derisinden yapılır.
        Katmanlı yapı vücut ısısını korur.
        """)

        st.image("inuit_clothing.jpg", use_container_width=True)

        st.divider()
        
        st.subheader("🏠 İgloo ve Modern Yaşam")

        st.write("""
        İgloo kar bloklarından yapılan geçici barınaklardır.
        Günümüzde Inuit toplulukları modern evlerde yaşamaktadır,
        ancak geleneksel bilgi ve avcılık kültürü devam etmektedir.
        """)

        st.image("igloo.jpg", use_container_width=True)

        st.divider()

        st.info("💡 Inuit kültürü doğayla uyum, dayanıklılık ve topluluk dayanışmasına dayanır.")
    # ===================== NENETS =====================
    elif culture == "Nenets":
        st.header("Nenets Kültürü")
        st.write("Yakında eklenecek...")
        
   # -------------------------
   # 🎮Eğlenerek Öğrenelim
   # -------------------------

    elif menu == "🎮 Eğlenerek Öğrenelim":

       st.title("🎯 Arctic Bilgi Görevleri")
       st.write("Sayfalardaki bilgileri okuduysan şimdi kendini test etme vakti!")

    # Puanı ve tamamlananları saklamak için (Koda daha önce eklemediysen buraya ekliyoruz)
    if "puan" not in st.session_state:
        st.session_state.puan = 0
    if "tamamlananlar" not in st.session_state:
        st.session_state.tamamlananlar = set()

    # --- GÖREV 1: SAMI ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("1. Sami Kültür Görevi")
    if "Sami" in st.session_state.tamamlananlar:
        st.success("✅ Tamamlandı! (Joik Müziğini öğrendin)")
    else:
        secim1 = st.radio("Sami geleneksel müziğine ne ad verilir?", ["Kanto", "Joik", "Haka"], key="sami_q")
        if st.button("Sami Cevabını Onayla"):
            if secim1 == "Joik":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Sami")
                st.rerun()
            else:
                st.error("Yanlış! İpucu: Ana sayfadaki Sami kısmına bak.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- GÖREV 2: INUIT ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("2. Inuit Kültür Görevi")
    if "Inuit" in st.session_state.tamamlananlar:
        st.success("✅ Tamamlandı! (İgloo yapısını öğrendin)")
    else:
        secim2 = st.radio("İgloo inşasında hangi tip kar tercih edilir?", ["Yumuşak Kar", "Sıkışmış Sert Kar", "Islak Kar"], key="inuit_q")
        if st.button("Inuit Cevabını Onayla"):
            if secim2 == "Sıkışmış Sert Kar":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Inuit")
                st.rerun()
            else:
                st.error("Yanlış! İpucu: Sert bloklar rüzgara dayanır.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- GÖREV 3: NENETS ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("3. Nenets Kültür Görevi")
    if "Nenets" in st.session_state.tamamlananlar:
        st.success("✅ Tamamlandı! (Ren Geyiği Çobanlığını öğrendin)")
    else:
        secim3 = st.radio("Nenets halkı hangi hayvanın sürülerinden sorumludur?", ["Kutup Ayısı", "Ren Geyiği", "Kurt"], key="nenets_q")
        if st.button("Nenets Cevabını Onayla"):
            if secim3 == "Ren Geyiği":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Nenets")
                st.rerun()
            else:
                st.error("Yanlış! Onlar tundranın kadim geyik çobanlarıdır.")
    st.markdown('</div>', unsafe_allow_html=True)

    # Final Kutlaması
    if len(st.session_state.tamamlananlar) == 3:
        st.balloons()
        st.sidebar.success(f"🏆 Toplam Puanın: {st.session_state.puan}")
