from pathlib import Path
from langchain_community.document_loaders import TextLoader


def load_documents():

    documents = []

    folder = Path("documents")

    for file in folder.glob("*.txt"):
        loader = TextLoader(str(file))
        documents.extend(loader.load())

    return documents