import streamlit as st
from rag_pipeline import rag_pipeline
from guardrails import check_guardrails

st.set_page_config(page_title="AI Customer Support Copilot", page_icon="💬")

st.title("💬 AI Customer Support Copilot")
st.write("Ask a support question about billing, login, subscriptions, or security.")

with st.sidebar:
    st.header("About")
    st.write(
        "This demo shows a Retrieval-Augmented Generation (RAG) based "
        "AI Customer Support Copilot that retrieves internal support "
        "documents and generates grounded responses."
    )

    if st.button("Reset Chat"):
        st.session_state.messages = []
        st.rerun()

# session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# chat input
query = st.chat_input("Type your support question...")

if query:

    # show user message
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    # guardrails check
    guardrail = check_guardrails(query)

    if guardrail:
        answer = guardrail
        sources = []
    else:
        answer, sources = rag_pipeline(query)

    # combine answer + sources
    assistant_content = answer

    if sources:
        assistant_content += "\n\n**Sources:**\n"
        for s in sources:
            assistant_content += f"- {s}\n"

    # display assistant message
    with st.chat_message("assistant"):
        st.markdown(assistant_content)

    # save to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_content}
    )