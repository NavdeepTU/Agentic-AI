import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# st.session_state -> dict -> resets only when we mannually refresh the page

CONFIG = {"configurable": {"thread_id": "1"}}

if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# loading the conversation history
for message in st.session_state["message_history"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type here")

if user_input:

    # first add the message to the message history
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # first add the message to the message history
    # st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
                message_chunk.content for message_chunk, metadata in chatbot.stream(
                {"messages": user_input},
                config={"configurable": {"thread_id": "1"}},
                stream_mode="messages"
            )
        )

    st.session_state["message_history"].append({"role":"assistant", "content": ai_message})

