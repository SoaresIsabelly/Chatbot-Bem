import os
from google import genai

# Inicializa o cliente do Gemini
client = genai.Client()

# Inicia a sessão de chat
chat = client.chats.create(model="gemini-2.5-flash")

print("🤖 Chatbot iniciado! Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")
    
    if user_input.lower() in ["sair", "exit", "quit"]:
        print("🤖 Até logo!")
        break
    
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}\n")