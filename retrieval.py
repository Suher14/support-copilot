import os
import numpy as np
from openai import AzureOpenAI
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
from documents import documents

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version="2024-10-21",
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),
)

embedding_model = "text-embedding-ada-002"

# Build a simple in-memory vector store (document embeddings)
vector_store = []


def get_embedding(text: str) -> np.ndarray:
    response = client.embeddings.create(
        input=[text],
        model=embedding_model,
    )
    return np.array(response.data[0].embedding)


def build_vector_store():
    global vector_store
    vector_store = [
        {
            "name": doc["name"],
            "content": doc["content"],
            "embedding": get_embedding(doc["content"]),
        }
        for doc in documents
    ]


def retrieve_documents(query: str, k: int = 3):
    if not vector_store:
        build_vector_store()

    query_embedding = get_embedding(query)

    similarities = [
        (cosine_similarity([query_embedding], [doc["embedding"]])[0][0], doc)
        for doc in vector_store
    ]

    similarities.sort(reverse=True, key=lambda x: x[0])

    return [doc for _, doc in similarities[:k]]

if __name__ == "__main__":
    query = "I was charged but my subscription is still inactive"

    results = retrieve_documents(query)

    print("Top retrieved documents:\n")

    for doc in results:
        print(doc["name"])