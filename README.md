# QueryGenie-RAG 

An LLM-powered assistant that translates natural language into SQL queries using schema-aware Retrieval-Augmented Generation (RAG) and memory-based improvement from user corrections.

## 💡 Features
- Natural Language → SQL with OpenAI GPT
- RAG using FAISS on past queries and schema
- SQLite backend + Streamlit frontend
- Memory for improvement

## 🚀 Deployment
1. Add your `.env` with `OPENAI_API_KEY`
2. Install requirements: `pip install -r requirements.txt`
3. Run with: `streamlit run streamlit_app.py`
4. Or deploy to Streamlit Cloud 🚀

## 📦 Sample Question
> Show all users who spent more than ₹10,000 in Delhi

## 📂 Files
- `sample_database.db`: SQLite DB
- `past_queries.json`: Vector memory
- `llm_query_generator.py`: Query generation
