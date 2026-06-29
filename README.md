# Banking AI Agent - Mortgage Assistant using RAG and LangGraph

An Agentic AI-powered mortgage assistant that helps answer Australian home loan policy queries using Retrieval-Augmented Generation (RAG), LangGraph workflows, FAISS vector search, and custom financial tools.

The system combines Large Language Models (LLMs) with banking domain knowledge to provide accurate loan eligibility decisions and EMI calculations.

---

# Project Overview

Traditional banking support systems require manual policy lookup and rule checking.

This project demonstrates an AI assistant capable of:

- Understanding customer mortgage questions
- Retrieving relevant banking policy information
- Applying eligibility rules
- Calculating loan EMI
- Producing structured responses

The assistant is designed around an agentic workflow where the LLM can reason and invoke domain-specific tools.

---

# Architecture
                     User
                      |
                      |
                FastAPI API
                      |
                      |
              LangGraph Agent
                      |
    ---------------------------------
    |                               |
    |                               |
RAG Pipeline                  Tool Calling
    |                               |
    |                    -----------------------
    |                    |                     |
 FAISS Vector Store EMI Calculator Eligibility Tool
|
|
Australian Mortgage Policy Documents
                                    |
                      |
                Mistral LLM
                 (Ollama)


---

# Technology Stack

## Artificial Intelligence

- Large Language Models (LLMs)
- Mistral using Ollama
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search

## Agent Framework

- LangChain
- LangGraph
- Tool Calling
- Agent Workflow Orchestration

## Backend

- FastAPI
- Python
- Pydantic

## Vector Database

- FAISS

## Storage

- SQLite
- LangGraph Memory Checkpointing

---

# Key Features

## 1. Retrieval-Augmented Generation (RAG)

The system retrieves relevant mortgage policy information from documents before generating responses.

Flow:
    Question
|
Embedding Model
|
FAISS Similarity Search
|
Relevant Policy Context
|
LLM Response Generation


---

## 2. Loan Eligibility Tool

The agent validates:

- Customer age
- Requested loan tenure
- Maximum maturity age rule

Example:
Customer Age: 60
Loan Tenure: 20 years

Maturity Age:
60 + 20 = 80

Maximum Allowed:
75

Decision:
Not Eligible


---

## 3. EMI Calculator Tool

The assistant can calculate monthly EMI.

Example:
Loan Amount:
500000

Interest Rate:
6%

Tenure:
20 years

Monthly EMI:
3582.16


---

# LangGraph Agent Workflow
START

|
|
Agent Node
|
|
Tool Execution
|
|
Response Processing
|
|
END


The workflow allows:

- LLM reasoning
- Tool selection
- Structured output generation
- Stateful conversations

---

# API Example

## Request

```json
{
 "question":"I am 55 years old. Can I get a 15 year home loan?",
 "customer_age":55,
 "loan_tenure":15
}

Response
{
 "decision":"Eligible",
 "reason":"Customer age plus tenure equals maturity age 70 years, which is within the allowed limit.",
 "policy_reference":[
    "Customer Age Eligibility",
    "Maximum Loan Tenure"
 ],
 "emi":4219.28
}

banking-ai-agent/

├── app/
│   ├── agents/
│   │   └── rag_agent.py
│   |
│   ├── api/
│   │   └── routes.py
│   |
│   ├── rag/
│   │   ├── retriever.py
│   │   ├── loader.py
│   │   └── vector_store.py
│   |
│   ├── tools/
│       ├── eligibility_tool.py
│       └── emi_tool.py
|
├── documents/
│   └── home_loan_policy.md
|
├── tests/
|
├── requirements.txt
└── main.py

Running the Application

Install dependencies:
Bash
pip install -r requirements.txt

Start Ollama:
Bash
ollama run mistral

Run API:
Bash
uvicorn main:app --reload

Swagger documentation:

http://localhost:8000/docs

Future Improvements
Docker containerization
Cloud deployment
CI/CD pipeline
Authentication layer
Production vector database
Automated evaluation framework
Monitoring and logging

Skills Demonstrated
Python
FastAPI
LangChain
LangGraph
Generative AI
RAG Systems
Vector Databases
LLM Tool Calling
AI Agents
API Development
Banking Domain Automation


