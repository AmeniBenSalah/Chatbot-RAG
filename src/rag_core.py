# rag_core.py
import psycopg
import ollama

DB_CONNECTION_STR = "dbname=rag_chatbot user=postgres password=summer2025 host=localhost port=5432"

EMBEDDING_MODEL = "nomic-embed-text"
LLM_MODEL = "llama3.2"


def calculate_embedding(text: str) -> list[float]:
    response = ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=text
    )
    return response["embedding"]


def similar_corpus(query: str, k: int = 3):
    query_embedding = calculate_embedding(query)
    vector_literal = "[" + ",".join(map(str, query_embedding)) + "]"

    with psycopg.connect(DB_CONNECTION_STR) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT corpus, embedding <=> %s::vector AS distance
                FROM embeddings
                ORDER BY distance ASC
                LIMIT %s
                """,
                (vector_literal, k)
            )
            return cur.fetchall()


def rag_answer(question: str) -> str:
    results = similar_corpus(question)

    context = "\n\n".join([r[0] for r in results])

    prompt = f"""
Tu es un assistant d'analyse de documents.

CONTEXTE :
{context}

QUESTION :
{question}

INSTRUCTIONS :
- Réponds uniquement à partir du contexte
- Si plusieurs documents sont concernés, synthétise les informations
- N'ajoute aucune information externe
"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
