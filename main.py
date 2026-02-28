import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk
import folium
import time
import random
from streamlit_folium import st_folium

# Sayfa Ayarları
st.set_page_config(page_title="Arctic Culture", page_icon="🌍", layout="wide")

# -------------------------
# CSS 
# -------------------------
st.markdown(""" 
<style> 
   /* Ana Arka Plan - Açık koyu gri */ 
      .stApp { 
         background-color: #343a40; 
         color: #ffffff; 
    }

    /* SOL TARAF (SIDEBAR) BEYAZ */
    [data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 1px solid #e2e8f0;
    }

    /* Sidebar Marka Başlığı Stili */
.sidebar-brand-title {
    font-size: 1.5rem !important; /* Yazı boyutunu büyüttük */
    color: #000000 !important;    /* Tam siyah yaptık */
    font-weight: 800 !important;  /* Ekstra kalın yaptık */
    line-height: 1.2 !important;
    text-align: center;
    margin-top: 15px;
    margin-bottom: 20px;
    text-transform: uppercase;    /* Hepsini büyük harf yap */
    letter-spacing: 1px;          /* Harf arası boşluk ile modern görünüm */
}

    .card-icon { font-size: 3rem; margin-bottom: 15px; }
    
    /* Türk Bayrağı Özel İkon */
    .tr-flag-container {
        width: 60px;
        height: 40px;
        margin: 0 auto 15px auto; /* Ortalamak için */
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/b/b4/Flag_of_Turkey.svg');
        background-size: cover;
        background-position: center;
        border-radius: 4px;
        box-shadow: 0 4px 10px rgba(227, 10, 23, 0.4);
     }

    .card-title { color: #3498db; font-weight: bold; font-size: 1.1rem; margin-bottom: 10px; }
    .card-text { font-size: 0.85rem; opacity: 0.8; line-height: 1.4; }
    
    /* Sol Alt Açıklama Kutusu (Siyah, Büyük ve Görünür) */
    .sidebar-footer {
        font-size: 1.1rem !important;
        color: #000000 !important;
        font-weight: 600 !important;
        text-align: center;
        padding: 15px;
        background-color: #f1f5f9;
        border-radius: 12px;
        margin-top: 20px;
        border: 2px solid #000000;
        line-height: 1.5;
    }

    /* GÜNÜN BİLGİSİ KUTUSU (Belirgin Siyah) */
    .fact-box {
        background: #ffffff !important;
        border-radius: 15px;
        padding: 25px 35px;
        border-left: 10px solid #000000 !important;
        margin-top: 50px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }

    .fact-box h4 {
        color: #000000 !important;
        font-size: 1.6rem !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
    }

    .fact-box p {
        color: #1a1a1a !important;
        font-size: 1.2rem !important;
        line-height: 1.6;
    }

    /* Keşif Kartları */
    .explore-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        min-height: 220px;
        transition: transform 0.3s;
    }
    .explore-card:hover {
        transform: translateY(-10px);
        background: rgba(255, 255, 255, 0.1);
        border-color: #a5f3fc;
    }
</style>
""", unsafe_allow_html=True)
# -------------------------
# SIDEBAR İÇERİĞİ (SOL TARAF)
# -------------------------
with st.sidebar:
    # Kuzey Işıkları Videosu
    try:
        st.video("kuzeyısıkları.mp4")
    except:
        st.info("Video dosyası bekleniyor...")

    st.sidebar.markdown('<div class="sidebar-brand-title">DİJİTAL ARKTİK KÜLTÜR<br>EĞİTİM PLATFORMU</div>', unsafe_allow_html=True)
    
    menu = st.selectbox(
        "📍 Keşif Rotası Seçin",
        ["🏔️ Ana Sayfa", "🗺️ Kültürel Harita", "🛰️ NASA İklim Verisi", "🧭 Kültür Keşfi", "🇹🇷 Türkiye'nin Çalışmaları", "🎮 Görev Merkezi"]
    )

    st.markdown("---")
    
    # 4. Sol Alt Açıklama Metni (İstediğin Siyah ve Büyük Stil)
    st.markdown("""
        <div class="sidebar-footer">
            Bu platform; Kuzey Kutbu’nda yer alan Arktik Bölgesini tanıtmak ve bu bölgede yaşayan yerli halkların kültürlerine yönelik 
            öğrenci bilgi ve farkındalık düzeyini artırmak amacıyla geliştirilmiş, 
            dijital bir eğitim platformudur.
        </div>
    """, unsafe_allow_html=True)

# -------------------------
# SAĞ TARAF (ANA SAYFA) İÇERİĞİ
# -------------------------
if menu == "🏔️ Ana Sayfa":
    
    # Hero Bölümü
    st.markdown("""
        <div style="text-align: center; padding: 50px 0;">
            <h1 style="font-size: 3.5rem; font-weight: 800; color: white;">Arktik: Buzun ve İnsanın Hikayesi</h1>
            <p style="font-size: 1.2rem; opacity: 0.8;">Buzulların ötesine geçin, kadim kültürlerin yaşamına dokunun.</p>
        </div>
    """, unsafe_allow_html=True)
    # Tanıtım Cümlesi - Rengi beyaz (white) veya gümüş (silver) yaparak görünür kıldık
    st.markdown("""
        <div style="text-align: center; margin-bottom: 40px; color: #e2e8f0; font-size: 1.1rem; max-width: 900px; margin-left: auto; margin-right: auto; line-height: 1.6;">
            Bu platform, Kuzey Kutbu'nu sadece bir buz kütlesi olarak değil; yaşayan, nefes alan ve binlerce yıllık 
            insan mirasını barındıran bütüncül bir ekosistem olarak ele alır.
        </div>
    """, unsafe_allow_html=True)
    
    # 3. İNTERAKTİF KEŞİF KARTLARI
    # Not: Bu kartlar görsel simülasyondur, tıklama için sidebar kullanılır.
    st.markdown('<h3 style="text-align: center; margin-bottom: 30px;">Keşfe Nereden Başlayacaksınız?</h3>', unsafe_allow_html=True)
    
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
            <div class="explore-card">
                <div class="card-icon">🗺️</div>
                <div class="card-title">Kültürel Harita</div>
                <p style="font-size: 0.9rem;">Halkların izini sürün ve yaşam alanlarını keşfedin.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class="explore-card">
                <div class="card-icon">🛰️</div>
                <div class="card-title">NASA Verileri</div>
                <p style="font-size: 0.9rem;">Buzulların değişimini gerçek zamanlı takip edin.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
            <div class="explore-card">
                <div class="card-icon">🧭</div>
                <div class="card-title">Kültür Keşfi</div>
                <p style="font-size: 0.9rem;">Gelenekler, diller ve sanatın derinliklerine inin.</p>
            </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
            <div class="explore-card">
                <div class="tr-flag-container"></div>
                <div class="card-title">Türkiye'nin Rotası</div>
                <p style="font-size: 0.9rem;">Milli Kutup Araştırmaları ve Arktik seferlerimizi keşfedin.</p>
            </div>
        """, unsafe_allow_html=True)
        
         
    with col5:
        st.markdown("""
            <div class="explore-card">
                <div class="card-icon">🎮</div>
                <div class="card-title">Görev Merkezi</div>
                <p style="font-size: 0.9rem;">Arktik elçisi olun  ve  bilginizi test edin.</p>
            </div>
        """, unsafe_allow_html=True)

    
    # 4. GÜNÜN KELİMESİ (Sözlük Kutusu - Alt Kısımda Zarif Bir Detay Olarak)
    kelimeler = [
        {"kelime": "İglo", "dil": "İnuit Mühendisliği", "anlam": "Sıkıştırılmış kardan yapılan, dışarısı -40 derece olsa bile içindeki ısıyı koruyan efsanevi kubbe evler."},
        {"kelime": "Albedo", "dil": "İklim Bilimi", "anlam": "Buzulların güneş ışığını bir ayna gibi yansıtma gücü. Buzlar eridikçe dünya bu koruyucu aynasını kaybeder."},
        {"kelime": "Kutup Sumrusu", "dil": "Doğa Gezgini", "anlam": "Dünyanın en uzun yolculuğunu yapan kuş! Her yıl Kuzey ve Güney kutbu arasında uçarak ömrü boyunca Ay'a 3 kez gidip gelecek kadar yol kateder."},
        {"kelime": "Gakti", "dil": "Sami Kültürü", "anlam": "Sami halkının giydiği, nakışlarıyla kişinin memleketinden medeni durumuna kadar pek çok bilgi veren geleneksel kıyafet."},
        {"kelime": "Umiak", "dil": "İnuit Ulaşımı", "anlam": "Genellikle mors veya mühür derisinden yapılan, ailelerin ve eşyaların taşınmasında kullanılan geniş, açık Arktik teknesi."},
        {"kelime": "Permafrost", "dil": "Jeoloji", "anlam": "En az iki yıl boyunca kesintisiz olarak donmuş halde kalan toprak tabakası. Çözülmesi küresel iklim için büyük bir risk oluşturur."},
        {"kelime": "Nanuq", "dil": "İnuit Dili", "anlam": "Kutup ayısı anlamına gelir. İnuit inanışında 'buzun efendisi' olarak kabul edilen kutsal ve saygın bir varlıktır."},
        {"kelime": "Pemmikan", "dil": "Arktik Azığı", "anlam": "Kurutulmuş et, yağ ve bazen meyvelerin karıştırılmasıyla yapılan, bozulmadan yıllarca dayanabilen yüksek enerjili bir hayatta kalma yiyeceği."}
    ]
    
    gunun_kelimesi = random.choice(kelimeler)

    st.markdown(f"""
        <div style="background: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 15px; border-left: 5px solid #3498db; margin-top: 20px;">
            <b style="color: #3498db; font-size: 1.1rem;">❄️ Arktik Kaşif Notu: {gunun_kelimesi['kelime']}</b> 
            <span style="color: #a0a0a0; font-size: 0.9rem; margin-left: 5px;">({gunun_kelimesi['dil']})</span>
            <p style="margin-top: 10px; font-size: 1rem; line-height: 1.5;">{gunun_kelimesi['anlam']}</p>
        </div>
    """, unsafe_allow_html=True)
    
# -------------------------
# EĞLENCELİ KÜLTÜREL HARİTA
# -------------------------
elif menu == "🗺️ Kültürel Harita":
    
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
    
# ARKTİK KÜLTÜR PANELİ 
# -------------------------
st.markdown("---")
st.title("❄️ Arktik'e Yolculuk")

# 1. BÜTÜNSEL GÖRÜNÜM
with st.expander("🌐 Arktik Yaşamı ve Kültürü Storyboard Panosu", expanded=False):
   st.image("Arktik'e yolculuk.png", 
       width=700,   # <-- sabit genişlik
       caption="Arktik Kültür Sistemi - Birleşik Görünüm")
   st.info("💡 Aşağıdaki slaytlar üzerinden detayları inceleyin.")

# 2. ETKİLEŞİMLİ SLAYT SİSTEMİ
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0

    slides = [
        {"baslik": "ARKTİK ÇEVRE", "img": "1.png", },
        {"baslik": "BÖLGEDEKİ HAYVANLAR", "img": "2.png", },
        {"baslik": "YERLİ HALK", "img": "3.png", },
        {"baslik": "İGLO", "img": "4.png", },
        {"baslik": "KIYAFETLER", "img": "5.png",},
        {"baslik": "BULUŞLAR", "img": "6.png",},
    ]

    slide_data = slides[st.session_state.current_slide]

    # Başlık üstte daha şık durur
    st.subheader(f"📌 Slayt {st.session_state.current_slide + 1} / {len(slides)} – {slide_data['baslik']}")

    st.image(slide_data["img"],width=800)

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
    st.title("📈 NASA GISTEMP Küresel Sıcaklık Analizi")
    
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
# TÜRKİYE'NİN ÇALIŞMALARI
# -------------------------
elif menu == "🇹🇷 Türkiye'nin Çalışmaları":

    # --- SAYFA DÜZENİ VE BOŞLUK AYARLARI (CSS) ---
    st.markdown("""
        <style>
            /* 1. Sayfanın en üstünde ve en altında nefes alacak boşluk bırakır */
            .block-container {
                padding-top: 5rem !important;    /* Üst boşluk */
                padding-bottom: 5rem !important; /* Alt boşluk */
            }
            
            /* 2. Videoların altındaki boşluğu azaltır */
            .stVideo { margin-bottom: -20px !important; }
            
            /* 3. Ayırıcı çizgi (Divider) boşluğunu düzenler */
            hr { margin: 1.5em 0 !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- BAŞLIK ---
    st.title("🚢 Türkiye'nin Arktik Bilimsel Serüveni")

    # --- BÖLÜM 1: İLK ARKTİK SEFERİ ---
    st.header("1. Ulusal Arktik Bilim Seferi (2019)")
    st.image("ilk-arktik-sefer.jpg", caption="Türkiye'nin ilk Arktik seferinden bir kare.", use_container_width=True)
    st.video("https://youtu.be/Jsf8ggWzKAQ?si=r4Uazv532UJ-7qKl")

    st.divider()

    # --- BÖLÜM 2: 5. ARKTİK SEFERİ (Video Solda, Yazı Sağda) ---
    st.header("📅 5. Arktik Seferi (2025)")
    
    col1, col2 = st.columns([1.6, 2], gap="medium") 
    
    with col1:
        # İstediğin gibi video burada
        st.video("https://youtu.be/Hd88m7qvMMY")
        st.caption("📽️ 5. Arktik Seferi Özeti")
        
        # Veriler videonun hemen altında, boşluksuz
        v_col1, v_col2 = st.columns(2)
        v_col1.metric(label="Mesafe", value="3.000 Mil")
        v_col2.metric(label="Proje Sayısı", value="19 Proje")

    with col2:
        # Net ve Beyaz Yazılı Bilgi Kutusu
        st.markdown("""
            <div style="background-color: #003366; padding: 18px; border-radius: 10px; border-left: 5px solid #00aeef;">
                <p style="color: white; margin: 0; font-size: 15px; line-height: 1.5;">
                <strong>Son Gelişme:</strong> Türkiye, 2025 yılında gerçekleştirilen 5. sefer ile Svalbard Takımadaları çevresinde 
                kapsamlı araştırmalar yaptı. Bu seferde ilk kez lise öğrencileri projelerini test ettiler.
                </p>
            </div>
            """, unsafe_allow_html=True)
        st.write("") # Buton için minik bir boşluk
        st.link_button("Haberin Detaylarını Oku (AA)", "https://www.aa.com.tr/tr/ekonomi/turkiyenin-kuzey-kutbundaki-bilimsel-ayak-izi-5-arktik-seferi/3650001")

    # Yeşil Bilgi Bandı
    st.success("💡 Arktik bölgesi, dünyanın geri kalanından tam 4 kat daha hızlı ısınıyor!")
    
    st.divider()

    # --- BÖLÜM 3: UZMAN GÖRÜŞÜ ---
    st.header("🎙️ Uzman Görüşü: Burcu Özsoy")
    st.subheader("Kutup Bölgeleri Bize Ne Anlatıyor?")
    st.video("https://youtu.be/8DczVgr03BQ?si=WKx_5YMTtlR6Am_m")

    # Burcu Özsoy Bilgi Kutusu
    st.markdown("""
        <div style="background-color: #003366; padding: 18px; border-radius: 10px; border-left: 5px solid #00aeef;">
            <p style="color: white; margin: 0; font-size: 15px; line-height: 1.5;">
            <strong>Prof. Dr. Burcu Özsoy Kimdir?</strong> TÜBİTAK MAM Kutup Araştırmaları Enstitüsü kurucu müdürüdür. 
            Türkiye'nin kutup bilim seferlerinin koordinatörlüğünü yaparak bu alanda ülkemize öncülük etmektedir.
            </p>
        </div>
        """, unsafe_allow_html=True)
# -------------------------
# 5. SAYFA: OYUN SAYFASI (Test Alanı)
# -------------------------
elif menu == "🎮 Görev Merkezi":
    st.title("🎯 Arctic Bilgi Görevleri")
    
    # OKUNURLUK İÇİN ÖZEL CSS
    st.markdown("""
        <style>
        .stMarkdown p { color: white !important; font-size: 1.2rem !important; font-weight: 600 !important; }
        div[data-testid="stRadio"] label p { 
            color: #FFFFFF !important; 
            font-size: 1.1rem !important; 
            font-weight: bold !important;
            text-shadow: 1px 1px 2px black; 
        }
        .glass-card p { color: white !important; }
        h1, h2, h3 { color: #00aeef !important; }
        </style>
    """, unsafe_allow_html=True)

    st.write("⚠️ **Dikkat:** Her soru için tek hakkın var! Yanlış cevap puan kazandırmaz.")

    # Puan ve Takip Sistemi
    if "puan" not in st.session_state: st.session_state.puan = 0
    if "cevaplananlar" not in st.session_state: st.session_state.cevaplananlar = {}

    # Sidebar Skor ve Sıfırlama
    st.sidebar.metric("🏆 Toplam Skor", st.session_state.puan)
    if st.sidebar.button("🔄 Testi Sıfırla (Baştan Başla)"):
        st.session_state.puan = 0
        st.session_state.cevaplananlar = {}
        st.rerun()

    # --- 1. SORU: İGLOO ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_igloo" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_igloo"] == "Doğru":
            st.success("✅ TEBRİKLER! İgloo bilgisini doğru bildin. (+10 Puan)")
        else:
            st.error("❌ HATALI! (Doğru Cevap: İgloo)")
    else:
        q_ig = st.radio("🏠 Inuit halkının kar bloklarıyla inşa ettiği barınaklara ne denir?", 
                       ["Yurt", "İgloo", "Hogan"], key="r_igloo")
        if st.button("Cevabı Onayla", key="b_igloo"):
            if q_ig == "İgloo":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_igloo"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_igloo"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 2. SORU: SAMI ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_sami" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_sami"] == "Doğru":
            st.success("✅ HARİKA! Joik sanatını doğru bildin. (+10 Puan)")
        else:
            st.error("❌ HATALI! (Doğru Cevap: Joik)")
    else:
        q_sa = st.radio("❄️ Sami halkının kadim vokal sanatına ne denir?", 
                       ["Kanto", "Joik", "Haka"], key="r_sami")
        if st.button("Cevabı Onayla", key="b_sami"):
            if q_sa == "Joik":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_sami"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_sami"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    # --- 3. SORU: NENETS ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_nenets" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_nenets"] == "Doğru":
            st.success("✅ TEBRİKLER! Ren geyiği bilgisini doğru bildin. (+10 Puan)")
        else:
            st.error("❌ HATALI! (Doğru Cevap: Ren Geyiği)")
    else:
        q_ne = st.radio("🦌 Nenets halkı hangi hayvanın sürülerine rehberlik eder?", 
                       ["Misk Öküzü", "Ren Geyiği", "Kutup Ayısı"], key="r_nenets")
        if st.button("Cevabı Onayla", key="b_nenets"):
            if q_ne == "Ren Geyiği":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_nenets"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_nenets"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
   

    # --- 4. SORU: KIZAK ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_kizak" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_kizak"] == "Doğru":
            st.success("✅ DOĞRU! Köpekli kızak doğru cevap. (+10 Puan)")
        else:
            st.error("❌ YANLIŞ! (Doğru Cevap: Köpekli Kızak)")
    else:
        q_ki = st.radio("🐕 Inuitlerin geleneksel kış ulaşımında en çok güvendiği araç hangisidir?", 
                       ["Kar Motoru", "Köpekli Kızak", "At Arabası"], key="r_kizak")
        if st.button("Cevabı Onayla", key="b_kizak"):
            if q_ki == "Köpekli Kızak":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_kizak"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_kizak"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


    # --- 5. SORU: KAYAK ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_kayak" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_kayak"] == "Doğru":
            st.success("✅ TEBRİKLER! Kayak doğru cevap. (+10 Puan)")
        else:
            st.error("❌ HATALI! (Doğru Cevap: Kayak)")
    else:
        q_ka = st.radio("🛶 Inuitlerin denizde fok veya balina avlamak için kullandığı tek kişilik deri kaplı kanoya ne denir?", 
                       ["Kayak", "Kano", "Gondol"], key="r_kayak")
        if st.button("Cevabı Onayla", key="b_kayak"):
            if q_ka == "Kayak":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_kayak"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_kayak"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


    # --- 6. SORU: AURORA ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_aurora" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_aurora"] == "Doğru":
            st.success("✨ MÜKEMMEL! Aurora bilgisini doğru bildin. (+10 Puan)")
        else:
            st.error("❌ HATALI! (Doğru Cevap: Aurora)")
    else:
        q_au = st.radio("✨ Kuzey gökyüzünde görülen renkli ışık dansına ne ad verilir?", 
                       ["Aurora Borealis", "Gökkuşağı", "Meteor Yağmuru"], key="r_aurora")
        if st.button("Cevabı Onayla", key="b_aurora"):
            if q_au == "Aurora Borealis":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_aurora"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_aurora"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)


    # --- 7. SORU: KAR GÖZLÜĞÜ ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_gozluk" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_gozluk"] == "Doğru":
            st.success("🕶️ HARİKA! Inuitler doğru cevap. (+10 Puan)")
        else:
            st.error("❌ HATALI! (Doğru Cevap: Inuitler)")
    else:
        q_go = st.radio("🕶️ Kar körlüğünü engellemek için dünyanın ilk güneş gözlüklerini kimler icat etmiştir?", 
                       ["Vikingler", "Inuitler", "Moğollar"], key="r_gozluk")
        if st.button("Cevabı Onayla", key="b_gozluk"):
            if q_go == "Inuitler":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_gozluk"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_gozluk"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
    # --- 8. SORU: BURCU ÖZSOY ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_burcu" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_burcu"] == "Doğru":
            st.success("✅ TEBRİKLER! Burcu Özsoy bilgisini doğru bildin. (+10 Puan)")
        else:
            st.error("❌ HATALI! (Doğru Cevap: Burcu Özsoy)")
    else:
        q1 = st.radio("👩‍🔬 Türkiye'nin kutup çalışmalarına öncülük eden bilim insanımız kimdir?", 
                     ["Canan Dağdeviren", "Burcu Özsoy", "Aziz Sancar"], key="r1")
        if st.button("Cevabı Onayla", key="b1"):
            if q1 == "Burcu Özsoy":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_burcu"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_burcu"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 9. SORU: SEFER SAYISI ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_sefer" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_sefer"] == "Doğru":
            st.success("✅ HARİKA! 5. sefer bilgisini doğru bildin. (+10 Puan)")
        else:
            st.error("❌ YANLIŞ! 2025 itibarıyla 5 sefer düzenlenmiştir.")
    else:
        q2 = st.radio("🚢 Türkiye, 2025 yılına kadar Arktik bölgesine toplam kaç bilimsel sefer düzenlemiştir?", 
                     ["3 Sefer", "5 Sefer", "10 Sefer"], key="r2")
        if st.button("Cevabı Onayla", key="b2"):
            if q2 == "5 Sefer":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_sefer"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_sefer"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 10. SORU: İKLİM HIZI ---
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    if "q_hiz" in st.session_state.cevaplananlar:
        if st.session_state.cevaplananlar["q_hiz"] == "Doğru":
            st.success("✅ DOĞRU! Arktik çok daha hızlı ısınıyor. (+10 Puan)")
        else:
            st.error("❌ MAALESEF YANLIŞ! Arktik dünyadan 4 kat daha hızlı ısınmaktadır.")
    else:
        q3 = st.radio("🌡️ Arktik bölgesi, dünyanın geri kalanına göre ne kadar daha hızlı ısınmaktadır?", 
                     ["2 Kat", "4 Kat", "10 Kat"], key="r3")
        if st.button("Cevabı Onayla", key="b3"):
            if q3 == "4 Kat":
                st.session_state.puan += 10
                st.session_state.cevaplananlar["q_hiz"] = "Doğru"
            else:
                st.session_state.cevaplananlar["q_hiz"] = "Yanlış"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
        # Final Durumu
    if len(st.session_state.cevaplananlar) == 10:
        st.balloons()
        st.success("🏆 TÜM GÖREVLER TAMAMLANDI!")
        st.markdown(f"## 🎖️ Toplam Puanın: {st.session_state.puan}")
        st.info("❄️ Artık resmi olarak bir **ARCTIC MASTER – Kutup Kaşifi** oldun!")
