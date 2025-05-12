import streamlit as st

# Konfigurasi tampilan halaman
st.set_page_config(page_title="Kalkulator Efisiensi IPAL", layout="wide")

# CSS latar belakang dan gaya tampilan
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3, [data-testid="stSidebar"] p,
[data-testid="stSidebar"] li {
color: white;
}
.stMarkdown {
color: black;
}
h2 {
color: black;
border-bottom: 4px solid black;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title('Menu')
menu = st.sidebar.radio('Pilih Menu', ['Beranda', 'Penjelasan IPAL', 'Perhitungan Efisiensi'])

# Fungsi untuk judul hitam bergaris
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
- \( C_{\text{inlet}} \): Konsentrasi polutan inlet (mg/L)  
- \( C_{\text{outlet}} \): Konsentrasi polutan outlet (mg/L)
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

    st.markdown("---")
    st.caption("© 2025 | Edukasi IPAL untuk Pengolahan Limbah Industri")

