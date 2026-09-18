from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

llm  = ChatGroq(model="openai/gpt-oss-120b")

if "message" not in st.session_state:
    st.session_state.message =[]

st.subheader("QNA BOT")

for msg in st.session_state.message:
    st.chat_message(msg.get("role")).markdown(msg.get("content"))

query = st.chat_input("Hello! Ask Anythings.....")
if query:
    st.session_state.message.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(st.session_state.message)
    st.session_state.message.append({"role":"ai", "content":res.content})
    st.chat_message("ai").markdown(res.content)
