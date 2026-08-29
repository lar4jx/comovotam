import streamlit as st

st.title("Como votam?")
st.write(
    "Saiba como seus parlamentares eleitos votam no Congresso Nacional"
)
lable = "Votação"

with st.container():
    st.write("Escolha a votação desejada")
action = st.menu_button(lable, options=["PL do Estupro", "PEC da Blindagem", "PEC da Pedofilia"])
if action == "PL do Estupro":
    st.write("Exporting as CSV...")
    lable = "PL do Estupro"
    st.menu_button(lable)
elif action == "PEC da Blindagem":
    st.write("Exporting as JSON...")
    lable = "PEC da Blindagem"
    st.menu_button(lable)
elif action == "PEC da Pedofilia":
    st.write("Exporting as PDF...")
    lable = "PEC da Pedofilia"
    st.menu_button(lable)