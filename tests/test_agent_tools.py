from app.agents.rag_agent import agent


def run_test(test_name, question, customer_age=None, loan_tenure=None):

    print("\n" + "=" * 60)
    print(test_name)
    print("=" * 60)

    input_data = {
        "question": question,
        "answer": "",
        "decision": "",
        "reason": "",
        "policy_reference": [],
        "messages": []
    }

    if customer_age is not None:
        input_data["customer_age"] = customer_age

    if loan_tenure is not None:
        input_data["loan_tenure"] = loan_tenure


    response = agent.invoke(
        input_data,
        config={
            "configurable": {
                "thread_id": test_name
            }
        }
    )


    print("\nFINAL RESPONSE:")
    print(response)


# --------------------------------------------------
# TEST 1
# Eligibility Tool
# --------------------------------------------------

run_test(
    test_name="TEST 1 - Loan Eligibility Check",
    question="Can I get a 20 year home loan? My age is 60",
    customer_age=60,
    loan_tenure=20
)


# --------------------------------------------------
# TEST 2
# EMI Tool
# --------------------------------------------------

run_test(
    test_name="TEST 2 - EMI Calculation",
    question="""
Calculate EMI for a home loan.

Loan amount: 500000
Interest rate: 6%
Loan tenure: 20 years
"""
)


# --------------------------------------------------
# TEST 3
# Eligibility + EMI Combined
# --------------------------------------------------

run_test(
    test_name="TEST 3 - Eligibility and EMI Combined",
    question="""
I am 55 years old.

Can I get a 15 year home loan?

Loan amount is 500000.
Interest rate is 6%.

Also calculate my EMI.
""",
    customer_age=55,
    loan_tenure=15
) 