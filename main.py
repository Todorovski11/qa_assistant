from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from qa_assistant.loader import extract_qa_from_docx
from qa_assistant.embedder import store_to_chroma
from qa_assistant.retriever import ask_question
from qa_assistant.config import load_env

load_env()

app = FastAPI()

# Allow frontend (e.g. React at localhost:5173) to access this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domain in production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optional: Load Q&A data on API start (or trigger manually)
@app.on_event("startup")
def load_qa_data():
    qa_pairs = extract_qa_from_docx("docs/sample.docx")
    if not qa_pairs:
        print("No Q&A found. Please check your .docx format.")
        return
    print(f"Extracted {len(qa_pairs)} Q&A pairs")
    store_to_chroma(qa_pairs)

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    query = data.get("query", "")
    if not query:
        return {"result": "Please provide a question."}
    
    response = ask_question(query)
    return {"result": response}
