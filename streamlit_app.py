import streamlit as st

st.title("Como votam?")
st.write(
    "Saiba como seus parlamentares eleitos votam no Congresso Nacional"
)
lable = "Votação"
if action == "PL do Estupro":
    lable = "PL do Estupro"
elif action == "PEC da Blindagem":
    lable = "PEC da Blindagem"
elif action == "PEC da Pedofilia":
    lable = "PEC da Pedofilia"

with st.container():
    st.write("Escolha a votação desejada")
action = st.menu_button(lable, options=["PL do Estupro", "PEC da Blindagem", "PEC da Pedofilia"])
if action == "PL do Estupro":
    st.write("Exporting as CSV...")
elif action == "PEC da Blindagem":
    st.write("Exporting as JSON...")
elif action == "PEC da Pedofilia":
    st.write("Exporting as PDF...")