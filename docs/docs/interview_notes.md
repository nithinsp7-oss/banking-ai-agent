# Banking AI Agent - Interview Notes

## Project Overview

AI-powered mortgage banking assistant built using RAG, LangGraph, FastAPI and LLM tool calling.

The system helps customers with:
- Home loan eligibility checks
- EMI calculations
- Policy based mortgage questions


## Architecture

User Query

↓

FastAPI API Layer

↓

LangGraph Agent

↓

Tool Calling + RAG Retrieval

↓

Ollama Mistral LLM

↓

Final Response


## RAG Implementation

Mortgage policy documents are converted into embeddings and stored in FAISS vector database.

Flow:

Document
→ Chunking
→ Embeddings
→ FAISS Vector Store
→ Similarity Search
→ LLM Context


## Agent Tools


### Eligibility Tool

Input:

- Customer age
- Requested loan tenure


Logic:

Maturity Age = Customer Age + Loan Tenure


Checks against maximum allowed maturity age.


### EMI Calculator

Input:

- Loan amount
- Interest rate
- Tenure


Output:

Monthly EMI calculation


## Technology Stack

Python

FastAPI

LangGraph

LangChain

Ollama

Mistral LLM

FAISS

Sentence Transformers

SQLite Memory


## Key Interview Points

### Why RAG?

RAG reduces hallucination by grounding responses using company policy documents.


### Why LangGraph?

LangGraph helps create controlled agent workflows with:

- State management
- Tool execution
- Memory
- Multi-step reasoning


### Production Improvements

Future enhancements:

- Authentication
- Cloud deployment
- Monitoring
- Logging
- Better evaluation metrics
- CI/CD pipeline