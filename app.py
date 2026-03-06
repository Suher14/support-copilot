import streamlit as st
from rag_pipeline import rag_pipeline
from guardrails import check_guardrails

st.set_page_config(page_title="AI Customer Support Copilot", page_icon="💬")

st.title("💬 AI Customer Support Copilot")
st.write("Ask a support question about billing, login, subscriptions, or security.")
with st.sidebar:
    st.header("About")
    st.write(
        "This demo shows a RAG-based AI Customer Support Copilot that retrieves "
        "support documents and generates grounded responses."
    )
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

    # guardrails
    guardrail = check_guardrails(query)

    if guardrail:
        answer = guardrail
        sources = []

    else:
        answer, sources = rag_pipeline(query)

    # display assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)

        if sources:
            st.markdown("**Sources:**")
            for s in sources:
                st.write("-", s)

    st.session_state.messages.append({"role": "assistant", "content": answer})