from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from pathlib import Path
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Paths
DOCUMENTS_PATH = "documents"
DB_PATH = "database/faiss_index"

# Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name = "BAAI/bge-small-en-v1.5"
)

# Load All PDFs

def load_documents():

    documents = []

    pdf_files = Path(DOCUMENTS_PATH).glob("*.pdf")

    for pdf in pdf_files:
        loader = PyPDFLoader(str(pdf))
        documents.extend(loader.load())
    return documents

# Create Vector Store

def create_vectorstore():

    print("Loading pdfs...")

    documents = load_documents()

    print(f"Loaded {len(documents)} pages")

    splitter = RecursiveCharacterTextSplitter( 
        chunk_size = 1000,
        chunk_overlap = 200
    )
    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    vectorstore = FAISS.from_documents(
        chunks,
        embedding_model
    )
    vectorstore.save_local(DB_PATH)
    print("FAISS vectorstore created and saved successfully.")

# Load Existing Vector Store
def load_vectorstore():
    return FAISS.load_local(
        DB_PATH,
        embedding_model,
        allow_dangerous_deserialization = True
    )

# Get Retriever
def get_retriever():
    if not os.path.exists(DB_PATH):
        create_vectorstore()
    vectorstore = load_vectorstore()

    retriever = vectorstore.as_retriever(
        search_kwargs = {"k":3}

    )
    return retriever

# Test
if __name__ == "__main__":

    retriever = get_retriever()

    query = "Can I return shoes after 10 days."

    docs = retriever.invoke(query)
    print("\nTop retrieved chunks:\n")

    for i, doc in enumerate(docs,start=1):
        print(f"Chunk{i}")
        print(doc.page_content)
        print()


    








  