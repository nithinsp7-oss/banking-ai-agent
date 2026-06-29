from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from app.rag.loader import load_documents


VECTOR_DB_PATH = "vectorstore"


def get_embeddings():

    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )


def create_vector_store():

    embeddings = get_embeddings()


    if Path(VECTOR_DB_PATH).joinpath("index.faiss").exists():

        print("Loading existing FAISS database...")

        vector_store = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

        return vector_store



    print("Creating new FAISS database...")


    documents = load_documents()


    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )


    chunks = splitter.split_documents(
        documents
    )


    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )


    vector_store.save_local(
        VECTOR_DB_PATH
    )


    return vector_store