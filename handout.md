# ChocoBot — A Hands-on RAG Workshop

## Overview

In this workshop, you'll work in teams as AI consultants hired by a real client. Your job: build an internal AI assistant powered by Retrieval-Augmented Generation (RAG).

## The Client

ChocoLux is a premium chocolate manufacturer (~1,800 employees) headquartered in Luxembourg City, Luxembourg. Founded in 2009, they source cocoa from West Africa and Latin America, produce artisanal and commercial chocolate lines, and sell B2B to hotels, airlines, and specialty retailers across Europe.

They have facilities in Luxembourg City (HQ and flagship factory), a second production plant in Lyon, a sourcing office in Lisbon, and a distribution hub in Milan.

## The Problem

ChocoLux has grown fast and the internal documentation hasn't kept up. Policies are spread across a patchwork of documents — the employee handbook, food safety protocols, supplier code of conduct, expense policy, quality control manual, sustainability charter, travel policy, and more.

Employees on the factory floor have different questions than office staff. Sourcing managers need different guidelines than sales reps. Nobody can find anything. HR and compliance spend half their time answering the same questions over and over.

## The Brief

ChocoLux has hired your team to build **ChocoBot** — an internal AI assistant that employees across all locations can use to get fast, reliable answers about company policies.

## Tech Stack

All teams must work with the following packages only:

```
streamlit
chromadb
python-dotenv
mistralai
pymupdf
pandas
```

The following models are allowed:

```
ministral-3b-2512
mistral-embed-2312
```

## Setup

### 1. Clone the repo

```bash
git clone <repo-url>
cd bsb-workshop
```

### 2. Create a virtual environment

Use Python 3.10 – 3.12. Newer versions (3.13+) have compatibility issues with ChromaDB.

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

Your API key will be provided during the workshop.

### 5. Verify everything works

```bash
python chocobot.py
```

If you get a response, you're good to go.

### 6. Launch the app

```bash
streamlit run app.py
```

## The Rules

- All teams work from the same document set.
- You build a RAG pipeline that ingests these documents and answers employee questions.
- Every hour there is a 2-3 minute status meeting with the client.
- At the end of the workshop, all teams will be evaluated against a shared set of test questions covering easy, tricky, and edge-case scenarios.
