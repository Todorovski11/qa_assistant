from docx import Document

def extract_qa_from_docx(file_path):
    doc = Document(file_path)
    qa_pairs = []

    for table in doc.tables:
        # Skip header row (assumed to be present)
        for row in table.rows[1:]:
            cells = row.cells
            if len(cells) >= 3:
                question = cells[1].text.strip()
                answer = cells[2].text.strip()
                if question and answer:
                    qa_pairs.append((question, answer))

    return qa_pairs

