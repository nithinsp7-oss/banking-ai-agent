from app.agents.basic_agent import agent


response = agent.invoke(
    {
        "question":
        """
        Explain the Australian home loan approval process
        from application to settlement.
        """
    }
)


print(response["answer"])