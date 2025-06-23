from langchain.chains import RetrievalQA
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# ✅ 1. Load environment variables
load_dotenv()

# ✅ 2. Fetch API key from .env or Streamlit Cloud Secrets
openai_api_key = os.getenv("OPENAI_API_KEY")

# ✅ 3. Function to generate SQL using LLM + RAG
def generate_sql(nl_query, schema, vectordb):
    # Prompt for SQL generation
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

    # Retrieve relevant past examples from vector memory
    retriever = vectordb.as_retriever()
    docs = retriever.get_relevant_documents(nl_query)
    context = "\n".join([d.page_content for d in docs])

    # ✅ 4. Initialize the LLM with your API key
    llm = OpenAI(openai_api_key=openai_api_key, temperature=0)

    # ✅ 5. Create RAG-based QA chain and run
    chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    response = chain.run(prompt + "\nContext:\n" + context)

    return response.strip()
