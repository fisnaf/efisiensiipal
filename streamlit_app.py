import streamlit as st
import numpy as np
import pandas as pd

# Konfigurasi halaman
st.set_page_config(
    page_title="Perhitungan Efisiensi IPAL",
    page_icon=" ",
    layout="centered",
    initial_sidebar_state="auto"
)

# CSS: background gelap + teks cerah agar kontras
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1693237476029-f8469bb756a2?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHxhfA%3D%3D");
    background-size: cover;
    background-position: center;
}

[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(6px);
    color: #fff;
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p, [data-testid="stSidebar"] li, label, .stSelectbox label {
    color: #f0f8ff !important;
    font-weight: bold;
}

.stMarkdown, .stNumberInput label, .stNumberInput input {
    color: #ffffff !important;
}

h1, h2, h3 {
    color: #00ffff !important;
    text-shadow: 1px 1px 2px #000;
}

.stButton>button {
    color: #000;
    background-color: #00ffff;
    font-weight: bold;
}

.output {
    color: yellow;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Judul
st.title("Perhitungan Efisiensi IPAL")

# Sidebar menu
opsi = st.sidebar.selectbox("Pilih Menu", ["Tentang Kami", "Perhitungan Efisiensi IPAL"])

if opsi == "Tentang Kami":
    st.subheader("Tentang Kami")
    st.write("Aplikasi ini digunakan untuk menghitung efisiensi Instalasi Pengolahan Air Limbah (IPAL).")
    st.write("Aplikasi ini merupakan hasil dari projek edukatif untuk memahami proses pengolahan air limbah secara interaktif.")

elif opsi == "Perhitungan Efisiensi IPAL":
    st.subheader("Formulir Perhitungan Efisiensi")

    volume_input = st.number_input("Masukkan volume air limbah yang masuk (m³):", min_value=0.0, value=10.0)
    volume_output = st.number_input("Masukkan volume air yang keluar (m³):", min_value=0.0, value=8.0)

    if st.button("Hitung Efisiensi"):
        if volume_input > 0:
            efisiensi = ((volume_input - volume_output) / volume_input) * 100
            st.success(f"Efisiensi IPAL: {efisiensi:.2f}%")
        else:
            st.error("Volume air limbah masuk harus lebih besar dari 0.")
