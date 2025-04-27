import streamlit as st

def hitung_efisiensi(c_inlet, c_outlet):
    efisiensi = ((c_inlet - c_outlet) / c_inlet) * 100
    return efisiensi

def main():
    st.title("Kalkulator Efisiensi IPAL")
    st.write("Aplikasi ini menghitung efisiensi Instalasi Pengolahan Air Limbah (IPAL) berdasarkan konsentrasi polutan.")

    c_inlet = st.number_input("Masukkan konsentrasi polutan di inlet (mg/L)", min_value=0.0)
    c_outlet = st.number_input("Masukkan konsentrasi polutan di outlet (mg/L)", min_value=0.0)

    if st.button("Hitung Efisiensi"):
        if c_inlet <= 0:
            st.error("Konsentrasi inlet harus lebih dari 0.")
        elif c_outlet > c_inlet:
            st.error("Konsentrasi outlet tidak boleh lebih besar dari inlet.")
        else:
            efisiensi = hitung_efisiensi(c_inlet, c_outlet)
            st.success(f"Efisiensi IPAL: {efisiensi:.2f}%")

            if efisiensi >= 90:
                st.info("Kinerja IPAL sangat baik ✅")
            elif efisiensi >= 70:
                st.info("Kinerja IPAL cukup baik ✅")
            else:
                st.warning("Kinerja IPAL perlu ditingkatkan ⚠️")

if __name__ == "__main__":
    main()
