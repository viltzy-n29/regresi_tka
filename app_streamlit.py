import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.joblib')

st.title("🎓 Prediksi Nilai TKA")
st.write("Atur nilai menggunakan slider")


jam_belajar = st.slider(
    "Jam belajar per hari",
    min_value=0,
    max_value=12,
    value=4,
    step=1
)

persen_kehadiran = st.slider(
    "Persentase kehadiran (%)",
    min_value=0,
    max_value=100,
    value=80,
    step=1
)

bimbel = st.selectbox(
    "Mengikuti bimbel?",
    ["ya", "tidak"]
)

if st.button("Prediksi Nilai TKA"):
    data_baru = pd.DataFrame(
        [[jam_belajar, persen_kehadiran, bimbel]],
        columns=['jam_belajar_per_hari', 'persen_kehadiran', 'bimbel']
    )

    prediksi = model.predict(data_baru)

    st.success(f"📊 Prediksi Nilai TKA: **{prediksi[0]:.0f}**")