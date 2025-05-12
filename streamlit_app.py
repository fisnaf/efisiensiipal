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

# CSS: latar belakang + perbaikan teks sidebar & input
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
    color: #f8f9fa !important;
    font-weight: bold;
}

.stMarkdown, .stNumberInput label {
    color: #ffffff !important;
}

.stNumberInput input {
    color: black !important;
    background-color: #ffffff !important;
    font-weight: bold;
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
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title('Menu')
menu = st.sidebar.radio('Pilih Menu', ['Beranda', 'Penjelasan IPAL', 'Perhitungan Efisiensi'])

# Fungsi header khusus
def bold_black_header(text):
    st.markdown(f"<h2 style='border-bottom: 4px solid black; color: black;'>{text}</h2>", unsafe_allow_html=True)

# Menu: Beranda
if menu == 'Beranda':
    bold_black_header('Selamat Datang di Kalkulator IPAL')
    st.write("""
Aplikasi ini membantu Anda memahami konsep Instalasi Pengolahan Air Limbah (IPAL) dan menghitung efisiensi pengolahannya.

Dibuat oleh:
- Syarif Nafis & Tim (2025)

Silakan gunakan menu di sebelah kiri untuk mulai mengeksplorasi.
""")

# Menu: Penjelasan IPAL
elif menu == 'Penjelasan IPAL':
    bold_black_header("📚 Pendahuluan")
    st.write("""
Instalasi Pengolahan Air Limbah (IPAL) adalah sistem yang dirancang untuk mengolah air limbah agar aman dibuang ke lingkungan atau digunakan kembali. IPAL penting untuk menjaga kualitas air dan kesehatan lingkungan.

Efisiensi IPAL mengukur seberapa besar kemampuan instalasi dalam menurunkan polutan dari air limbah.
""")

    bold_black_header("🔎 Inlet dan Outlet")
    st.write("""
- **Inlet**: Titik masuk air limbah, biasanya konsentrasi polutan tinggi.
- **Outlet**: Titik keluarnya air setelah diolah, seharusnya konsentrasi lebih rendah.

Perbandingan antara inlet dan outlet digunakan untuk menghitung efisiensi.
""")

    bold_black_header("🧮 Rumus Perhitungan")
    st.latex(r'''
    \text{Efisiensi (\%)} = \frac{C_{\text{inlet}} - C_{\text{outlet}}}{C_{\text{inlet}}} \times 100
    ''')
    st.markdown("""
- C_{\text{inlet}}: Konsentrasi polutan inlet (mg/L)  
- C_{\text{outlet}}: Konsentrasi polutan outlet (mg/L)
""")

    bold_black_header("📊 Parameter Evaluasi")
    st.write("""
- **BOD**: Permintaan oksigen oleh mikroorganisme.
- **COD**: Permintaan oksigen total untuk oksidasi.
- **pH**: Tingkat keasaman/basaan.
- **TSS**: Jumlah padatan tersuspensi.

Evaluasi ini berguna untuk:
- Memastikan kepatuhan regulasi.
- Menilai efektivitas proses.
- Menyusun strategi peningkatan efisiensi.
""")

# Menu: Perhitungan Efisiensi
elif menu == 'Perhitungan Efisiensi':
    bold_black_header("🛠️ Hitung Efisiensi IPAL Anda")

    # Sidebar untuk memilih kalkulator parameter
    kalkulator = st.sidebar.radio("Pilih Kalkulator", ['Efisiensi IPAL', 'Kalkulator BOD', 'Kalkulator COD', 'Kalkulator TSS', 'Kalkulator pH'])
    
    if kalkulator == 'Efisiensi IPAL':
        # Perhitungan efisiensi IPAL
        c_inlet = st.number_input("Masukkan konsentrasi polutan inlet (mg/L)", min_value=0.0, step=0.1)
        c_outlet = st.number_input("Masukkan konsentrasi polutan outlet (mg/L)", min_value=0.0, step=0.1)

        if st.button("Hitung Efisiensi"):
            if c_inlet <= 0:
                st.error("Konsentrasi inlet harus lebih dari 0.")
            elif c_outlet > c_inlet:
                st.error("Konsentrasi outlet tidak boleh lebih besar dari inlet.")
            else:
                efisiensi = ((c_inlet - c_outlet) / c_inlet) * 100
                st.success(f"Efisiensi IPAL adalah {efisiensi:.2f}%")
                if efisiensi >= 90:
                    st.balloons()
                    st.info("Kinerja IPAL: Sangat Baik ✅")
                elif efisiensi >= 70:
                    st.info("Kinerja IPAL: Cukup Baik ✅")
                else:
                    st.warning("Kinerja IPAL: Perlu Ditingkatkan ⚠️")

    elif kalkulator == 'Kalkulator BOD':
        # Kalkulator BOD
        bod_inlet = st.number_input("Masukkan konsentrasi BOD di inlet (mg/L)", min_value=0.0, step=0.1)
        bod_outlet = st.number_input("Masukkan konsentrasi BOD di outlet (mg/L)", min_value=0.0, step=0.1)

        if st.button("Hitung Efisiensi BOD"):
            if bod_inlet <= 0:
                st.error("Konsentrasi BOD inlet harus lebih dari 0.")
            elif bod_outlet > bod_inlet:
                st.error("Konsentrasi BOD outlet tidak boleh lebih besar dari inlet.")
            else:
                bod_efisiensi = ((bod_inlet - bod_outlet) / bod_inlet) * 100
                st.success(f"Efisiensi pengurangan BOD adalah {bod_efisiensi:.2f}%")
                if bod_efisiensi >= 90:
                    st.balloons()
                    st.info("Kinerja BOD: Sangat Baik ✅")
                elif bod_efisiensi >= 70:
                    st.info("Kinerja BOD: Cukup Baik ✅")
                else:
                    st.warning("Kinerja BOD: Perlu Ditingkatkan ⚠️")

    elif kalkulator == 'Kalkulator COD':
        # Kalkulator COD
        cod_inlet = st.number_input("Masukkan konsentrasi COD di inlet (mg/L)", min_value=0.0, step=0.1)
        cod_outlet = st.number_input("Masukkan konsentrasi COD di outlet (mg/L)", min_value=0.0, step=0.1)

        if st.button("Hitung Efisiensi COD"):
            if cod_inlet <= 0:
                st.error("Konsentrasi COD inlet harus lebih dari 0.")
            elif cod_outlet > cod_inlet:
                st.error("Konsentrasi COD outlet tidak boleh lebih besar dari inlet.")
            else:
                cod_efisiensi = ((cod_inlet - cod_outlet) / cod_inlet) * 100
                st.success(f"Efisiensi pengurangan COD adalah {cod_efisiensi:.2f}%")
                if cod_efisiensi >= 90:
                    st.balloons()
                    st.info("Kinerja COD: Sangat Baik ✅")
                elif cod_efisiensi >= 70:
                    st.info("Kinerja COD: Cukup Baik ✅")
                else:
                    st.warning("Kinerja COD: Perlu Ditingkatkan ⚠️")

    elif kalkulator == 'Kalkulator TSS':
        # Kalkulator TSS
        tss_inlet = st.number_input("Masukkan konsentrasi TSS di inlet (mg/L)", min_value=0.0, step=0.1)
        tss_outlet = st.number_input("Masukkan konsentrasi TSS di outlet (mg/L)", min_value=0.0, step=0.1)

        if st.button("Hitung Efisiensi TSS"):
            if tss_inlet <= 0:
                st.error("Konsentrasi TSS inlet harus lebih dari 0.")
            elif tss_outlet > tss_inlet:
                st.error("Konsentrasi TSS outlet tidak boleh lebih besar dari inlet.")
            else:
                tss_efisiensi = ((tss_inlet - tss_outlet) / tss_inlet) * 100
                st.success(f"Efisiensi pengurangan TSS adalah {tss_efisiensi:.2f}%")
                if tss_efisiensi >= 90:
                    st.balloons()
                    st.info("Kinerja TSS: Sangat Baik ✅")
                elif tss_efisiensi >= 70:
                    st.info("Kinerja TSS: Cukup Baik ✅")
                else:
                    st.warning("Kinerja TSS: Perlu Ditingkatkan ⚠️")

    elif kalkulator == 'Kalkulator pH':
        # Kalkulator pH
        ph_inlet = st.number_input("Masukkan nilai pH di inlet", min_value=0.0, max_value=14.0, step=0.1)
        ph_outlet = st.number_input("Masukkan nilai pH di outlet", min_value=0.0, max_value=14.0, step=0.1)

        if st.button("Evaluasi pH"):
            if 6.5 <= ph_outlet <= 8.5:
                st.success(f"pH outlet ({ph_outlet}) dalam rentang normal 👍")
        else:
            st.warning(f"pH outlet ({ph_outlet}) di luar rentang ideal ⚠️")
