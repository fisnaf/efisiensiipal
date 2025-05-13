import streamlit as st

st.set_page_config(page_title="Evaluasi IPAL & Baku Mutu", layout="centered")

st.title("Aplikasi Evaluasi Efisiensi IPAL")
st.markdown("Perhitungan efisiensi parameter BOD, COD, TSS, dan pH serta pembanding terhadap baku mutu berdasarkan **Permen LHK No. 5 Tahun 2020**")

# Baku mutu berdasarkan Permen LHK No. 5 Tahun 2020 Lampiran III Bagian C
baku_mutu = {
    "BOD": 30.0,    # mg/L
    "COD": 100.0,   # mg/L
    "TSS": 30.0,    # mg/L
    "pH_min": 6.5,
    "pH_max": 8.5
}

st.header("1. Kalkulator Efisiensi BOD")
bod_inlet = st.number_input("Masukkan BOD inlet (mg/L)", min_value=0.0)
bod_outlet = st.number_input("Masukkan BOD outlet (mg/L)", min_value=0.0)
if st.button("Hitung Efisiensi BOD"):
    if bod_inlet <= 0:
        st.error("BOD inlet harus lebih dari 0")
    elif bod_outlet > bod_inlet:
        st.error("BOD outlet tidak boleh lebih besar dari inlet")
    else:
        efisiensi_bod = (bod_inlet - bod_outlet) / bod_inlet * 100
        st.success(f"Efisiensi BOD: {efisiensi_bod:.2f}%")
        if bod_outlet <= baku_mutu["BOD"]:
            st.info(f"BOD outlet ({bod_outlet} mg/L) sesuai baku mutu ✅")
        else:
            st.warning(f"BOD outlet ({bod_outlet} mg/L) melebihi baku mutu ({baku_mutu['BOD']} mg/L) ⚠️")

st.header("2. Kalkulator Efisiensi COD")
cod_inlet = st.number_input("Masukkan COD inlet (mg/L)", min_value=0.0)
cod_outlet = st.number_input("Masukkan COD outlet (mg/L)", min_value=0.0)
if st.button("Hitung Efisiensi COD"):
    if cod_inlet <= 0:
        st.error("COD inlet harus lebih dari 0")
    elif cod_outlet > cod_inlet:
        st.error("COD outlet tidak boleh lebih besar dari inlet")
    else:
        efisiensi_cod = (cod_inlet - cod_outlet) / cod_inlet * 100
        st.success(f"Efisiensi COD: {efisiensi_cod:.2f}%")
        if cod_outlet <= baku_mutu["COD"]:
            st.info(f"COD outlet ({cod_outlet} mg/L) sesuai baku mutu ✅")
        else:
            st.warning(f"COD outlet ({cod_outlet} mg/L) melebihi baku mutu ({baku_mutu['COD']} mg/L) ⚠️")

st.header("3. Kalkulator Efisiensi TSS")
tss_inlet = st.number_input("Masukkan TSS inlet (mg/L)", min_value=0.0)
tss_outlet = st.number_input("Masukkan TSS outlet (mg/L)", min_value=0.0)
if st.button("Hitung Efisiensi TSS"):
    if tss_inlet <= 0:
        st.error("TSS inlet harus lebih dari 0")
    elif tss_outlet > tss_inlet:
        st.error("TSS outlet tidak boleh lebih besar dari inlet")
    else:
        efisiensi_tss = (tss_inlet - tss_outlet) / tss_inlet * 100
        st.success(f"Efisiensi TSS: {efisiensi_tss:.2f}%")
        if tss_outlet <= baku_mutu["TSS"]:
            st.info(f"TSS outlet ({tss_outlet} mg/L) sesuai baku mutu ✅")
        else:
            st.warning(f"TSS outlet ({tss_outlet} mg/L) melebihi baku mutu ({baku_mutu['TSS']} mg/L) ⚠️")

st.header("4. Evaluasi pH")
ph_outlet = st.number_input("Masukkan pH outlet", min_value=0.0)
if st.button("Evaluasi pH"):
    if baku_mutu["pH_min"] <= ph_outlet <= baku_mutu["pH_max"]:
        st.success(f"pH outlet ({ph_outlet}) dalam rentang baku mutu (6.5–8.5) ✅")
    else:
        st.warning(f"pH outlet ({ph_outlet}) di luar baku mutu (6.5–8.5) ⚠️")

st.caption("Dibuat oleh Zafindo Group | Mengacu Permen LHK No. 5 Tahun 2020")
