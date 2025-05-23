import streamlit as st  
import numpy as np  
import pandas as pd  
  
st.set_page_config(page_title="Perhitungan Efisiensi IPAL", layout="centered")  
  
# Background dan CSS terang
st.markdown("""  
<style>  
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1693237476029-f8469bb756a2?q=80&w=1932&auto=format&fit=crop");  
    background-size: cover;  
    background-position: center;  
    color: white;
}
[data-testid="stSidebar"] {
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(6px);
    color: white;
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] label {
    color: white;
    font-weight: bold;
}
.stNumberInput input {
    color: black;
    background-color: white;
    font-weight: bold;
}
h2, h3, h4, p, label, .stMarkdown {
    color: white !important;
}
.stButton>button {
    color: black;
    background-color: #00ffff;
    font-weight: bold;
}
</style>  
""", unsafe_allow_html=True)  
  
# Sidebar menu  
st.sidebar.title('Menu')  
menu = st.sidebar.radio('Pilih Menu', ['Beranda', 'Penjelasan IPAL', 'Perhitungan Efisiensi'])  
  
def bold_black_header(text):  
    st.markdown(f"<h2 style='border-bottom: 4px solid white;'>{text}</h2>", unsafe_allow_html=True)  
  
if menu == 'Beranda':  
    bold_black_header('Selamat Datang di Kalkulator IPAL')  
    st.write("""  
Aplikasi ini membantu Anda menghitung efisiensi IPAL dan membandingkannya dengan baku mutu limbah berdasarkan PermenLHK No. 5 Tahun 2022.  
  
Dibuat oleh:  
2F/PLI/2025  
""")  
  
elif menu == 'Penjelasan IPAL':  
    bold_black_header("📚 Apa itu IPAL?")  
    st.write("""  
IPAL (Instalasi Pengolahan Air Limbah) adalah sistem yang digunakan untuk mengolah air limbah agar dapat memenuhi standar baku mutu yang ditetapkan sebelum dibuang ke lingkungan. Tujuan utama dari IPAL adalah mengurangi polutan dalam air, seperti BOD, COD, TSS, dan pH.  
  
Berikut penjelasan singkat:  
- **BOD (Biological Oxygen Demand)**: Mengukur jumlah oksigen yang dibutuhkan oleh mikroorganisme untuk mengurai bahan organik dalam air.  
- **COD (Chemical Oxygen Demand)**: Mengukur jumlah oksigen yang dibutuhkan untuk mengoksidasi bahan kimia organik dan anorganik.  
- **TSS (Total Suspended Solid)**: Padatan tersuspensi yang dapat menyebabkan kekeruhan air.  
- **pH**: Tingkat keasaman atau kebasaan air limbah.  
""")  
  
elif menu == 'Perhitungan Efisiensi':  
    bold_black_header("🛠️ Kalkulator Parameter IPAL")  
    kalkulator = st.sidebar.radio("Pilih Kalkulator", ['Kalkulator BOD', 'Kalkulator COD', 'Kalkulator TSS', 'Kalkulator pH'])  
  
    def baku_mutu_check(nama, nilai, ambang, satuan="mg/L"):  
        if nilai <= ambang:  
            st.success(f"{nama} ({nilai} {satuan}) **MEMENUHI** baku mutu ({nama} ≤ {ambang} {satuan})")  
        else:  
            st.error(f"{nama} ({nilai} {satuan}) **TIDAK MEMENUHI** baku mutu ({nama} ≤ {ambang} {satuan})")  
  
    if kalkulator == 'Kalkulator BOD':  
        bod_in = st.number_input("BOD inlet (mg/L)", min_value=0.0, step=0.1)  
        bod_out = st.number_input("BOD outlet (mg/L)", min_value=0.0, step=0.1)  
        if st.button("Hitung Efisiensi BOD"):  
            if bod_in <= 0:  
                st.error("Inlet BOD harus lebih dari 0.")  
            elif bod_out > bod_in:  
                st.error("Outlet tidak boleh lebih besar dari inlet.")  
            else:  
                e = ((bod_in - bod_out) / bod_in) * 100  
                st.success(f"Efisiensi BOD: {e:.2f}%")  
                baku_mutu_check("BOD Outlet", bod_out, 30)  
  
    elif kalkulator == 'Kalkulator COD':  
        cod_in = st.number_input("COD inlet (mg/L)", min_value=0.0, step=0.1)  
        cod_out = st.number_input("COD outlet (mg/L)", min_value=0.0, step=0.1)  
        if st.button("Hitung Efisiensi COD"):  
            if cod_in <= 0:  
                st.error("Inlet COD harus lebih dari 0.")  
            elif cod_out > cod_in:  
                st.error("Outlet tidak boleh lebih besar dari inlet.")  
            else:  
                e = ((cod_in - cod_out) / cod_in) * 100  
                st.success(f"Efisiensi COD: {e:.2f}%")  
                baku_mutu_check("COD Outlet", cod_out, 100)  
  
    elif kalkulator == 'Kalkulator TSS':  
        tss_in = st.number_input("TSS inlet (mg/L)", min_value=0.0, step=0.1)  
        tss_out = st.number_input("TSS outlet (mg/L)", min_value=0.0, step=0.1)  
        if st.button("Hitung Efisiensi TSS"):  
            if tss_in <= 0:  
                st.error("Inlet TSS harus lebih dari 0.")  
            elif tss_out > tss_in:  
                st.error("Outlet tidak boleh lebih besar dari inlet.")  
            else:  
                e = ((tss_in - tss_out) / tss_in) * 100  
                st.success(f"Efisiensi TSS: {e:.2f}%")  
                baku_mutu_check("TSS Outlet", tss_out, 30)  
  
    elif kalkulator == 'Kalkulator pH':  
        ph_in = st.number_input("pH inlet", min_value=0.0, max_value=14.0, step=0.1)  
        ph_out = st.number_input("pH outlet", min_value=0.0, max_value=14.0, step=0.1)  
        if st.button("Evaluasi pH"):  
            if 6.5 <= ph_out <= 8.5:  
                st.success(f"pH outlet ({ph_out}) **MEMENUHI** baku mutu (6.5–8.5)")  
            else:  
                st.error(f"pH outlet ({ph_out}) **TIDAK MEMENUHI** baku mutu (6.5–8.5)")
