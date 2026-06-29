from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.rag_agent import agent


router = APIRouter()


class ChatRequest(BaseModel):
    customer_id: str
    message: str
    customer_age: int | None = None
    loan_tenure: int | None = None


class ChatResponse(BaseModel):
    decision: str
    reason: str
    policy_reference: list[str]
    emi: float | None = None 

@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    result = agent.invoke(
        {
            "question": request.message,
            "customer_age": request.customer_age,
            "loan_tenure": request.loan_tenure,
            "answer": "",
            "decision": "",
            "reason": "",
            "policy_reference": [],
            "messages": []
        },
        config={
            "configurable": {
                "thread_id": request.customer_id
            }
        }
    )


    return {
        "decision": result["decision"],
        "reason": result["reason"],
        "policy_reference": result["policy_reference"],
        "emi": result.get("emi")
    } 