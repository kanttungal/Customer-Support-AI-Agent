from database.vectorstore import get_retriever

retriever = get_retriever()

def search_documents(query:str):

    docs = retriever.invoke(query)

    return docs



