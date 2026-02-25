import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import folium
import time
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
    ["🏔️Ana Sayfa", "🗺️Kültürel Harita", "🛰️ NASA İklim Verisi", "🧭 Kültür Keşfi", "🎮 Görev Merkezi"]
)
# -------------------------
# ANA SAYFA - EĞİTSEL ARKTIK SÖZLÜĞÜ
# -------------------------
if menu == "🏔️Ana Sayfa":

    import random

    # Kelime listesi - Tüm virgüller ve parantezler kontrol edildi
    kelimeler = [
        {"kelime": "İglo", "dil": "İnuit Mühendisliği", "anlam": "Sıkıştırılmış kardan yapılan, dışarısı -40 dereceye kadar düşse de içindeki insan ısısını hapseden efsanevi kubbe evler."},
        {"kelime": "Kutup Sumrusu", "dil": "Doğa Gezgini", "anlam": "Dünyanın en büyük yolcusu! Her yıl Kuzey ve Güney kutbu arasında uçarak hayatı boyunca Ay'a 3 kez gidip gelecek kadar yol kateder."},
        {"kelime": "Albedo", "dil": "İklim Bilimi", "anlam": "Buzulların güneş ışığını bir ayna gibi uzaya geri yansıtma gücü. Buzlar eridikçe dünya bu koruyucu aynasını kaybeder."},
        {"kelime": "Kuzey Işıkları", "dil": "Gök Olayı", "anlam": "Aurora Borealis! Güneşten gelen fırtınaların gece gökyüzünü yeşil ve mor bir dans pistine çevirdiği büyüleyici ışık gösterisi."},
        {"kelime": "Tundra", "dil": "Coğrafya", "anlam": "Yılın büyük bölümü donmuş olan, ağaçsız ama yazın rengarenk yosun ve çiçeklerle kaplanan devasa Arktik düzlükler."}
    ]

    # Her yenilemede bu 5 tanesinden birini rastgele seçer
    gunun_kelimesi = random.choice(kelimeler)

    # Arktik Kaşif Notu Kutusu
    st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.05); 
                    padding: 20px; 
                    border-radius: 12px; 
                    border: 1px dashed #3498db; 
                    margin-top: 10px;
                    margin-bottom: 20px;">
            <span style="color: #3498db; font-weight: bold; font-size: 1.1em;">❄️ Arktik Kaşif Notu:</span>
            <div style="margin-top: 10px;">
                <span style="color: white; font-size: 1.2em;"><b>{gunun_kelimesi['kelime']}</b></span>
                <span style="color: #a0a0a0; font-size: 0.9em; margin-left: 5px;">({gunun_kelimesi['dil']})</span>
                <p style="color: white; margin-top: 8px; line-height: 1.5;">{gunun_kelimesi['anlam']}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- KARTLAR (BOŞLUKLARI ÖNLEMEK İÇİN BİRLEŞİK YAPI) ---
    
    # 1. INUIT
    st.markdown('<div class="glass-card"><h2 style="color: white; margin-top: 0;">Inuit</h2>', unsafe_allow_html=True)
    st.image("inuit.jpg", use_container_width=True)
    st.write("Kanada, Alaska ve Grönland bölgesinde yaşayan Arktik yerli halkıdır.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. SAMI
    st.markdown('<div class="glass-card"><h2 style="color: white; margin-top: 0;">Sami</h2>', unsafe_allow_html=True)
    st.image("sami.jpg", use_container_width=True)
    st.write("İskandinavya'nın kuzeyinde yaşayan yerli topluluktur.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. NENETS
    st.markdown('<div class="glass-card"><h2 style="color: white; margin-top: 0;">Nenets</h2>', unsafe_allow_html=True)
    st.image("nenets.jpg", use_container_width=True)
    st.write("Rusya tundra bölgesinde göçebe ren geyiği çobanlarıdır.")
    st.markdown('</div>', unsafe_allow_html=True)
    
# -------------------------
# EĞLENCELİ KÜLTÜREL HARİTA
# -------------------------
if menu == "🗺️Kültürel Harita":

    st.title("✈️ Türkiye'den Arktik'e Yolculuk")
    st.subheader("Yerli Halkların İzinde Bir Keşif Rotası")

    # Harita merkezi (Görünümü Türkiye ve Arktik arasını kapsayacak şekilde ayarladım)
    m = folium.Map(
        location=[55, 20], 
        zoom_start=3, 
        tiles="CartoDB dark_matter"
    )

    # 1. TÜRKİYE (BAŞLANGIÇ NOKTASI)
    folium.Marker(
        location=[39.9, 32.8], # Ankara
        popup="<b>Burası Evimiz!</b><br>Arktik yolculuğu buradan başlıyor. 🚀",
        icon=folium.Icon(color="red", icon="home", prefix="fa")
    ).add_to(m)

    # 2. HALKLAR VE ÖZEL İKONLAR (EMOJİLERLE)
    # Inuit (Küçük Eskimo Emojisi)
    folium.Marker(
        location=[64.2, -51.7],
        popup="<b>İnuitler</b><br>❄️ Buzun ve karın koruyucuları.",
        icon=folium.DivIcon(html=f"""<div style="font-size: 30px;">🧑‍🌾</div>""")
    ).add_to(m)

    # Sami (Ren Geyiği Emojisi)
    folium.Marker(
        location=[68.5, 23.6],
        popup="<b>Samiler</b><br>🦌 Ren geyikleriyle yaşayan kadim halk.",
        icon=folium.DivIcon(html=f"""<div style="font-size: 30px;">🦌</div>""")
    ).add_to(m)

    # Nenets (Çadır Emojisi)
    folium.Marker(
        location=[67.5, 53.0],
        popup="<b>Nenetsler</b><br>⛺ Tundranın göçebe çobanları.",
        icon=folium.DivIcon(html=f"""<div style="font-size: 30px;">⛺</div>""")
    ).add_to(m)

    # 3. UÇAK ROTASI (TÜRKİYE -> ARKTIK)
    # Ankara'dan her bir merkeze giden kesikli uçuş çizgileri
    rota_inuit = [[39.9, 32.8], [64.2, -51.7]]
    rota_sami = [[39.9, 32.8], [68.5, 23.6]]
    rota_nenets = [[39.9, 32.8], [67.5, 53.0]]

    folium.PolyLine(rota_inuit, color="#3498db", weight=2.5, opacity=0.8, dash_array='10').add_to(m)
    folium.PolyLine(rota_sami, color="#2ecc71", weight=2.5, opacity=0.8, dash_array='10').add_to(m)
    folium.PolyLine(rota_nenets, color="#e74c3c", weight=2.5, opacity=0.8, dash_array='10').add_to(m)

    # Rotanın ortasına küçük bir uçak ikonu (Opsiyonel görsel şölen)
    folium.Marker(
        location=[55, 10], 
        icon=folium.DivIcon(html=f"""<div style="font-size: 20px; transform: rotate(45deg);">✈️</div>""")
    ).add_to(m)

    # Haritayı göster
    # width=None ve use_container_width=True beraber kullanılır
    from streamlit_folium import st_folium
    
    st_folium(
        m, 
        width=None, 
        height=500, 
        use_container_width=True
    )

    st.markdown("""
        <div style="background-color: rgba(52, 152, 219, 0.2); 
                    padding: 15px; 
                    border-radius: 10px; 
                    margin-top: 20px;
                    border: 1px solid #3498db;
                    text-align: center;">
            <p style="color: #F1C40F; font-weight: bold; margin: 0; font-size: 1.1em;">
                💡 İpucu: Haritadaki simgelere tıklayarak detayları görebilirsin. 
                Kesikli çizgiler Türkiye'den olan uçuş rotalarımızı temsil eder!
            </p>
        </div>
    """, unsafe_allow_html=True)
# -------------------------
# ARKTIK ÖYKÜ VE KÜLTÜR PANELİ
# -------------------------
    st.markdown("---")
    st.title("❄️ Arktik'in Hikayesi: Yerli Kültürler")

# 1. BÜTÜNSEL GÖRÜNÜM (ZİHİN HARİTASI)
# Kullanıcı önce burayı görür, tıkladığında slaytları açar
with st.expander("🌐 Arktik Çevre ve Kültür Zihin Haritasını Gör", expanded=True):
    # Buraya senin paylaştığın bütünsel zihin haritası görselini koyuyoruz
    st.image("https://files.storyboardthat.com/storyboard-src/tr-classic/arctic-environment-and-cultures-indigenous-peoples.png", 
             use_container_width=True, 
             caption="Arktik Kültür Sistemi - Birleşik Görünüm")
    st.info("💡 Aşağıdaki slaytlar üzerinden her bir bölümü detaylıca inceleyebilir ve sesli dinleyebilirsiniz.")

# 2. ETKİLEŞİMLİ SLAYT SİSTEMİ
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0

# Senin verdiğin 7 Slaytlık İçerik Yapısı
slides = [
    {"baslik": "📍 YER", "metin": "Arktik ve Kuzey Kutup Bölgesi, kuzey Kanada, Alaska ve Grönland'da yer almaktadır. Pasifik Okyanusu'ndaki Bering denizinden Atlantik Okyanusu'ndaki Labrador Denizi'ne kadar uzanır.", "img": "https://www.storyboardthat.com/storyboard-src/tr-classic/arctic-location-zoom.png", "ses": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"},
    {"baslik": "🌌 ÇEVRE", "metin": "Arazi, donmuş tundradan boreal ormanlara kadar değişir. Aurora borealis (Kuzey Işıkları) bu bölgelerde gökyüzünü süsler.", "img": "https://www.storyboardthat.com/storyboard-src/tr-classic/arctic-environment-zoom.png", "ses": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3"},
    {"baslik": "💎 DOĞAL KAYNAKLAR", "metin": "Foklar, orca, kutup ayıları, ren geyikleri ve kurtlar gibi birçok hayvan bu dondurucu ekosistemin parçasıdır.", "img": "https://www.storyboardthat.com/storyboard-src/tr-classic/arctic-resources-zoom.png", "ses": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3"},
    {"baslik": "🏠 EVLER", "metin": "İglolar, buzdan yapılmış 20 kişiyi barındırabilen geçici barınaklardır. Yazın ise hayvan derilerinden Tipiler inşa edilir.", "img": "https://www.storyboardthat.com/storyboard-src/tr-classic/arctic-homes-zoom.png", "ses": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3"},
    {"baslik": "🏹 KIYAFETLER VE BULUŞLAR", "metin": "Kürkten yapılan mukluklar ve fildişinden oyulmuş kar gözlükleri, hayatta kalmak için icat edilen muazzam araçlardır.", "img": "https://www.storyboardthat.com/storyboard-src/tr-classic/arctic-inventions-zoom.png", "ses": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3"},
    {"baslik": "🤝 GELENEKLER", "metin": "Avcılar 'deniz tanrıçasına' teşekkür eder. Bir hayvanın hiçbir parçası asla ziyan edilmez; bu bir saygı kuralıdır.", "img": "https://www.storyboardthat.com/storyboard-src/tr-classic/arctic-traditions-zoom.png", "ses": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3"},
    {"baslik": "👥 YERLİ İNSANLAR", "metin": "Inuit, Aleut, Yu'pik ve Cree gibi halklar bu toprakların kadim koruyucularıdır.", "img": "https://www.storyboardthat.com/storyboard-src/tr-classic/arctic-people-zoom.png", "ses": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3"}
]

# Slayt Arayüzü
slide_data = slides[st.session_state.current_slide]

# İki Kolonlu Yapı: Sol Görsel, Sağ Metin ve Ses
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.image(slide_data["img"], use_container_width=True)

with col_right:
    st.subheader(f"Slayt {st.session_state.current_slide + 1}: {slide_data['baslik']}")
    st.write(slide_data["metin"])
    st.write("---")
    st.write("🎧 **Sesli Anlatım:**")
    st.audio(slide_data["ses"])

# Navigasyon Butonları
nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 3])
with nav_col1:
    if st.button("⬅️ Geri") and st.session_state.current_slide > 0:
        st.session_state.current_slide -= 1
        st.rerun()
with nav_col2:
if st.button("İleri ➡️") and st.session_state.current_slide < len(slides) - 1:
        st.session_state.current_slide += 1
        st.rerun()

# -------------------------
# NASA İKLİM VERİSİ
# -------------------------

elif menu == "🛰️ NASA İklim Verisi":
    st.title("📈 NASA GISTEMP Küresel Sıcaklık Anomalisi")

    try:
        # Veri çekme işlemi
        url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
        df = pd.read_csv(url, skiprows=1)

        # Veri temizleme
        df = df[["Year", "J-D"]]
        df.columns = ["Year", "Temperature"]
        
        # 'Temperature' sütunundaki sayısal olmayan değerleri temizle
        df['Temperature'] = pd.to_numeric(df['Temperature'], errors='coerce')
        df = df.dropna()

        # Son ölçülen anomali değerini al (İnovasyon için)
        latest_temp = df['Temperature'].iloc[-1]
        latest_year = df['Year'].iloc[-1]

        # Grafik oluşturma
        fig = px.line(
            df,
            x="Year",
            y="Temperature",
            title=f"NASA GISTEMP Küresel Sıcaklık Değişimi (Son Ölçüm: {latest_year})"
        )

        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            title=dict(font=dict(size=22, color="white"), x=0.5),
            xaxis=dict(title="Yıl", gridcolor="rgba(255,255,255,0.1)"),
            yaxis=dict(title="Sıcaklık Anomalisi (°C)", gridcolor="rgba(255,255,255,0.1)")
        )

        st.plotly_chart(fig, use_container_width=True)

        # --- İNOVATİF ANALİZ KUTUSU (BEYAZ YAZI) ---
        st.divider()
        
        status_color = "rgba(231, 76, 60, 0.2)" if latest_temp > 1.0 else "rgba(52, 152, 219, 0.2)"
        border_color = "#e74c3c" if latest_temp > 1.0 else "#3498db"
        
        # DİKKAT: Başta 3 tırnak (f""") ve sonda 3 tırnak (""") olmalı
        st.markdown(f"""
            <div style="background-color: {status_color}; 
                        padding: 25px; 
                        border-radius: 15px; 
                        border-left: 8px solid {border_color};
                        margin-top: 20px;">
                <h3 style="color: white; margin-top: 0;">🌍 Canlı Veri Analizi ({latest_year})</h3>
                <p style="color: white; font-size: 1.1em;">
                    NASA verilerine göre küresel sıcaklık artışı şu anda <b>{latest_temp}°C</b> seviyesinde. 
                </p>
            </div>
        """, unsafe_allow_html=True)

        # --- YENİ EKLEDİĞİMİZ RENKLİ CÜMLE VE ZAMAN MAKİNESİ ---
        # ÖNEMLİ: Bu satırlar 'try' ile aynı hizada değil, daha İÇERİDE olmalı!
        st.markdown("---")
        st.markdown("### 🕒 İklim Zaman Makinesi: Neler Değişiyor?")
        
        st.markdown("""
            <div style="background-color: rgba(52, 152, 219, 0.2); 
                        padding: 10px; 
                        border-radius: 5px; 
                        margin-bottom: 20px;
                        border: 1px solid #3498db;">
                <p style="color: #F1C40F; font-weight: bold; margin: 0; text-align: center;">
                    ❄️ Sıcaklık artışının Arktik yaşamı üzerindeki etkilerini görmek için başlıklara tıklayın.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Şık, genişletilebilir (expander) bir kronoloji
        with st.expander("🔵 +0.5°C: Geleneksel Yaşamın Zirvesi"):
            st.write("""
                Bu dönemde deniz buzu (Siku) kalındı. Inuit avcıları güvenle buzun üzerine çıkabiliyor, 
                İglolar kış boyunca erimeden kalabiliyordu. Doğal denge tamdı.
            """)

        with st.expander("🟡 +1.0°C: Değişimin Başlangıcı"):
            st.write("""
                **Albedo Etkisi** zayıflamaya başladı. Buzlar daha erken eriyor, ren geyikleri (Nenetslerin can damarı) 
                göç yollarındaki nehirleri geçmekte zorlanıyor.
            """)

        with st.expander("🟠 +1.5°C: Kritik Eşik (Şu Anki Durum)"):
            st.write("""
                NASA verilerinin gösterdiği bu noktada, permafrost (donmuş toprak) eriyor. 
                Sami halkının köylerinde zemin kaymaları görülmeye başladı. Kuzey Sumrusu'nun durakladığı 
                kıyı şeritleri sular altında kalma riskiyle karşı karşıya.
            """)

        with st.expander("🔴 +2.0°C ve Ötesi: Belirsiz Gelecek"):
            st.error("""
                Bu seviyede 'Siku' yani kalıcı deniz buzu tamamen yok olabilir. 
                Bu, sadece bir buzun erimesi değil, binlerce yıllık bir kültürün kütüphanesinin yanması demektir.
            """)
            
    except Exception as e:
        st.error(f"NASA verisine şu an erişilemiyor. Hata: {e}")
    except Exception as e:
        st.error(f"NASA verisine şu an erişilemiyor. Lütfen internet bağlantınızı kontrol edin. Hata: {e}")

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
        # ================= El Sanatları =================
        st.subheader("🛠️ Geleneksel El Sanatı: Duodji")

        st.write("""
        Duodji, sadece bir el sanatı değil, Sami halkının doğayla kurduğu bağın bir yansımasıdır. 
        Her bir parça, doğaya saygı duyularak ve sadece ihtiyaç kadar malzeme alınarak üretilir.
        """)

        # GitHub'a yüklediğin görseli buraya ekliyoruz
        st.image("duodji.jpg", caption="Geleneksel Sami El Sanatları: Duodji", use_container_width=True)

        # BEYAZ YAZILI BİLGİ KUTUSU
        st.markdown("""
            <div style="background-color: rgba(243, 156, 18, 0.2); 
                        padding: 20px; 
                        border-radius: 10px; 
                        border-left: 5px solid #f39c12;
                        margin: 10px 0px;">
                <span style="color: white; font-weight: bold; font-size: 1.1em;">💡 İnanılmaz Teknik Detay: Kuksa ve Dokuma Sanatı</span>
                <p style="color: white; margin-top: 10px; line-height: 1.6;">
                Duodji'nin en bilinen örneği 'Kuksa' adı verilen ahşap bardaklardır. Bu bardaklar sıradan bir odun parçasından değil, 
                huş ağacının üzerinde oluşan 'yumru' (burl) kısmından elle oyulur. Bu özel yapı sayesinde Kuksa asla çatlamaz, 
                ısıyı mükemmel yalıtır ve ömür boyu kullanılabilir. 
                <br><br>
                Ayrıca, <b>yumuşak Duodji</b> olarak bilinen el dokuması ürünlerde, ren geyiği sinirlerinden yapılan ipler ve bitkisel boyalarla 
                renklendirilmiş yünler kullanılarak, doğanın geometrisini yansıtan ve her biri bir hikaye anlatan eşsiz desenler dokunur.
                </p>
            </div>
        """, unsafe_allow_html=True)
       
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
        # Dosyayı bilgisayarından 'kar_gozlugu.jpg' adıyla yüklediğini varsayıyorum:
        st.image("kar_gozlugu.jpg", caption="Geleneksel Inuit Kar Gözlüğü")

        st.divider()

        # --- DOKUNSAL HARİTALAR ---
        st.subheader("🗺️ Dokunsal Ahşap Haritalar")
        st.write("""
        **Ammassalik Ahşap Haritaları:** Karanlık kutup gecelerinde sadece dokunarak yolu bulmayı sağlayan 3 boyutlu kıyı haritalarıdır.
        """)
        # Dosyayı bilgisayarından 'dokunsal_harita.jpg' adıyla yüklediğini varsayıyorum:
        st.image("dokunsal_harita.jpg", caption="Ammassalik Dokunsal Haritası")

        st.markdown("""
    <div style="background-color: rgba(13, 110, 253, 0.2); 
                padding: 20px; 
                border-radius: 10px; 
                border-left: 5px solid #0d6efd;
                margin: 10px 0px;">
        <span style="color: white; font-weight: bold;">💡 İnanılmaz Teknik Detay:</span>
        <p style="color: white; margin-top: 10px;">
        Bu ahşap haritalar o kadar hassas yontulmuştur ki, Inuitler eldivenlerini çıkarmadan, 
        sadece başparmaklarıyla ahşap üzerindeki oyukları takip ederek hangi koyda veya burunda olduklarını %100 doğrulukla anlayabilirler. 
        Ayrıca denize düştüğünde batmazlar ve zifiri karanlıkta (kutup gecesinde) bile çalışmaya devam eden dünyanın tek 'analog GPS' sistemidir.
        </p>
    </div>
""", unsafe_allow_html=True)
        st.divider()

        # --- İNOVATİF ARKTİK RADYOSU ---
        st.subheader("📻 Arktik Radyosu: Inuit Frekansı")
        with st.expander("🎧 Kutup Seslerini Dinlemek İçin Tıkla"):
            st.write("Şu an Grönland kıyılarında bir buzun çatırmasını ve kutup rüzgarını duyuyorsunuz...")
            # Yeni ve daha stabil link:
            st.audio("https://www.mfiles.co.uk/mp3-downloads/wind-howl-storm.mp3")
    # ===================== NENETS =====================
    elif culture == "Nenets":
        st.header("🦌 Nenets Kültürü: Tundra'nın Göçebe Efendileri")
        
        st.write("""
        Nenets halkı, Sibirya'nın en kuzeyinde, sıcaklığın **-50°C**'ye kadar düştüğü Yamal Yarımadası'nda yaşar. 
        Binlerce yıldır ren geyikleriyle birlikte dünyanın en uzun göç yollarından birini tamamlarlar.
        """)

        # Mevcut nenets.jpg dosyanı kullanıyoruz
        st.image("nenets2.jpg", caption="Geleneksel Nenets Yaşamı ve Ren Geyikleri")

        st.divider()

        # --- AZ BİLİNEN BİLGİ: CHUM ÇADIRLARI ---
        st.subheader("🏠 Hareketli Evler: Chum")
        st.write("""
        Nenetslerin 'Chum' adını verdikleri çadırları, ren geyiği derisinden yapılır. 
        Bu çadırlar o kadar pratiktir ki, göç sırasında sadece **40 dakika** içinde kurulup sökülebilir. 
        Bir aile yılda yaklaşık **1000 kilometreden fazla** yol kat eder ve her duraklamada bu evi yeniden kurar.
        """)
        
        # Eklediğimiz görsel satırı:
        st.image("chum.jpg", caption="Geleneksel Nenets Çadırı: Chum")

        st.divider()

        # --- NENETS DİLİ VE DOĞA  ---
        st.markdown("""
            <div style="background-color: rgba(52, 152, 219, 0.2); 
                        padding: 20px; 
                        border-radius: 10px; 
                        border-left: 5px solid #3498db;
                        margin: 10px 0px;">
                <span style="color: white; font-weight: bold;">❄️ Dilin Gücü:</span>
                <p style="color: white; margin-top: 10px;">
                Nenets dilinde 'kar'ı tanımlamak için kullanılan onlarca farklı kelime vardır. 
                Karın sertliğine, rengine ve sürüşe uygunluğuna göre her durumu ayrı bir kelimeyle ifade ederler.
                </p>
            </div>
        """, unsafe_allow_html=True)
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
