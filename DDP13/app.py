import streamlit as st

st.write("")

dashboard = st.Page("./pages/dashboard.py", title="Dashboard")
nabung = st.Page("./pages/nabung.py", title="Nabung")

pg = st.navigation({
    "Dashboard" : [dashboard],
    "Nabung" : [nabung],
})

if "nabung" not in st.session_state:
    st.session_state["nabung"] = []

pg.run()    