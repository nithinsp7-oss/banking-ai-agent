# Banking AI Agent - Home Loan Assistant

An AI-powered mortgage banking assistant built using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), LangGraph agents, and FastAPI.

The system helps customers evaluate home loan eligibility based on lending policies and calculate estimated EMI using AI-powered tool calling.

---

# Project Overview

Traditional banking assistants rely on predefined rules and limited responses.

This project demonstrates a modern AI banking assistant capable of:

- Understanding natural language customer queries
- Retrieving relevant lending policy information using RAG
- Performing eligibility assessment
- Calculating EMI dynamically
- Using LLM agent reasoning with external tools


---

# Architecture

The system follows an agent-based AI architecture:


![Architecture](assets/architecture.png)


---

# Technology Stack

## Artificial Intelligence

- Large Language Model: Mistral (Ollama)
- LangChain
- LangGraph
- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- FAISS Vector Database


## Backend

- Python
- FastAPI
- Pydantic


## Storage

- FAISS Vector Store
- SQLite Memory Checkpoint


## Development

- Git
- GitHub
- Virtual Environment


---

# AI Workflow

Customer Query

↓

LangGraph Agent

↓

Intent Understanding

↓

Tool Selection

↓

RAG Policy Retrieval

↓

Decision Generation

↓

Final Response


---

# Features

## 1. Home Loan Eligibility Assessment

Example:

Customer:

"I am 55 years old. Can I get a 15 year home loan?"

System calculates:

Customer Age + Loan Tenure = Maturity Age

55 + 15 = 70 years


Maximum allowed maturity age:

75 years


Result:

Eligible


---

## 2. EMI Calculation

Example:

Loan Amount:
500000

Interest Rate:
6%

Tenure:
15 years


Generated EMI:

4219.28/month


---

## 3. Combined AI Agent Capability

The agent can perform multiple tasks:

- Check eligibility
- Calculate EMI
- Provide policy references
- Generate structured banking responses


---

# Project Structure

```

banking-ai-agent

├── app
│
├── agents
│   └── rag_agent.py
│
├── api
│   ├── main.py
│   └── routes.py
│
├── rag
│   ├── loader.py
│   ├── retriever.py
│   └── vector_store.py
│
├── tools
│   ├── eligibility_tool.py
│   └── emi_tool.py
│
├── documents
│   └── home_loan_policy.md
│
├── tests
│
├── assets
│   ├── architecture.png
│   └── swagger_response.png
│
├── requirements.txt
└── main.py

````


---

# API Demo

FastAPI Swagger Interface:

![Swagger Response](assets/swagger_response.png)


Example Request:

```json
{
 "question":
 "I am 55 years old. Can I get a 15 year home loan? Loan amount 500000 interest rate 6%"
}
````

Example Response:

```json
{
 "decision": "Eligible",
 "reason": "Customer maturity age is 70 years which is within the allowed limit",
 "policy_reference": [
   "Customer Age Eligibility",
   "Maximum Loan Tenure"
 ],
 "emi":4219.28
}
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/nithinsp7-oss/banking-ai-agent.git
```

Create environment:

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python main.py
```

---

# Running Tests

```bash
python tests/test_agent_tools.py
```

---

# Future Improvements

Possible production enhancements:

* Add authentication layer
* Deploy using Docker
* Add cloud LLM support
* Add monitoring and logging
* Add customer profile database integration
* Add evaluation framework for RAG accuracy

---

# Skills Demonstrated

* Generative AI
* LLM Application Development
* RAG Systems
* LangGraph Agents
* LangChain Tool Calling
* FastAPI Development
* Vector Databases
* AI Backend Engineering

```
