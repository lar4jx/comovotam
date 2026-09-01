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
            with col2:
             st.write("Lei Antigênero (Lei 12.479/2025)")
             st.image("AdilsonEspindula.jpg", caption="Adilson Espindula (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("AlcântaroFilho.jpg", caption="Alcantâro Filho (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("AllanFerreira.jpg", caption="Allan Ferreira (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("BispoAlves.jpg", caption="Bispo Alves (Republicanos-ES) - Fonte: Câmara dos Deputados",)
             st.image("Callegari.jpg", caption="Callegari (PL-ES) - Fonte: Câmara dos Deputados",)
             st.image("CamilaValadão.jpg", caption="Camila Valadão (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("CapitãoAssunção.jpg", caption="Capitão Assumção (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("CoronelWeliton.jpg", caption="Coronel Weliton (UNIÃO-ES) - Fonte: Câmara dos Deputados",)
             st.image("DaryPagung.jpg", caption="Dary Pagung (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("DelegadoDaniloBahiense.jpg", caption="Delegado Danilo Bahiense (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("DenninhoSilva.jpg", caption="Denninho Silva (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("DrBrunoResende.jpg", caption="Dr Bruno Resende (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("EngenheiroJoséEsmeraldo.jpg", caption="Engenheiro José Esmeraldo (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("FábioDuarte.jpg", caption="Fábio Duarte (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("FabricioGandini.jpg", caption="Fabricio Gandini (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("HudsonLeal.jpg", caption="Hudson Leal (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("IrinyLopes.jpg", caption="Iriny Lopes (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("JanetaDeSá.jpg", caption="Janete de Sá (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("JoãoCoser.jpg", caption="João Coser (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("LucasPolese.jpg", caption="Lucas Polese (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("MarceloSantos.jpg", caption="Marcelo Santos (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("MarcosMadureira.jpg", caption="Marcus Maureira (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("MazinhoDosAnjos.jpg", caption="Mazinho dos Anjos (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("PabloMuribeca.jpg", caption="Pablo Muribeca (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("RaquelLessa.jpg", caption="Raquel Lessa (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("SergioMeneguelli.jpg", caption="Iriny Lopes (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("TyagoHoffmann.jpg", caption="Iriny Lopes (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("VandinhoLeite.jpg", caption="Vandinho Leite (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("Zépreto.jpg", caption="Zé Preto (PSB-ES) - Fonte: Câmara dos Deputados",)



elif st.session_state.selected_sphere == "Federal":
    col1, col2, col3 = st.columns(3)
    with col1:
        option = st.selectbox(
            "Escolha a votação desejada",
            ("PL do Estupro (PL nº 1.904/2024)", "PEC da Blindagem (PEC nº 3/2021)", "PDL da Pefofilia (PDL nº 3/2025)"),
            key="voting_option"
        )

#https://www.agazeta.com.br/es/politica/veja-como-votaram-os-deputados-do-es-na-pec-da-blindagem-0925
        #Imagens dos Deputados Federais do Espírito Santo
        if option == "PL do Estupro (PL nº 1.904/2024)":
            with col2:
             st.write("PL do Estupro (PL nº 1.904/2024)")
             st.image("AmaroNeto.jpg", caption="Amaro Neto (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("DaVitoria.jpg", caption="Da Vitoria (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("DrVictorLinhalis.jpg", caption="Dr. Victor Linhalis (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("EvairDeMelo.jpg", caption="Evair de Melo (Republicanos-ES) - Fonte: Câmara dos Deputados",)
             st.image("GilvanDaFederal.jpg", caption="Gilvan da Federal (PL-ES) - Fonte: Câmara dos Deputados",)
             st.image("HelderSalomão.jpg", caption="Helder Salomão (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("JackRocha.jpg", caption="Jack Rocha (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("MessiasDonato.jpg", caption="Messias Donato (UNIÃO-ES) - Fonte: Câmara dos Deputados",)
             st.image("PauloFolletto.jpg", caption="Paulo Folletto (PSB-ES) - Fonte: Câmara dos Deputados",)

            #Voto de Amaro Neto
            with col3:
                st.markdown(
                "    <br><br><br><br><br><br><br>   ",
                 unsafe_allow_html=True)
                st.markdown(
                    "<p style='color: green;'>A FAVOR</p>",
                    unsafe_allow_html=True)
                st.markdown(
                 "    <br><br><br><br><br><br>   ",
                unsafe_allow_html=True)

            #Voto de Da Vitoria
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Dr Victor Linhalis
            with col3:
                st.markdown(
                            "    <br><br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>  ",
                            unsafe_allow_html=True)
                
           #Voto de Evair de Melo
            with col3:
                st.markdown(
                            "    <br><br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Gilvan da Federal
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Helder Salomão
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: red;'>CONTRA</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Da Jack Rocha
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: red;'>CONTRA</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>  ",
                            unsafe_allow_html=True)

           #Voto de Messias Donato
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Paulo Folletto
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

        #fonte:https://www.agazeta.com.br/es/politica/veja-como-votaram-os-deputados-do-es-na-pec-da-blindagem-0925       
        #Imagens dos Deputados Federais do Espírito Santo
        elif option == "PEC da Blindagem (PEC nº 3/2021)":
            with col2:
             st.write("PEC da Blindagem (PEC nº 3/2021)")
             st.image("AmaroNeto.jpg", caption="Amaro Neto (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("DaVitoria.jpg", caption="Da Vitoria (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("DrVictorLinhalis.jpg", caption="Dr. Victor Linhalis (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("EvairDeMelo.jpg", caption="Evair de Melo (Republicanos-ES) - Fonte: Câmara dos Deputados",)
             st.image("GilvanDaFederal.jpg", caption="Gilvan da Federal (PL-ES) - Fonte: Câmara dos Deputados",)
             st.image("HelderSalomão.jpg", caption="Helder Salomão (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("JackRocha.jpg", caption="Jack Rocha (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("MessiasDonato.jpg", caption="Messias Donato (UNIÃO-ES) - Fonte: Câmara dos Deputados",)
             st.image("PauloFolletto.jpg", caption="Paulo Folletto (PSB-ES) - Fonte: Câmara dos Deputados",)
            #Voto de Amaro Neto
            with col3:
                st.markdown(
                "    <br><br><br><br><br><br><br>   ",
                 unsafe_allow_html=True)
                st.markdown(
                    "<p style='color: green;'>A FAVOR</p>",
                    unsafe_allow_html=True)
                st.markdown(
                 "    <br><br><br><br><br><br>   ",
                unsafe_allow_html=True)

            #Voto de Da Vitoria
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Dr Victor Linhalis
            with col3:
                st.markdown(
                            "    <br><br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>  ",
                            unsafe_allow_html=True)
                
           #Voto de Evair de Melo
            with col3:
                st.markdown(
                            "    <br><br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Gilvan da Federal
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Helder Salomão
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: red;'>CONTRA</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Da Jack Rocha
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: red;'>CONTRA</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>  ",
                            unsafe_allow_html=True)

           #Voto de Messias Donato
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Paulo Folletto
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

        
        #fonte:https://www.congressoemfoco.com.br/noticia/113622/veja-como-cada-deputado-votou-no-projeto-sobre-aborto-em-criancas
        #Imagens dos Deputados Federais do Espírito Santo
        elif option == "PDL da Pefofilia (PDL nº 3/2025)":
            with col2:
             st.write("PDL da Pefofilia (PDL nº 3/2025)")
             st.image("AmaroNeto.jpg", caption="Amaro Neto (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("DaVitoria.jpg", caption="Da Vitoria (PP-ES) - Fonte: Câmara dos Deputados",)
             st.image("DrVictorLinhalis.jpg", caption="Dr. Victor Linhalis (PSB-ES) - Fonte: Câmara dos Deputados",)
             st.image("EvairDeMelo.jpg", caption="Evair de Melo (Republicanos-ES) - Fonte: Câmara dos Deputados",)
             st.image("GilvanDaFederal.jpg", caption="Gilvan da Federal (PL-ES) - Fonte: Câmara dos Deputados",)
             st.image("HelderSalomão.jpg", caption="Helder Salomão (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("JackRocha.jpg", caption="Jack Rocha (PT-ES) - Fonte: Câmara dos Deputados",)
             st.image("MessiasDonato.jpg", caption="Messias Donato (UNIÃO-ES) - Fonte: Câmara dos Deputados",)
             st.image("PauloFolletto.jpg", caption="Paulo Folletto (PSB-ES) - Fonte: Câmara dos Deputados",)
            
            #Voto de Amaro Neto
            with col3:
                st.markdown(
                "    <br><br><br><br><br><br><br>   ",
                 unsafe_allow_html=True)
                st.markdown(
                    "<p style='color: green;'>A FAVOR</p>",
                    unsafe_allow_html=True)
                st.markdown(
                 "    <br><br><br><br><br><br>   ",
                unsafe_allow_html=True)

            #Voto de Da Vitoria
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Dr Victor Linhalis
            with col3:
                st.markdown(
                            "    <br><br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>  ",
                            unsafe_allow_html=True)
                
           #Voto de Evair de Melo
            with col3:
                st.markdown(
                            "    <br><br><br><br><br><br>  ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Gilvan da Federal
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Helder Salomão
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: red;'>CONTRA</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Da Jack Rocha
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: red;'>CONTRA</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>  ",
                            unsafe_allow_html=True)

           #Voto de Messias Donato
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)

           #Voto de Paulo Folletto
            with col3:
                st.markdown(
                            "    <br><br><br><br><br>   ",
                             unsafe_allow_html=True)
                st.markdown(
                                "<p style='color: green;'>A FAVOR</p>",
                                unsafe_allow_html=True)
                st.markdown(
                             "    <br><br><br><br><br><br>   ",
                            unsafe_allow_html=True)
