# AI Customer Support Copilot (RAG)

This project demonstrates a **Retrieval-Augmented Generation (RAG) pipeline** for customer support.

The assistant retrieves relevant internal support documents from a knowledge base and generates grounded responses to help support agents answer common SaaS-related questions.

## Features

- Retrieval-Augmented Generation (RAG)
- Document embeddings
- Cosine similarity retrieval
- Structured support responses
- Security guardrails for sensitive information
- CLI interface for demo

## Architecture

User Question  
↓  
Guardrails Check  
↓  
Document Retrieval (Embeddings + Cosine Similarity)  
↓  
Top 3 Relevant Documents  
↓  
Prompt Construction  
↓  
LLM Response Generation  
↓  
Structured Support Output + Sources

## Project Structure

```
support-copilot/
├── main.py
├── rag_pipeline.py
├── retrieval.py
├── documents.py
├── guardrails.py
├── requirements.txt
└── README.md
```

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the CLI version:

python3 main.py

Run the Streamlit web app:

streamlit run app.py

## Environment Variables

Create a `.env` file with your Azure OpenAI credentials:

AZURE_API_KEY=your_api_key
AZURE_ENDPOINT=your_endpoint
AZURE_DEPLOYMENT=gpt-4.1

## Example Query

I was charged but my subscription is still inactive

Example output includes:

- issue category
- priority
- suggested reply
- troubleshooting steps
- confidence
- document sources

## Demo Queries

Try asking questions like:

- I was charged but my subscription is still inactive
- I can't log in and the password reset email never arrives
- I canceled my subscription but was still billed
- I think my account was hacked
- Can you delete my data under GDPR?