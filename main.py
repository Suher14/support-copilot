from rag_pipeline import rag_pipeline
from guardrails import check_guardrails

BANNER = """
===============================
  Customer Support Copilot (RAG)
===============================
Type 'exit' to quit.
"""

def main():
    print(BANNER)

    # Lägg den här
    print("Ask a support question about billing, login, subscriptions, or security.\n")

    while True:
        query = input("You > ").strip()

        if query.lower() == "exit":
            print("Assistant > Goodbye!")
            break

        guardrail_response = check_guardrails(query)
        if guardrail_response:
            print("\nAssistant >", guardrail_response)
            print()
            continue

        answer, sources = rag_pipeline(query)

        print("\nAssistant >")
        print(answer)
        print("\nSources   >", ", ".join(sources))
        print("-" * 31)
        print()


if __name__ == "__main__":
    main()