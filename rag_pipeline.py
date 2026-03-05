import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from retrieval import retrieve_documents

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version="2024-10-21",
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
)

deployment_name = os.getenv("AZURE_DEPLOYMENT", "gpt-4.1")

SYSTEM_PROMPT = """
You are a customer support AI assistant for a generic SaaS product.

Rules:
- Use ONLY the provided context to answer.
- Be calm, professional, and helpful.
- Do NOT claim you accessed or changed any real user account.
- Never ask for or accept passwords, 2FA codes, API keys, tokens, or payment card details.
- If the context does not contain enough information, say so and suggest what non-sensitive details the support agent should ask for next.
"""


def build_prompt(query: str, docs) -> str:
    context = "\n\n".join([f"({doc['name']}) {doc['content']}" for doc in docs])

    return f"""
Use ONLY the context below to answer.

Context:
{context}

You are a customer support copilot. Generate a structured suggestion for a support agent.

Return the answer in this format:

Category: <Billing / Subscription / Login / Cancellation / Security / Privacy / General>
Priority: <Low / Medium / High>

Suggested Reply:
<message to send to the customer>

Steps for the agent:
1. ...
2. ...
3. ...

Confidence: <0-100>

Question: {query}
"""


def generate_answer(prompt: str) -> str:
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT.strip()},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=300,
    )
    return response.choices[0].message.content.strip()


def rag_pipeline(query: str, k: int = 3):
    retrieved_docs = retrieve_documents(query, k=k)
    prompt = build_prompt(query, retrieved_docs)
    answer = generate_answer(prompt)
    sources = [doc["name"] for doc in retrieved_docs]
    return answer, sources


if __name__ == "__main__":
    q = "I was charged but my subscription is still inactive."
    answer, sources = rag_pipeline(q)
    print("Answer:\n", answer)
    print("\nSources:", ", ".join(sources))