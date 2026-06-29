from app.agents.rag_agent import agent


config = {
    "configurable": {
        "thread_id": "customer_001"
    }
}


response = agent.invoke(
    {
        "question": "My age is 55 years",
        "customer_age": 55,
        "loan_tenure": 15
    },
    config
)

print("FIRST RESPONSE")
print(response["answer"])


response = agent.invoke(
    {
        "question": """
        Can I get this home loan?
        """
    },
    config
)

print("\nSECOND RESPONSE")
print(response["answer"]) 