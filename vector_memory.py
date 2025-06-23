from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import json
import os

def get_vectorstore(past_query_file):
    with open(past_query_file, 'r') as f:
        past_queries = json.load(f)

    texts = [item["query"] + " → " + item["sql"] for item in past_queries]
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_texts(texts, embeddings)
    return vectordb
