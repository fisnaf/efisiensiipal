import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Perhitungan Efisiensi IPAL", layout="centered")

# Background CSS dan styling teks terang
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

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] label {
    color: white;
    font-weight: bold;
}

.stNumberInput input {
    color: black;
    background-color: white;
    font-weight: bold;
}

h2 {
    color: #00ffff;
    text-shadow: 1px 1px 2px black;
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

# Fungsi header tebal hitam

def bold_black_header(text):
    st.markdown(f"<h2 style='border-bottom: 4px solid black; color: white;'>{text}</h2>", unsafe_allow_html=True)

# Baku mutu berdasarkan Permen LHK No. 5 Tahun 2022 (untuk industri tekstil sebagai contoh)
BAKU_MUTU = {
    "BOD": 30,
    "COD": 100,
    "TSS": 30,
    "pH_min": 6.5,
    "pH_max": 8.5
}

if menu == 'Beranda':
    bold_black_header('Selamat Datang di Kalkulator IPAL')
    st.write("""
Aplikasi ini membantu Anda menghitung efisiensi IPAL dan membandingkannya dengan baku mutu limbah berdasarkan **Permen LHK No. 5 Tahun 2022**.

Dibuat oleh:
- 2F/PLI/2025
""")

elif menu == 'Penjelasan IPAL':
    bold_black_header("📚 Apa itu IPAL?")
    st.write("IPAL adalah Instalasi Pengolahan Air Limbah untuk menurunkan kandungan polutan seperti BOD, COD, TSS, dan pH dalam air limbah sebelum dibuang ke lingkungan.")
    st.write("Baku mutu limbah cair domestik berdasarkan PermenLHK No. 5 Tahun 2022 (contoh):")
    st.markdown(f"""
- BOD ≤ {BAKU_MUTU['BOD']} mg/L
- COD ≤ {BAKU_MUTU['COD']} mg/L
- TSS ≤ {BAKU_MUTU['TSS']} mg/L
- pH antara {BAKU_MUTU['pH_min']}–{BAKU_MUTU['pH_max']}
""")
    st.latex(r'''Efisiensi = \frac{C_{inlet} - C_{outlet}}{C_{inlet}} \times 100''')

elif menu == 'Perhitungan Efisiensi':
    bold_black_header("🛠️ Kalkulator Efisiensi IPAL")
    kalkulator = st.sidebar.radio("Pilih Kalkulator", ['Efisiensi IPAL', 'Kalkulator BOD', 'Kalkulator COD', 'Kalkulator TSS', 'Kalkulator pH'])

    def baku_mutu_check(nama, nilai, ambang, satuan="mg/L"):
        if nilai <= ambang:
            st.info(f"{nama} ({nilai} {satuan}) **MEMENUHI** baku mutu (≤ {ambang} {satuan}) sesuai PermenLHK No. 5 Tahun 2022")
        else:
            st.error(f"{nama} ({nilai} {satuan}) **TIDAK MEMENUHI** baku mutu (≤ {ambang} {satuan}) sesuai PermenLHK No. 5 Tahun 2022")

    if kalkulator == 'Efisiensi IPAL':
        c_inlet = st.number_input("Konsentrasi inlet (mg/L)", min_value=0.0, step=0.1)
        c_outlet = st.number_input("Konsentrasi outlet (mg/L)", min_value=0.0, step=0.1)
        if st.button("Hitung Efisiensi IPAL"):
            if c_inlet <= 0:
                st.error("Inlet harus lebih dari 0.")
            elif c_outlet > c_inlet:
                st.error("Outlet tidak boleh lebih besar dari inlet.")
            else:
                efisiensi = ((c_inlet - c_outlet) / c_inlet) * 100
                st.success(f"Efisiensi: {efisiensi:.2f}%")
                baku_mutu_check("Outlet", c_outlet, 30)

    elif kalkulator == 'Kalkulator BOD':
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
                baku_mutu_check("BOD Outlet", bod_out, BAKU_MUTU['BOD'])

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
                baku_mutu_check("COD Outlet", cod_out, BAKU_MUTU['COD'])

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
                baku_mutu_check("TSS Outlet", tss_out, BAKU_MUTU['TSS'])

    elif kalkulator == 'Kalkulator pH':
        ph_in = st.number_input("pH inlet", min_value=0.0, max_value=14.0, step=0.1)
        ph_out = st.number_input("pH outlet", min_value=0.0, max_value=14.0, step=0.1)
        if st.button("Evaluasi pH"):
            if BAKU_MUTU['pH_min'] <= ph_out <= BAKU_MUTU['pH_max']:
                st.success(f"pH outlet ({ph_out}) dalam baku mutu ({BAKU_MUTU['pH_min']}–{BAKU_MUTU['pH_max']}) sesuai PermenLHK No. 5 Tahun 2022")
            else:
                st.error(f"pH outlet ({ph_out}) di luar baku mutu ({BAKU_MUTU['pH_min']}–{BAKU_MUTU['pH_max']}) sesuai PermenLHK No. 5 Tahun 2022")
