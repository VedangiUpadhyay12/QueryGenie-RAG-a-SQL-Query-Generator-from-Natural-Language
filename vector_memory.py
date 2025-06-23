from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import json
import os
from langchain.docstore import InMemoryDocstore
from langchain.embeddings.base import Embeddings
from langchain.vectorstores.base import VectorStore
from langchain.schema import Document

def get_vectorstore(past_query_file):
    with open(past_query_file, 'r') as f:
        past_queries = json.load(f)

    texts = [item["query"] + " → " + item["sql"] for item in past_queries]
    embeddings = OpenAIEmbeddings()
    vectordb = FAISS.from_texts(texts, embeddings)
    return vectordb
