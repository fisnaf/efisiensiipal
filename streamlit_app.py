import streamlit as st

def main():
    # Judul Halaman
    st.title("🌎 Kalkulator Efisiensi IPAL (Instalasi Pengolahan Air Limbah)")

    # Pendahuluan
    st.header("📚 Pendahuluan")
    st.write("""
    Instalasi Pengolahan Air Limbah (IPAL) adalah sistem yang dirancang untuk mengolah air limbah sehingga dapat dibuang ke lingkungan dengan aman atau bahkan digunakan kembali.
    IPAL memainkan peran penting dalam menjaga kualitas air dan kesehatan lingkungan.

    Dalam proses pengolahan, sangat penting untuk mengukur **efisiensi** IPAL, yaitu seberapa besar kemampuan instalasi dalam menurunkan konsentrasi polutan dari air limbah.
    """)

    # Penjelasan Inlet dan Outlet
    st.header("🔎 Apa itu Inlet dan Outlet?")
    st.write("""
    - **Inlet** adalah titik masuknya air limbah ke dalam sistem pengolahan. Biasanya air di inlet memiliki konsentrasi polutan yang tinggi.
    - **Outlet** adalah titik keluarnya air dari sistem setelah mengalami proses pengolahan. Konsentrasi polutan di outlet seharusnya jauh lebih rendah.

    Dengan membandingkan konsentrasi di inlet dan outlet, kita dapat menghitung berapa persen polutan yang berhasil dihilangkan.
    """)

    # Rumus Efisiensi
    st.header("🧮 Rumus Perhitungan Efisiensi")
    st.latex(r'''
    \text{Efisiensi (\%)} = \frac{C_{\text{inlet}} - C_{\text{outlet}}}{C_{\text{inlet}}} \times 100
    ''')
    st.write("Keterangan:")
    st.markdown("""
    - \( C_{\text{inlet}} \) = Konsentrasi polutan pada inlet (mg/L)  
    - \( C_{\text{outlet}} \) = Konsentrasi polutan pada outlet (mg/L)
    """)

    # Input User
    st.header("🛠️ Hitung Efisiensi IPAL Anda")
    c_inlet = st.number_input("Masukkan konsentrasi polutan inlet (mg/L)", min_value=0.0, step=0.1)
    c_outlet = st.number_input("Masukkan konsentrasi polutan outlet (mg/L)", min_value=0.0, step=0.1)

    # Tombol untuk menghitung
    if st.button("Hitung Efisiensi"):
        if c_inlet <= 0:
            st.error("Konsentrasi inlet harus lebih dari 0.")
        elif c_outlet > c_inlet:
            st.error("Konsentrasi outlet tidak boleh lebih besar dari inlet.")
        else:
            efisiensi = ((c_inlet - c_outlet) / c_inlet) * 100
            st.success(f"Efisiensi IPAL adalah {efisiensi:.2f}%")

            # Penilaian Efisiensi
            if efisiensi >= 90:
                st.balloons()
                st.info("Kinerja IPAL: Sangat Baik ✅")
            elif efisiensi >= 70:
                st.info("Kinerja IPAL: Cukup Baik ✅")
            else:
                st.warning("Kinerja IPAL: Perlu Ditingkatkan ⚠️")

    # Footer
    st.markdown("---")
    st.caption("© 2025 | Dibuat untuk edukasi jurusan Pengolahan Limbah Industri 🌱")

if __name__ == "__main__":
    main()
