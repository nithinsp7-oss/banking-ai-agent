from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


# State definition
class AgentState(TypedDict):
    question: str
    answer: str


# Local Mistral model
llm = ChatOllama(
    model="mistral",
    temperature=0
)


# Agent node
def banking_assistant(state: AgentState):

    question = state["question"]

    messages = [
        SystemMessage(
            content="""
You are an expert Australian mortgage banking assistant.

Your responsibilities:
- Explain home loan processes clearly.
- Explain mortgage concepts professionally.
- Use banking terminology.
- Avoid making unsupported assumptions.
- If information is unavailable, say you need the relevant policy document.

Focus areas:
- Home loans
- Mortgage applications
- Customer eligibility
- Lending processes
- Compliance
"""
        ),
        HumanMessage(
            content=question
        )
    ]


    response = llm.invoke(messages)


    return {
        "answer": response.content
    }



# Create LangGraph workflow

workflow = StateGraph(AgentState)


workflow.add_node(
    "banking_assistant",
    banking_assistant
)


workflow.set_entry_point(
    "banking_assistant"
)


workflow.add_edge(
    "banking_assistant",
    END
)


agent = workflow.compile()