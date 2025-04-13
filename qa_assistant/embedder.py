from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

def store_to_chroma(qa_pairs, persist_dir="chroma_db"):
    documents = [
        Document(page_content=answer.strip(), metadata={"question": question.strip()})
        for question, answer in qa_pairs
        if question and answer
    ]

    if not documents:
        raise ValueError("No valid Q&A documents to store in Chroma.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Chroma.from_documents(
        documents,
        embedding=embeddings,
        persist_directory=persist_dir
    )
    vectorstore.persist()
