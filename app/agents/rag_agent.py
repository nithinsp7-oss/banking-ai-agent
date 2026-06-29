from typing import TypedDict, Annotated

from langgraph.graph import StateGraph, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

from app.database.memory import get_memory

from app.tools.emi_tool import emi_calculator
from app.tools.eligibility_tool import check_home_loan_eligibility


# ==============================
# STATE
# ==============================

class AgentState(TypedDict):

    question: str

    answer: str

    customer_age: int
    loan_tenure: int

    decision: str
    reason: str

    policy_reference: list[str]

    emi: float | None

    messages: Annotated[list, add_messages]



# ==============================
# LLM
# ==============================


llm = ChatOllama(
    model="mistral",
    temperature=0
)



tools = [
    emi_calculator,
    check_home_loan_eligibility
]


llm_with_tools = llm.bind_tools(tools)


tool_node = ToolNode(tools)



# ==============================
# AGENT NODE
# ==============================


def agent_node(state):


    response = llm_with_tools.invoke(
        [
            HumanMessage(
                content=state["question"]
            )
        ]
    )


    return {
        "messages":[response]
    }




# ==============================
# RESPONSE PROCESSOR
# ==============================


def response_node(state):


    messages = state["messages"]


    decision = ""
    reason = ""

    policy_reference=[]

    emi=None



    for message in messages:


        if message.type == "tool":


            import json


            result=json.loads(
                message.content
            )



            # Eligibility tool

            if "maximum_allowed_maturity_age" in result:


                if result["eligible"]:

                    decision="Eligible"


                    reason=result["message"]



                else:

                    decision="Not Eligible"


                    reason=result["message"]



                policy_reference=[
                    "Customer Age Eligibility",
                    "Maximum Loan Tenure"
                ]



            # EMI tool

            if "monthly_emi" in result:


                if decision=="Eligible":

                    emi=result["monthly_emi"]



    return {


        "answer":"Response generated successfully.",

        "decision":decision,

        "reason":reason,

        "policy_reference":
            list(set(policy_reference)),

        "emi":emi

    }




# ==============================
# WORKFLOW
# ==============================


workflow=StateGraph(
    AgentState
)



workflow.add_node(
    "agent",
    agent_node
)



workflow.add_node(
    "tools",
    tool_node
)



workflow.add_node(
    "response",
    response_node
)



workflow.set_entry_point(
    "agent"
)



workflow.add_edge(
    "agent",
    "tools"
)



workflow.add_edge(
    "tools",
    "response"
)



workflow.add_edge(
    "response",
    END
)



memory=get_memory()



agent=workflow.compile(
    checkpointer=memory
)