import streamlit as st
import pandas as pd
import plotly.express as px
import pydeck as pdk

import streamlit as st

st.set_page_config(page_title="Arctic Voices Digital", page_icon="🌍", layout="wide")

# -------------------------
# GLASSMORPHISM CSS
# -------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}

.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 20px;
    padding: 25px;
    margin: 20px 0px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    transition: 0.3s;
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
}

.card-title {
    font-size: 28px;
    font-weight: bold;
    color: white;
}

.card-text {
    font-size: 16px;
    color: #e0e0e0;
}

img {
    border-radius: 15px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------

st.markdown("<h1 style='color:white;'>🌍 Arctic Voices Digital</h1>", unsafe_allow_html=True)
st.write(" ")

# ------------------ CARD GRID ------------------

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">Inuit</div>
        <div class="card-text">
        Kanada, Alaska ve Grönland bölgesinde yaşayan Arktik yerli halkıdır.
        Deniz buzuna dayalı avcılık kültürü ve dayanıklı yaşam biçimi ile bilinir.
        </div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/5/5a/Inuit_family_1906.jpg" width="100%">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="glass-card">
        <div class="card-title">Sami</div>
        <div class="card-text">
        İskandinavya'nın kuzeyinde yaşayan yerli topluluktur.
        Ren geyiği yetiştiriciliği ve geleneksel joik müziği ile tanınır.
        </div>
        <img src="https://upload.wikimedia.org/wikipedia/commons/3/3a/Sami_people_1900.jpg" width="100%">
    </div>
    """, unsafe_allow_html=True)

