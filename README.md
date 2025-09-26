# miq-agentic-ai

A hands-on training repo for LangChain, RAG, and Agentic AI patterns. It includes notebooks, small scripts, and sample datasets to explore document loading, chunking, retrieval, SQL/CSV agents, and simple UIs.

## Project Structure

- `requirements.txt`: Python dependencies for the training environment.
- `0-lc-basics/`: Intro LangChain notebooks and exercises.
  - `1-lc-demo.ipynb` .. `11-lc-demo.ipynb`: Step-by-step LC demos.
  - `001-exercise.txt`, `analysis.md`: Prompts and notes.
- `1.0-lc-intermediate/`: Intermediate topics, e.g., SQL agents.
  - `1-sql-agents.ipynb`, `chinook.db`: Use an SQLite DB from a notebook.
- `1.1-rag-basics/`: RAG fundamentals.
  - `1-document-loaders.ipynb`, `2-text-splitters.ipynb`, `3-retriever.ipynb`.
  - Small sample texts: `when.txt`, `work.txt`.
- `1.2-rag/`: Scripts for a minimal RAG pipeline and UI.
  - `0-data-ingestion.py`: Ingest and embed docs.
  - `1-test-retrieval.py`: Sanity-check retrieval.
  - `3-ui.py`: Simple UI to query the index.
- `2-agents/`: Agent notebooks and scripts.
  - `agentic-rag.ipynb`: Agentic RAG examples.
  - `csv-agents.py`: CSV agent script.
- `lc-training-data/`: Datasets for labs and demos.
  - `chinook.db` and `Chinook_Sqlite.sql` (sample music DB)
  - CSVs (`movies.csv`, `hr-employees-attritions-internet.csv`, etc.)
  - PDFs under `rag-docs/` and `ai-agents-data/` used by RAG/agents.
- `env/`: Local Python virtual environment (Windows). Contains `Scripts/python.exe`.

## Quickstart (Windows CMD)

1) Create/activate a virtual env (if not using the provided `env/`):

```cmd
py -3.11 -m venv env
env\Scripts\activate
```

2) Install dependencies:

```cmd
pip install -r requirements.txt
```

3) Run a demo script (examples):

- Data ingestion for RAG
```cmd
python 1.2-rag\0-data-ingestion.py
```

- Test retrieval
```cmd
python 1.2-rag\1-test-retrieval.py
```

- Launch the simple UI
```cmd
python 1.2-rag\3-ui.py
```

4) Explore notebooks: open the `.ipynb` files in VS Code and run cells.

## Notes

- Some notebooks and scripts expect API keys (e.g., OpenAI) in env vars. If needed, set them before running:

```cmd
set OPENAI_API_KEY=your_key_here
```

- The `env/` folder is included for convenience on this machine; you can delete and recreate it as needed.

## License

This project is licensed under the MIT License — see `LICENSE` for details.