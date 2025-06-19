import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# ✅ Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Initialize the ChatOpenAI model
llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo",   # ✅ Use GPT-3.5 instead
    openai_api_key=api_key
)


# ✅ Memory for conversation context (stores previous chat history)
memory = ConversationBufferMemory()

# ✅ Chain to handle the conversation
chat_chain = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True  # Set to False to remove debug logging
)

# ✅ Function to ask the bot
def ask_agent(query: str) -> str:
    return chat_chain.run(query)


if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = ask_agent(user_input)
        print("Bot:", response)
