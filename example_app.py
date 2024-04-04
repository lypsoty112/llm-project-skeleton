import streamlit as st

from _startup import startup
from src.chains.example_chain import ExampleChain
from src.models.example_model import ExampleChainInput

startup()

chain = ExampleChain()
chain.build()

st.title('SarcasticGPT')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "human", "content": prompt})
    with st.chat_message("human"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = chain.run(
            data=ExampleChainInput(
                messages=st.session_state.messages
            )
        ).response
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})