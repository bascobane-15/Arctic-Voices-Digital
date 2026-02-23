import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Sayfa Ayarları
st.set_page_config(page_title="Arctic Culture", page_icon="🌍", layout="wide")

# -------------------------
# GLASSMORPHISM & CUSTOM CSS
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

/* Sidebar ve genel metin renkleri */
[data-testid="stSidebar"] *, .stMarkdown, h1, h2, h3, p {
    color: white !important;
}

/* Kart Tasarımı (Glassmorphism) */
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    margin-bottom: 20px;
}

/* Radio buton yazıları */
div[role="radiogroup"] label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# SESSION STATE (OYUN PUANI İÇİN)
# -------------------------
if "puan" not in st.session_state:
    st.session_state.puan = 0
if "tamamlananlar" not in st.session_state:
    st.session_state.tamamlananlar = set()

# -------------------------
# SIDEBAR MENU
# -------------------------
st.sidebar.title("🧭 Menü")
menu = st.sidebar.selectbox(
    "Gitmek istediğiniz sayfa:",
    ["Ana Sayfa", "Kültürel Harita", "NASA İklim Verisi", "🎮 Kültür Keşfi"]
)

# Puanı sidebar'da göster
st.sidebar.divider()
st.sidebar.metric("🏆 Keşif Puanı", st.session_state.puan)

# -------------------------
# 1. ANA SAYFA
# -------------------------
if menu == "Ana Sayfa":
    st.title("🌍 Arctic Culture")
    st.markdown("### Arktik Yerli Kültürleri | Kültür • Coğrafya • İklim")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.header("Inuit")
        # st.image("inuit.jpg", use_container_width=True) # Resim varsa aktif et
        st.write("Kanada, Alaska ve Grönland bölgesinde yaşayan Arktik yerli halkıdır.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.header("Sami")
        # st.image("sami.jpg", use_container_width=True) # Resim varsa aktif et
        st.write("İskandinavya'nın kuzeyinde yaşayan yerli topluluktur.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.header("Nenets")
        # st.image("nenets.jpg", use_container_width=True) # Resim varsa aktif et
        st.write("Rusya tundra bölgesinde göçebe ren geyiği çobanlarıdır.")
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# 2. HARİTA
# -------------------------
elif menu == "Kültürel Harita":
    st.title("🗺️ Arktik Yerli Kültür Haritası")
    
    m = folium.Map(location=[70, 0], zoom_start=3, tiles="CartoDB dark_matter")
    
    # Koordinatlar ve Bilgiler
    locations = [
        {"loc": [64.2, -51.7], "name": "Inuit", "desc": "Kanada, Alaska ve Grönland"},
        {"loc": [68.5, 23.6], "name": "Sami", "desc": "İskandinavya'nın Kuzeyi"},
        {"loc": [67.5, 53.0], "name": "Nenets", "desc": "Sibirya Tundrası"}
    ]
    
    for item in locations:
        folium.Marker(
            location=item["loc"],
            popup=f"<b>{item['name']}</b><br>{item['desc']}",
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)

    st_folium(m, width=900, height=600)

# -------------------------
# 3. NASA VERİSİ
# -------------------------
elif menu == "NASA İklim Verisi":
    st.title("📈 NASA Sıcaklık Anomalisi")
    try:
        url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
        df = pd.read_csv(url, skiprows=1)
        df = df[["Year", "J-D"]]
        df.columns = ["Year", "Temperature"]
        df = df[df["Year"].apply(lambda x: str(x).isnumeric())] # Sadece sayısal yılları al
        
        fig = px.line(df, x="Year", y="Temperature", title="Küresel Sıcaklık Değişimi (1880-Günümüz)")
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font=dict(color="white"))
        st.plotly_chart(fig, use_container_width=True)
    except:
        st.error("NASA verisine şu an ulaşılamıyor.")

# -------------------------
# 4. KÜLTÜR KEŞFİ (OYUNLU BÖLÜM)
# -------------------------
elif menu == "🎮 Kültür Keşfi":
    st.title("🧭 Arctic Culture - Kültür Keşfi")
    
    culture = st.selectbox("Bir topluluk seç ve görevini tamamla:", ["Seçiniz", "Sami", "Inuit", "Nenets"])

    if culture == "Sami":
        st.header("🎭 Sami Kültürü")
        st.write("Sami halkı binlerce yıldır İskandinavya'nın en kuzeyinde doğayla iç içe yaşar.")
        
        # Öğretici İçerik
        st.subheader("🎵 Joik Müziği")
        st.write("Joik sadece bir şarkı değildir; o şeyi 'hatırlamak' değil, o şeyi 'oluşturmaktır'.")
        # st.video("https://www.youtube.com/watch?v=bLhmmChzkl0") 
        
        # Mini Görev
        st.markdown("---")
        st.subheader("🎯 Görev: Sami Bilgesi Ol!")
        soru = "Sami kültüründeki geleneksel şarkı söyleme biçimine ne ad verilir?"
        secim = st.radio("Cevabını seç:", ["Kanto", "Joik", "Haka"])
        
        if st.button("Kontrol Et"):
            if secim == "Joik":
                if "Sami" not in st.session_state.tamamlananlar:
                    st.session_state.puan += 10
                    st.session_state.tamamlananlar.add("Sami")
                st.success("✅ Doğru! +10 Puan Kazandın.")
                st.balloons()
            else:
                st.error("❌ Yanlış cevap, metni tekrar oku.")

    elif culture == "Inuit":
        st.header("🧊 Inuit Kültürü")
        st.write("Kutup dairesinin en zorlu şartlarında hayatta kalma ustaları.")
        
        st.subheader("🏠 İgloo Yapımı")
        st.write("İgloo sadece kardan bir ev değildir, mühendislik harikası bir ısı yalıtım sistemidir.")
        
        # Mini Görev
        st.markdown("---")
        st.subheader("🎯 Görev: Barınak Ustası!")
        soru = "İgloo yapımında hangi tip kar kullanılır?"
        secim = st.radio("Cevabını seç:", ["Yumuşak Toz Kar", "Sıkışmış Sert Kar", "Buz Parçaları"])
        
        if st.button("Kontrol Et"):
            if secim == "Sıkışmış Sert Kar":
                if "Inuit" not in st.session_state.tamamlananlar:
                    st.session_state.puan += 10
                    st.session_state.tamamlananlar.add("Inuit")
                st.success("✅ Doğru! Sert kar blokları rüzgarı keser ve yapıyı tutar. +10 Puan.")
                st.balloons()
            else:
                st.error("❌ Yanlış cevap! İpucu: Yapı için dayanıklı bir malzeme lazım.")

    elif culture == "Nenets":
        st.header("🦌 Nenets Kültürü")
        st.write("Sibirya'nın göçebe ren geyiği çobanları.")
        st.info("Bu bölümün detaylı içeriği yakında eklenecek. Ama bir deneme yapabilirsin!")
        
        # Mini Görev
        st.subheader("🎯 Görev: Sürü Yönetimi")
        soru = "Nenets halkı hangi hayvanın sürülerine rehberlik eder?"
        secim = st.radio("Cevabını seç:", ["At", "Ren Geyiği", "Koyun"])
        
        if st.button("Kontrol Et"):
            if secim == "Ren Geyiği":
                if "Nenets" not in st.session_state.tamamlananlar:
                    st.session_state.puan += 10
                    st.session_state.tamamlananlar.add("Nenets")
                st.success("✅ Doğru! Nenetsler geyikleriyle binlerce kilometre göç ederler. +10 Puan.")
                st.balloons()
            else:
                st.error("❌ Yanlış! Onlar 'Tundranın Kovboyları'dır ama başka bir hayvanla.")

# Tebrik mesajı
if st.session_state.puan >= 30:
    st.sidebar.success("🎉 TEBRİKLER! Tüm kültürleri keşfettin!")
