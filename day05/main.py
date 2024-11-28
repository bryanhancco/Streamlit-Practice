import streamlit as st
from graph_auth import Graph_Auth
from RAG_Sharepoint import RAG_Sharepoint
from streamlit_option_menu import option_menu

codigo_secreto = "sk-proj-_fd356p2NJWDUlpGSZMjc4TI3tQ_RWqf1PfdOZVOn2c2cN8jdtWN1EIfluT3BlbkFJG6FqPrBH_5Y8e4-"

def refresh():
    st.empty()
    st.rerun()

if "has_auth_data" not in st.session_state:
    st.session_state["has_auth_data"] = False

if "need_reload" not in st.session_state:
    st.session_state["need_reload"] = False

if not st.session_state["has_auth_data"]:  
    st.title("Bienvenido")
    st.write("Realiza el proceso de autenticación")
    if st.button("Iniciar Sesión"):
        graph = Graph_Auth()
        st.session_state["has_auth_data"] = True
        with st.spinner("Generando la base de datos..."):
            st.session_state["rag"] = RAG_Sharepoint(graph.get_access_token())
        graph.close_window()
        refresh()

if st.session_state["has_auth_data"] and st.session_state["need_reload"]:
    st.session_state["need_reload"] = False

elif not st.session_state["has_auth_data"]:    
    st.stop()

with st.sidebar:
    selected = option_menu(
        menu_title="Menu de opciones",
        options=["Chat", "Estadísticas", "Cerrar Sesión"]
    )


if selected == "Chat":
    def add_message(message):
        st.session_state["chat_history"].append(message)
        if len(st.session_state.chat_history) > HISTORY_CHAT:
            st.session_state.chat_history.pop(0)

    def get_reponse(query, chat_history):
        response = st.session_state["rag"].hacer_pregunta(pregunta=query, history=chat_history)
        print(response.usage_metadata)
        return response.content

    st.title(f"Chat con Sharepoint")
    st.markdown(
            """
            <style>
                .element-container:has(#button-after) + div button {
                    display: flex;
                    justify-content: flex-end; 
                    width: auto;
                    margin-left: 40%;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

    st.info(
                f"Estas consultado información de los Sites a los que tienes acceso"
            )

    prompt = st.chat_input("Escribe tu pregunta...")
    if "user_prompt_history" not in st.session_state:
        st.session_state["user_prompt_history"] = []
    if "chat_answers_history" not in st.session_state:
        st.session_state["chat_answers_history"] = []
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    if "sharepoint_site" not in st.session_state:
        st.session_state["sharepoint_site"] = ""
        
    if prompt:
        with st.spinner("Generando respuesta......"):
            output = get_reponse(
                query=prompt, chat_history=st.session_state["chat_history"]
            )
            st.session_state["chat_answers_history"].append(output)
            st.session_state["user_prompt_history"].append(prompt)
            add_message((prompt, output))

    if st.session_state["chat_answers_history"]:
        count = 0
        for i, j in zip(
            st.session_state["chat_answers_history"],
            st.session_state["user_prompt_history"],
        ):
            message1 = st.chat_message("user")
            message1.markdown(j)
            message2 = st.chat_message("assistant")
            message2.markdown(i)
                    #st.markdown('<span id="button-after"></span>', unsafe_allow_html=True)
                    #st.button(
                    #    label="Mejorar respuesta", key=count, on_click=improve_answer, args=[1]
                    #)
            count += 1


if selected == "Estadísticas":
    st.title("Estadísticas")

if selected == "Cerrar Sesión":
    st.session_state["has_auth_data"] = False
    st.session_state["need_reload"] = False
    st.rerun()