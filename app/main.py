import streamlit as st
from api.utils import query_local_llm

st.set_page_config(page_title="Local LLM Chat", page_icon=":shark:", layout="wide")
st.title("Local LLM ChatAPP")
st.sidebar.header("Settings")

model_name = st.sidebar.selectbox(
    "Choose a model",
    ["llama3", "Phi3", "Mistral"]
)

user_input = st.text_input("Enter your query", key="user_input")

if st.button("Submit"):
    with st.spinner("Processing..."):
        response = query_local_llm(model_name, user_input)
        st.write(f"Response: {response}")
