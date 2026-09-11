import streamlit as st
from google import genai

st.set_page_config(page_title="Chatbot do Bem", page_icon="🤖")

st.title("🤖 Chatbot Bem")

try:
    st.sidebar.image("bem.jpg", caption="O Bem", width='stretch')
except Exception:
    st.sidebar.warning("Coloque a imagem 'bem.png' na pasta do projeto!")

st.sidebar.markdown("### Sobre")
st.sidebar.write("Este é o seu assistente inteligente integrado com o Gemini.")

client = genai.Client()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_session" not in st.session_state:
    st.session_state.chat_session = client.chats.create(model="gemini-2.5-flash")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Digite sua mensagem para o Bem..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("O Bem está pensando..."):
            response = st.session_state.chat_session.send_message(prompt)
            st.markdown(response.text)
            
    st.session_state.messages.append({"role": "assistant", "content": response.text})