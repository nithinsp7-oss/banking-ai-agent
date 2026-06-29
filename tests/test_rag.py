from app.rag.vector_store import create_vector_store


db = create_vector_store()


results = db.similarity_search(
    "What is the maximum loan tenure?"
)


for doc in results:
    print(doc.page_content)