import os
from langchain_openai import OpenAIEmbeddings
embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")

from langchain_chroma import Chroma
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_function)

from langchain_experimental.text_splitter import SemanticChunker
text_splitter = SemanticChunker(OpenAIEmbeddings())

def get_markdown_files(directory: str):
    markdown_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    
    return markdown_files

def split_md_files(files):
    texts=[]
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            text = f.read()
        texts.append(text)
    
    return texts

def vector_store_exists():
    for _, dir, _ in os.walk("chroma_db"):
        if dir == []:
            return(False)
        return(True)

def initialise_vector_store():
    if not os.path.isdir(os.getenv("DIRECTORY")):
        return False
    if not vector_store_exists():
        files= get_markdown_files(os.getenv("DIRECTORY"))
        texts= split_md_files(files)
        docs= text_splitter.create_documents(texts)
        vectorstore.add_documents(documents=docs)
    return True

def retrieve_docs(question: str):
    retrieved_docs = vectorstore.similarity_search(question)
    context=""
    for doc in retrieved_docs:
        context= context + str(doc.page_content) + "\n\n"
    return context
