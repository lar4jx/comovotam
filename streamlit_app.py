import streamlit as st

st.title("Como votam?")
st.write(
    "Saiba como seus parlamentares eleitos votam no Congresso Nacional"
)
if "selected_sphere" not in st.session_state:
    st.session_state.selected_sphere = None

with st.container():
    st.write("Escolha a votação desejada")

st.session_state.selected_sphere = st.segmented_control(
    "Esfera", 
    options=["Estadual", "Federal"]
)
if st.session_state.selected_sphere == "Estadual":
    col1, col2, col3 = st.columns(3)
    with col1:
            option = st.selectbox(
                "Escolha a votação desejada",
                ("Lei Antigênero (Lei 12.479/2025)", "PL Agrotóxicos (PL 828/2023)", "PEC da Pedofilia"),
                key="voting_option"
            )
            if option == "Lei Antigênero (Lei 12.479/2025)":
                st.write("Você escolheu a Lei Antigênero (Lei 12.479/2025)")
            elif option == "PL Agrotóxicos (PL 828/2023)":
                st.write("Você escolheu o PL Agrotóxicos (PL 828/2023)")
            elif option == "PEC da Pedofilia":
                st.write("Você escolheu a PEC da Pedofilia")
    
elif st.session_state.selected_sphere == "Federal":
    col1, col2, col3 = st.columns(3)
    with col1:
        option = st.selectbox(
            "Escolha a votação desejada",
            ("PL do Estupro (PL nº 1.904/2024)", "PEC da Blindagem (PEC nº 3/2021)", "PDL da Pefofilia (PDL nº 3/2025)"),
            key="voting_option"
        )
        if option == "PL do Estupro (PL nº 1.904/2024)":
            st.write("Você escolheu o PL do Estupro")
            st.image("AmaroNeto.jpg", caption="Amaro Neto (PP-ES) - Fonte: Câmara dos Deputados",)
            st.image("DaVitoria.jpg", caption="Da Vitoria (PP-ES) - Fonte: Câmara dos Deputados",)
            st.image("DrVictorLinhalis.jpg", caption="Dr. Victor Linhalis (PSB-ES) - Fonte: Câmara dos Deputados",)
            st.image("EvairDeMelo.jpg", caption="Evair de Melo (Republicanos-ES) - Fonte: Câmara dos Deputados",)
            st.image("GilvanDaFederal.jpg", caption="Gilvan da Federal (PL-ES) - Fonte: Câmara dos Deputados",)
            st.image("HelderSalomão.jpg", caption="Helder Salomão (PT-ES) - Fonte: Câmara dos Deputados",)
            st.image("JackRocha.jpg", caption="Jack Rocha (PT-ES) - Fonte: Câmara dos Deputados",)
            st.image("MessiasDonato.jpg", caption="Messias Donato (UNIÃO-ES) - Fonte: Câmara dos Deputados",)
            st.image("PauloFolletto.jpg", caption="Paulo Folletto (PSB-ES) - Fonte: Câmara dos Deputados",)


        elif option == "PEC da Blindagem (PEC nº 3/2021)":
            st.write("Você escolheu a PEC da Blindagem (PEC nº 3/2021)")
            st.image("AmaroNeto.jpg", caption="Amaro Neto (PP-ES) - Fonte: Câmara dos Deputados",)
            st.image("DaVitoria.jpg", caption="Da Vitoria (PP-ES) - Fonte: Câmara dos Deputados",)
            st.image("DrVictorLinhalis.jpg", caption="Dr. Victor Linhalis (PSB-ES) - Fonte: Câmara dos Deputados",)
            st.image("EvairDeMelo.jpg", caption="Evair de Melo (Republicanos-ES) - Fonte: Câmara dos Deputados",)
            st.image("GilvanDaFederal.jpg", caption="Gilvan da Federal (PL-ES) - Fonte: Câmara dos Deputados",)
            st.image("HelderSalomão.jpg", caption="Helder Salomão (PT-ES) - Fonte: Câmara dos Deputados",)
            st.image("JackRocha.jpg", caption="Jack Rocha (PT-ES) - Fonte: Câmara dos Deputados",)
            st.image("MessiasDonato.jpg", caption="Messias Donato (UNIÃO-ES) - Fonte: Câmara dos Deputados",)
            st.image("PauloFolletto.jpg", caption="Paulo Folletto (PSB-ES) - Fonte: Câmara dos Deputados",)

            
        elif option == "PDL da Pefofilia (PDL nº 3/2025)":
            st.write("Você escolheu o PDL da Pefofilia (PDL nº 3/2025)")
            st.image("AmaroNeto.jpg", caption="Amaro Neto (PP-ES) - Fonte: Câmara dos Deputados",)
            st.image("DaVitoria.jpg", caption="Da Vitoria (PP-ES) - Fonte: Câmara dos Deputados",)
            st.image("DrVictorLinhalis.jpg", caption="Dr. Victor Linhalis (PSB-ES) - Fonte: Câmara dos Deputados",)
            st.image("EvairDeMelo.jpg", caption="Evair de Melo (Republicanos-ES) - Fonte: Câmara dos Deputados",)
            st.image("GilvanDaFederal.jpg", caption="Gilvan da Federal (PL-ES) - Fonte: Câmara dos Deputados",)
            st.image("HelderSalomão.jpg", caption="Helder Salomão (PT-ES) - Fonte: Câmara dos Deputados",)
            st.image("JackRocha.jpg", caption="Jack Rocha (PT-ES) - Fonte: Câmara dos Deputados",)
            st.image("MessiasDonato.jpg", caption="Messias Donato (UNIÃO-ES) - Fonte: Câmara dos Deputados",)
            st.image("Paulo Folletto.jpg", caption="Paulo Folletto (PSB-ES) - Fonte: Câmara dos Deputados",)