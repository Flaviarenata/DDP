import streamlit as st

st.title("Ini Halaman Nabung!")

with st.form("nabung"):
    nama = st.text_input("Masukkan Nama")
    nominal = st.number_input("Masukkan Nominal Nabung")
    submit = st.form_submit_button("Save")

if submit:
    st.write(f"Nama: {nama}")
    st.session_state["nabung"].append({
        "nama": nama,
        "nominal": nominal
    })

    st.success("Data berhasil menabung!")