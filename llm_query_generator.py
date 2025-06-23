from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
import os

load_dotenv()

def generate_sql(nl_query, schema, vectordb):
    prompt_template = PromptTemplate(
        input_variables=["question", "schema"],
        template="""
Given this SQL table schema:
{schema}

And this natural language question:
{question}

Generate the correct SQL query using standard SQL.
"""
    )

    prompt = prompt_template.format(question=nl_query, schema=schema)
    retriever = vectordb.as_retriever()
    docs = retriever.get_relevant_documents(nl_query)

    context = "\n".join([d.page_content for d in docs])

    llm = OpenAI(temperature=0)
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = chain.run(prompt + "\nContext:\n" + context)
    return response.strip()
