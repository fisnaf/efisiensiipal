import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Efisiensi IPAL", layout="wide")

# Gaya latar belakang yang ringan dan tematik (air/IPAL)
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1506368249639-73a05d6f6488?auto=format&fit=crop&w=1650&q=80");
background-size: cover;
background-attachment: fixed;
}
[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
.stMarkdown, .stTextInput, .stNumberInput, .stButton {
color: black;
}
h1, h2, h3, h4 {
color: black;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title('Menu')
menu = st.sidebar.radio('Pilih Menu', ['Beranda', 'Kalkulator Efisiensi'])

# Fungsi tampilan beranda
def show_beranda():
    st.title("🌱 Aplikasi Efisiensi IPAL")
    st.write("""
    Selamat datang di aplikasi edukatif untuk menghitung **efisiensi Instalasi Pengolahan Air Limbah (IPAL)**.
    
    Aplikasi ini bertujuan untuk memberikan pemahaman sederhana mengenai bagaimana mengukur seberapa efektif suatu IPAL bekerja dalam mengurangi polutan dari air limbah.
    
    Silakan pilih menu **"Kalkulator Efisiensi"** untuk memulai perhitungan.
    """)

# Fungsi kalkulator efisiensi IPAL
def kalkulator_ipal():
    st.title("🌎 Kalkulator Efisiensi IPAL (Instalasi Pengolahan Air Limbah)")

    st.header("📚 Pendahuluan")
    st.write("""
    IPAL adalah sistem yang dirancang untuk mengolah air limbah agar aman dibuang ke lingkungan atau digunakan kembali.
    Penting untuk mengukur **efisiensi** IPAL dalam menurunkan polutan dari air limbah.
    """)

    st.header("🔎 Apa itu Inlet dan Outlet?")
    st.write("""
    - **Inlet**: Titik masuk air limbah ke sistem pengolahan, biasanya dengan konsentrasi polutan tinggi.
    - **Outlet**: Titik keluarnya air yang telah diolah. Harusnya konsentrasi polutan lebih rendah.
    """)

    st.header("🧮 Rumus Perhitungan Efisiensi")
    st.latex(r'''
    \text{Efisiensi (\%)} = \frac{C_{\text{inlet}} - C_{\text{outlet}}}{C_{\text{inlet}}} \times 100
    ''')
    st.markdown("""
    - \( C_{\text{inlet}} \): Konsentrasi polutan di inlet (mg/L)  
    - \( C_{\text{outlet}} \): Konsentrasi polutan di outlet (mg/L)
    """)

    st.header("📊 Evaluasi Efisiensi IPAL Berdasarkan Parameter")
    st.write("""
    Parameter utama yang biasa dievaluasi:
    - **BOD**
    - **COD**
    - **pH**
    - **TSS**
    """)

    st.header("🛠️ Hitung Efisiensi IPAL Anda")
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
    st.caption("© 2025 | Aplikasi edukatif IPAL 🌱")

# Routing menu
if menu == 'Beranda':
    show_beranda()
elif menu == 'Kalkulator Efisiensi':
    kalkulator_ipal()
