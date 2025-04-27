import streamlit as st

def main():
    st.title("Kalkulator Efisiensi IPAL")
    st.markdown("Hitung efisiensi instalasi pengolahan air limbah berdasarkan konsentrasi polutan.")

    # Input dari user
    c_inlet = st.number_input("Masukkan konsentrasi polutan inlet (mg/L)", min_value=0.0, step=0.1)
    c_outlet = st.number_input("Masukkan konsentrasi polutan outlet (mg/L)", min_value=0.0, step=0.1)

    # Tombol untuk hitung
    if st.button("Hitung Efisiensi"):
        if c_inlet <= 0:
            st.error("Konsentrasi inlet harus lebih dari 0.")
        elif c_outlet > c_inlet:
            st.error("Konsentrasi outlet tidak boleh lebih besar dari inlet.")
        else:
            efisiensi = ((c_inlet - c_outlet) / c_inlet) * 100
            st.success(f"Efisiensi IPAL adalah {efisiensi:.2f}%")

            if efisiensi >= 90:
                st.info("Kinerja IPAL: Sangat Baik ✅")
            elif efisiensi >= 70:
                st.info("Kinerja IPAL: Cukup Baik ✅")
            else:
                st.warning("Kinerja IPAL: Perlu Ditingkatkan ⚠️")

if __name__ == "__main__":
    main()
