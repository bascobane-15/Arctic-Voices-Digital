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
/* Arka Plan */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Seçeneklerin (Radio Buttons) Okunmasını Sağlayan Kısım */
div[data-testid="stRadio"] label p {
    color: white !important;
    font-weight: bold !important;
    text-shadow: 1px 1px 2px black; /* Yazıyı daha da belirgin yapar */
}

/* Glass-card tasarımı */
.glass-card {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🌍 Arctic Culture")
st.markdown("### Arktik Yerli Kültürleri | Kültür • Coğrafya • İklim")

menu = st.sidebar.selectbox(
    "Sayfa Seç",
    ["Ana Sayfa", "Kültürel Harita", "NASA İklim Verisi", "🧭 Kültür Keşfi", "🎮 Görev Merkezi"]
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

elif menu == "🧭 Kültür Keşfi":

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
        # --- DÜNYANIN İLK GÜNEŞ GÖZLÜĞÜ ---
        st.subheader("🕶️ Dünyanın İlk Güneş Gözlüğü")
        st.write("""
        **Puvirnituq:** Inuitler binlerce yıl önce fildişinden bu gözlükleri icat etti. 
        İnce bir çizgi sayesinde ışığı süzer ve kar körlüğünü engeller.
        """)
        # Daha doğrudan bir görsel yolu:
        st.image("https://raw.githubusercontent.com/MetMuseum/openaccess/master/Pre-Columbian/1978.412.301.jpg", caption="Geleneksel Inuit Kar Gözlüğü")

        st.divider()

        # --- DOKUNSAL HARİTALAR ---
        st.subheader("🗺️ Dokunsal Ahşap Haritalar")
        st.write("""
        **Ammassalik Ahşap Haritaları:** Karanlık kutup gecelerinde sadece dokunarak yolu bulmayı sağlayan 3 boyutlu kıyı haritalarıdır.
        """)
        # Müze kaynağı üzerinden doğrudan link:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4e/Wooden_map_Greenland.jpg", caption="Dokunsal Ahşap Harita")

        st.info("💡 İpucu: Eğer görseller hala yüklenmiyorsa, internet bağlantını kontrol edip sayfayı yenilemeyi dene.")
    # ===================== NENETS =====================
    elif culture == "Nenets":
        st.header("Nenets Kültürü")
        st.write("Yakında eklenecek...")
        
# -------------------------
# 5. SAYFA: OYUN SAYFASI (Test Alanı)
# -------------------------
elif menu == "🎮 Görev Merkezi":
    st.title("🎯 Arctic Bilgi Görevleri")
    st.write("Kültür Keşfi sayfasında öğrendiklerini kanıtlama vakti! Bakalım kaç puan toplayabileceksin?")

    # Puan sistemi kurulumu
    if "puan" not in st.session_state: st.session_state.puan = 0
    if "tamamlananlar" not in st.session_state: st.session_state.tamamlananlar = set()

    st.sidebar.metric("🏆 Toplam Puan", st.session_state.puan)

    # Seçeneklerin beyaz ve okunaklı olması için CSS
    st.markdown("""
        <style>
        div[data-testid="stRadio"] label p { color: white !important; font-size: 1.1rem; font-weight: 500; }
        </style>
    """, unsafe_allow_html=True)

    # --- 1. SAMI SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Sami" in st.session_state.tamamlananlar:
        st.success("✅ Sami bilgisi ustalıkla öğrenildi!")
    else:
        sami_q = st.radio("❄️ Sami halkının kadim vokal sanatına ne denir?", ["Kanto", "Joik", "Haka"], key="q1")
        if st.button("Sami Cevabını Onayla"):
            if sami_q == "Joik":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Sami")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 2. INUIT SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Inuit" in st.session_state.tamamlananlar:
        st.success("✅ Inuit bilgisi ustalıkla öğrenildi!")
    else:
        inuit_q = st.radio("🏠 İgloo inşasında en önemli malzeme hangisidir?", ["Toz Kar", "Buz Kalıpları", "Sıkışmış Sert Kar"], key="q2")
        if st.button("Inuit Cevabını Onayla"):
            if inuit_q == "Sıkışmış Sert Kar":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Inuit")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 3. NENETS SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Nenets" in st.session_state.tamamlananlar:
        st.success("✅ Nenets bilgisi ustalıkla öğrenildi!")
    else:
        nenets_q = st.radio("🦌 Nenets halkı hangi hayvanın sürülerine rehberlik eder?", ["Ren Geyiği", "Kutup Ayısı", "Kurt"], key="q3")
        if st.button("Nenets Cevabını Onayla"):
            if nenets_q == "Ren Geyiği":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Nenets")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 4. NAVİGASYON SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Inukshuk" in st.session_state.tamamlananlar:
        st.success("✅ Navigasyon bilgisi tamam!")
    else:
        nav_q = st.radio("🗿 Arctic bölgelerinde yol bulmak veya bir yeri işaretlemek için üst üste dizilen taşlara ne denir?", ["Totem", "Inukshuk", "Piramit"], key="q4")
        if st.button("Navigasyon Cevabını Onayla"):
            if nav_q == "Inukshuk":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Inukshuk")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. ULAŞIM SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Ulasim" in st.session_state.tamamlananlar:
        st.success("✅ Ulaşım kültürü öğrenildi!")
    else:
        trans_q = st.radio("🐕 Inuitlerin geleneksel kış ulaşımında en çok güvendiği araç hangisidir?", ["Köpek Kızağı (Qamutik)", "Kar Arabası", "At Arabası"], key="q5")
        if st.button("Ulaşım Cevabını Onayla"):
            if trans_q == "Köpek Kızağı (Qamutik)":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Ulasim")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 6. SANAT SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Sanat" in st.session_state.tamamlananlar:
        st.success("✅ Arctic sanatı keşfedildi!")
    else:
        art_q = st.radio("🎨 Inuit sanatında heykel yapmak için en çok kullanılan yumuşak ve doğal taş hangisidir?", ["Mermer", "Granit", "Sabun Taşı (Soapstone)"], key="q6")
        if st.button("Sanat Cevabını Onayla"):
            if art_q == "Sabun Taşı (Soapstone)":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Sanat")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 7. AV ARAÇLARI SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Av" in st.session_state.tamamlananlar:
        st.success("✅ Hayatta kalma araçları öğrenildi!")
    else:
        hunt_q = st.radio("🛶 Inuitlerin denizde fok veya balina avlamak için kullandığı tek kişilik deri kaplı kanoya ne denir?", ["Kano", "Kayak", "Sal"], key="q7")
        if st.button("Avcılık Cevabını Onayla"):
            if hunt_q == "Kayak":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Av")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    # --- 8. KUTUP AYISI SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "KutupAyisi" in st.session_state.tamamlananlar:
        st.success("✅ Kutup ayısı uzmanlığı tamam!")
    else:
        bear_q = st.radio("🐻 Kutup ayılarının derisi aslında ne renktir?", ["Beyaz", "Siyah", "Pembe"], key="q8")
        if st.button("Ayı Bilgisini Onayla"):
            # İlginç bilgi: Kutup ayılarının tüyleri şeffaftır, altındaki derileri güneş ısısını emmek için siyahtır!
            if bear_q == "Siyah":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("KutupAyisi")
                st.rerun()
            else:
                st.error("Yanlış! İpucu: Güneş ısısını en iyi hangi renk emer?")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 9. NARVAL (DENİZ GERGEDANI) SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Narval" in st.session_state.tamamlananlar:
        st.success("✅ Deniz Gergedanı uzmanlığı tamam!")
    else:
        narval_q = st.radio("🦄 'Deniz Tekboynuzu' olarak bilinen, uzun bir dişi olan kutup canlısı hangisidir?", ["Mors", "Narval", "Beluga"], key="q9")
        if st.button("Narval Cevabını Onayla"):
            if narval_q == "Narval":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Narval")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 10. KUZEY IŞIKLARI SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Aurora" in st.session_state.tamamlananlar:
        st.success("✅ Gökyüzü olayları öğrenildi!")
    else:
        aurora_q = st.radio("✨ Kuzey gökyüzünde görülen renkli ışık dansına ne ad verilir?", ["Aurora Borealis", "Meteor Yağmuru", "Samanyolu"], key="q10")
        if st.button("Aurora Cevabını Onayla"):
            if aurora_q == "Aurora Borealis":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Aurora")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 11. HAYVAN ADAPTASYONU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Adaptasyon" in st.session_state.tamamlananlar:
        st.success("✅ Hayatta kalma uzmanlığı!")
    else:
        adapt_q = st.radio("🦊 Arctic tilkisi (Kutup Tilkisi) neden kışın beyaz, yazın ise kahverengidir?", ["Moda için", "Kamuflaj (Gizlenme) için", "Daha iyi duymak için"], key="q11")
        if st.button("Adaptasyon Cevabını Onayla"):
            if adapt_q == "Kamuflaj (Gizlenme) için":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Adaptasyon")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 12. MORS SORUSU ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "Mors" in st.session_state.tamamlananlar:
        st.success("✅ Mors bilgisi eklendi!")
    else:
        walrus_q = st.radio("🐘 Hangi Arctic hayvanı devasa dişlerini buzun üzerine tırmanmak için bir 'çapa' gibi kullanır?", ["Mors", "Fok", "Deniz Aslanı"], key="q12")
        if st.button("Mors Cevabını Onayla"):
            if walrus_q == "Mors":
                st.session_state.puan += 10
                st.session_state.tamamlananlar.add("Mors")
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # Final Durumu
    if len(st.session_state.tamamlananlar) == 12:
        st.balloons()
        st.success("🎉 İNANILMAZ! 12 Görevin tamamını bitirdin ve gerçek bir 'Kutup Kaşifi' oldun!")
