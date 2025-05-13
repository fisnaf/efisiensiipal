import streamlit as st

st.title("Aplikasi Edukatif IPAL - Evaluasi Efisiensi dan Baku Mutu")

# Input data dari pengguna
influent_bod = st.number_input("BOD influent (mg/L):", min_value=0.0, format="%.2f")
effluent_bod = st.number_input("BOD effluent (mg/L):", min_value=0.0, format="%.2f")

influent_cod = st.number_input("COD influent (mg/L):", min_value=0.0, format="%.2f")
effluent_cod = st.number_input("COD effluent (mg/L):", min_value=0.0, format="%.2f")

influent_tss = st.number_input("TSS influent (mg/L):", min_value=0.0, format="%.2f")
effluent_tss = st.number_input("TSS effluent (mg/L):", min_value=0.0, format="%.2f")

ph_effluent = st.number_input("pH effluent:", min_value=0.0, max_value=14.0, format="%.2f")

# Tombol hitung
if st.button("Hitung Efisiensi dan Evaluasi Baku Mutu"):
    # Hitung efisiensi
    def hitung_efisiensi(influent, effluent):
        if influent == 0:
            return 0
        return ((influent - effluent) / influent) * 100

    efisiensi_bod = hitung_efisiensi(influent_bod, effluent_bod)
    efisiensi_cod = hitung_efisiensi(influent_cod, effluent_cod)
    efisiensi_tss = hitung_efisiensi(influent_tss, effluent_tss)

    st.subheader("Hasil Perhitungan Efisiensi:")
    st.write(f"Efisiensi BOD: {efisiensi_bod:.2f}%")
    st.write(f"Efisiensi COD: {efisiensi_cod:.2f}%")
    st.write(f"Efisiensi TSS: {efisiensi_tss:.2f}%")

    # Evaluasi baku mutu berdasarkan PermenLHK No. 5 Tahun 2020 Lampiran III (Kegiatan Domestik)
    st.subheader("Evaluasi Kepatuhan terhadap Baku Mutu Effluent:")
    hasil_bod = "Memenuhi" if effluent_bod <= 30 else "Melebihi"
    hasil_cod = "Memenuhi" if effluent_cod <= 100 else "Melebihi"
    hasil_tss = "Memenuhi" if effluent_tss <= 30 else "Melebihi"
    hasil_ph = "Memenuhi" if 6.5 <= ph_effluent <= 8.5 else "Melebihi"

    st.write(f"BOD effluent: {effluent_bod:.2f} mg/L → {hasil_bod} baku mutu")
    st.write(f"COD effluent: {effluent_cod:.2f} mg/L → {hasil_cod} baku mutu")
    st.write(f"TSS effluent: {effluent_tss:.2f} mg/L → {hasil_tss} baku mutu")
    st.write(f"pH effluent: {ph_effluent:.2f} → {hasil_ph} baku mutu")

    st.markdown("""
    **Catatan:**
    Ambang batas baku mutu mengacu pada **PermenLHK No. 5 Tahun 2020 – Lampiran III (Kegiatan Domestik)**:
    - BOD ≤ 30 mg/L  
    - COD ≤ 100 mg/L  
    - TSS ≤ 30 mg/L  
    - pH antara 6.5 – 8.5
    """)

