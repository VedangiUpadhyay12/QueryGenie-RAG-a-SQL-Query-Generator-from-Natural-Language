import streamlit as st
from schema_loader import get_schema_descriptions
from llm_query_generator import generate_sql
from vector_memory import get_vectorstore
import sqlite3
import pandas as pd
import os

# --- Load
st.title("🧠 QueryGenie-RAG: Natural Language to SQL")
db_path = "sample_database.db"
schema = get_schema_descriptions(db_path)
schema_str = "\n".join([f"{k}: {v}" for k,v in schema.items()])
vectordb = get_vectorstore("past_queries.json")

# --- Input
user_query = st.text_input("Ask your question (in plain English):", placeholder="e.g. Show users who spent more than ₹10,000 in Delhi")

if st.button("Generate SQL"):
    if user_query:
        sql = generate_sql(user_query, schema_str, vectordb)
        st.code(sql, language='sql')

        # --- Run the query
        try:
            conn = sqlite3.connect(db_path)
            df = pd.read_sql_query(sql, conn)
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
