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
IPAL (Instalasi Pengolahan Air Limbah) adalah sistem yang digunakan untuk mengolah air limbah agar dapat memenuhi standar baku mutu yang ditetapkan sebelum dibuang ke lingkungan. Tujuan utama dari IPAL adalah mengurangi polutan dalam air, seperti BOD (Biochemical Oxygen Demand), COD (Chemical Oxygen Demand), TSS (Total Suspended Solids), dan pH, agar tidak mencemari ekosistem perairan.

### Proses IPAL  
Proses pengolahan air limbah terdiri dari beberapa tahap, di antaranya:  
1. **Pengolahan Fisik**: Menghilangkan partikel besar dan padatan dari air limbah melalui pemisahan mekanik, seperti penyaringan atau pengendapan.
2. **Pengolahan Kimia**: Menggunakan bahan kimia untuk mengendapkan atau mengurai bahan kimia berbahaya dalam air limbah.
3. **Pengolahan Biologis**: Menggunakan mikroorganisme untuk menguraikan bahan organik dalam air limbah, biasanya dengan proses aerasi (penambahan oksigen).
4. **Pengolahan Lanjutan**: Biasanya dilakukan untuk mencapai kualitas air yang lebih tinggi, seperti penghilangan nutrien (nitrat, fosfat) dan pengolahan dengan teknologi membran (misalnya, RO - Reverse Osmosis).

### Tujuan dan Manfaat IPAL  
- **Menjaga Kualitas Lingkungan**: Mengurangi pencemaran air dengan memastikan air limbah yang dibuang ke sungai, laut, atau saluran lain memenuhi baku mutu.
- **Pemulihan Ekosistem**: Air yang telah diolah dapat digunakan kembali untuk berbagai tujuan, termasuk irigasi, rekreasi, atau bahkan air minum (setelah pemurnian lebih lanjut).
- **Kepatuhan terhadap Regulasi**: IPAL membantu industri atau pemukiman dalam memenuhi regulasi pemerintah yang mengatur baku mutu air limbah.

### Teknologi yang Digunakan dalam IPAL  
Terdapat berbagai teknologi yang digunakan dalam IPAL untuk menangani berbagai jenis limbah, di antaranya:  
1. **Reaktor Anaerobik**: Menggunakan mikroorganisme yang bekerja tanpa oksigen untuk mengurai limbah organik, cocok untuk limbah dengan kadar BOD tinggi.
2. **Reaktor Aerobik**: Menggunakan mikroorganisme yang membutuhkan oksigen untuk menguraikan limbah organik.
3. **Sistem Membran**: Menggunakan teknologi membran, seperti filtrasi tekanan tinggi (RO), untuk mengolah air dengan lebih efisien, sering digunakan untuk mengolah air limbah industri atau air limbah yang sangat tercemar.
4. **Sistem Biofilter**: Menggunakan media biologi untuk menyaring kontaminan organik dari air limbah.

### Regulasi Baku Mutu  
Baku mutu limbah cair domestik diatur dalam **PermenLHK No. 5 Tahun 2022** (Lampiran I), dengan standar sebagai berikut:
- **BOD**: Maksimum 30 mg/L
- **COD**: Maksimum 100 mg/L
- **TSS**: Maksimum 30 mg/L
- **pH**: Antara 6,5–8,5

Baku mutu ini bertujuan untuk melindungi kualitas air yang ada di alam serta keberlanjutan ekosistem perairan. Setiap pengolahan limbah harus memastikan bahwa kualitas air yang dibuang ke lingkungan memenuhi batasan tersebut.

### Manfaat Kepatuhan terhadap Baku Mutu  
- **Perlindungan Kesehatan Manusia**: Pengolahan air limbah yang tepat dapat mengurangi risiko penyakit akibat pencemaran air.
- **Pelestarian Keanekaragaman Hayati**: Air yang lebih bersih mendukung kehidupan organisme aquatik yang lebih sehat dan berkelanjutan.
- **Penghindaran Sanksi**: Pemenuhan terhadap baku mutu adalah syarat yang diwajibkan oleh pemerintah untuk setiap fasilitas yang mengolah air limbah.

Menjaga kualitas air dengan menerapkan sistem IPAL yang baik tidak hanya bermanfaat untuk kelestarian alam tetapi juga untuk kesehatan manusia dan keberlanjutan industri.

""")  
    st.write("### Bagaimana IPAL Membantu Lingkungan?")  
    st.write("""  
Pengolahan air limbah yang efektif membantu mencegah pencemaran lingkungan yang dapat menyebabkan kerusakan ekosistem. Misalnya, limbah yang mengandung bahan kimia berbahaya bisa mencemari tanah dan air jika tidak diolah dengan benar. Dengan adanya IPAL, limbah yang dibuang ke alam bisa memenuhi standar baku mutu yang telah ditetapkan, sehingga mengurangi dampak negatif terhadap lingkungan.

Pengolahan air limbah juga sangat penting dalam mendukung kegiatan industri yang ramah lingkungan. Dengan mematuhi regulasi yang ada, industri dapat beroperasi secara berkelanjutan tanpa merusak alam di sekitarnya.

""")  
    st.markdown("""  
- **Pemeliharaan Kualitas Lingkungan**: Tanpa pengolahan yang tepat, limbah domestik dan industri dapat mencemari sumber daya air yang sangat penting bagi kehidupan manusia dan makhluk hidup lainnya.
- **Penggunaan Ulang Air**: IPAL juga membuka peluang untuk penggunaan ulang air limbah, yang dikenal dengan istilah **reuse water**, yang semakin penting dalam menghadapi krisis air global.
""")  
    st.write("Dari sisi teknologi, pengolahan air limbah yang efektif membutuhkan peralatan dan proses yang canggih, termasuk reaktor biologis, teknologi membran, dan teknologi kimiawi, yang perlu dioperasikan secara hati-hati untuk menjaga efektivitasnya.")  

elif menu == 'Perhitungan Efisiensi':  
    bold_black_header("🛠️ Kalkulator Efisiensi IPAL")  
    kalkulator = st.sidebar.radio("Pilih Kalkulator", ['kalkulatpr Efisiensi IPAL', 'Kalkulator BOD', 'Kalkulator COD', 'Kalkulator TSS', 'Kalkulator pH'])  
  
    def baku_mutu_check(nama, nilai, ambang, satuan="mg/L"):  
        if nilai <= ambang:  
            st.success(f"{nama} ({nilai} {satuan}) **MEMENUHI** baku mutu ({nama} ≤ {ambang} {satuan})")  
        else:  
            st.error(f"{nama} ({nilai} {satuan}) **TIDAK MEMENUHI** baku mutu ({nama} ≤ {ambang} {satuan})")  
  
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
