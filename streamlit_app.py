import streamlit as st
import numpy as np
import pandas as pd

# Mengatur tema Streamlit dengan dominasi warna ungu sangat gelap
st.set_page_config(
    page_title="Perhitungan Efisiensi IPAL",
    page_icon=" ",
    layout="centered",
    initial_sidebar_state="auto"
)

# Tambahkan CSS untuk latar belakang gambar dan teks hitam, termasuk header
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
    background: rgba(255, 255, 255, 0.2); /* Transparan dengan efek blur */
    backdrop-filter: blur(5px); /* Efek blur */
}

[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
[data-testid="stSidebar"] p, [data-testid="stSidebar"] li {
    color: white; /* Set warna font sidebar menjadi putih */
}

.stMarkdown {
    color: white; /* Set warna teks markdown menjadi putih */
}

.stNumberInput div {
    color: white; /* Mengubah warna teks input menjadi putih */
}

h2 {
    color: white; /* Set warna h2 menjadi putih */
    border-bottom: 4px solid white; /* Ubah garis bawah menjadi putih */
}

.output {
    color: yellow; /* Set warna output menjadi kuning */
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Judul aplikasi
st.title("Perhitungan Efisiensi IPAL")

# Opsi di sidebar
opsi = st.sidebar.selectbox("Pilih opsi:", ["Tentang Kami", "Perhitungan Efisiensi IPAL"])

# Konten opsi pertama
if opsi == "Tentang Kami":
    st.write("### Tentang Kami:")
    st.write("Aplikasi ini digunakan untuk menghitung efisiensi Instalasi Pengolahan Air Limbah (IPAL).")
    st.write("Aplikasi ini merupakan hasil dari projek yang bertujuan untuk membantu memahami konsep dan proses dalam pengolahan air limbah.")

# Konten opsi kedua
if opsi == "Perhitungan Efisiensi IPAL":
    st.write("### Perhitungan Efisiensi IPAL")
    
    # Input data
    volume_input = st.number_input("Masukkan volume air limbah yang masuk (m³):", min_value=0.0, value=10.0)
    volume_output = st.number_input("Masukkan volume air yang keluar (m³):", min_value=0.0, value=8.0)

    if st.button("Hitung Efisiensi"):
        if volume_input > 0:
            # Menghitung efisiensi
            efisiensi = ((volume_input - volume_output) / volume_input) * 100
            st.write(f"### Efisiensi IPAL: {efisiensi:.2f}%")
        else:
            st.error("Volume air limbah masuk harus lebih besar dari 0.")
