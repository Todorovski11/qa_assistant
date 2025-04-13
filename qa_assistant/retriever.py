from langchain_chroma import Chroma
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_huggingface.llms import HuggingFaceEndpoint
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def ask_question(query, persist_dir="chroma_db"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory=persist_dir
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    prompt_template = """
Answer the question using only the information below.
If the answer is not contained, respond with: "I don't know based on the provided information."

Context:
{context}

Question: {question}
Answer:
"""
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=prompt_template,
    )

    llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.1",
        task="text-generation",
        temperature=0.1,
        max_new_tokens=200,
        model_kwargs={}
    )


    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return qa_chain.invoke(query)["result"]

