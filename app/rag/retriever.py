from app.rag.vector_store import create_vector_store


vector_store = create_vector_store()


def retrieve_context(question):

    results = vector_store.similarity_search(
        question,
        k=3
    )

    context = "\n\n".join(
        doc.page_content
        for doc in results
    )

    return context