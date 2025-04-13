from qa_assistant.loader import extract_qa_from_docx
from qa_assistant.embedder import store_to_chroma
from qa_assistant.retriever import ask_question
from qa_assistant.config import load_env

load_env()

qa_pairs = extract_qa_from_docx("docs/sample.docx")
print(f"\nExtracted {len(qa_pairs)} Q&A pairs")
if not qa_pairs:
    print("No Q&A found. Please check your .docx format.")
    exit()

store_to_chroma(qa_pairs)

print("\nAsk a question (type 'exit' to quit):")
while True:
    query = input("> ")
    if query.lower() == "exit":
        break
    print("\nAnswer:", ask_question(query))
