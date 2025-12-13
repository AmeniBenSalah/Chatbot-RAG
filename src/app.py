import chainlit as cl
from rag_core import rag_answer


@cl.on_chat_start
async def start():
    await cl.Message(
        content="🤖 Chatbot RAG local (Ollama + PostgreSQL).\nPosez votre question."
    ).send()


@cl.on_message
async def main(message: cl.Message):
    question = message.content

    answer = rag_answer(question)

    await cl.Message(
        content=answer
    ).send()
