# ChocoBot — RAG Workshop

Build an internal AI assistant for ChocoLux using Retrieval-Augmented Generation (RAG).

See `handout.md` for the full brief.

## Prerequisites

- Python 3.10 – 3.12 (3.13+ has compatibility issues with ChromaDB)
- A Mistral API key (provided during the workshop)

## Setup

### 1. Clone the repo

```bash
git clone git@github.com:daniil-kumok/bsb-lecture-rag.git
cd bsb-lecture-rag
```

### 2. Create a virtual environment

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
mistral_api_key=YOUR_API_KEY
mistral_llm_model=ministral-3b-2512
mistral_embedding_model=mistral-embed
```

Replace `YOUR_API_KEY` with the key provided to your team.

## Running

### Chatbot App

```bash
streamlit run app.py
```

This opens a browser with the ChocoBot chat interface.

### Quick test (no UI)

```bash
python chocobot.py
```

## Project Structure

```
├── chocobot.py          # Core chatbot logic (answer_question)
├── ingest.py            # Document ingestion into ChromaDB
├── app.py               # Streamlit chat app
├── docs/                # ChocoLux company documents
├── requirements.txt     # Python dependencies
├── .env                 # API keys (do not commit)
└── handout.md           # Workshop brief
```

## Tech Stack

| Package        | Purpose                    |
|----------------|----------------------------|
| streamlit      | Chat UI                    |
| mistralai      | LLM and embeddings         |
| chromadb       | Vector store for RAG       |
| python-dotenv  | Environment variable mgmt  |
| pymupdf        | PDF parsing                |
| pandas         | Data handling              |

## Allowed Models

- `ministral-3b-2512` — LLM for chat completions
- `mistral-embed-2312` — Embedding model for RAG
