from langchain_core.tools import tool


@tool
def check_home_loan_eligibility(
    customer_age: int,
    requested_tenure: int
):
    """
    Checks home loan age eligibility.

    Maximum age at loan maturity should not exceed 75 years.
    """

    maturity_age = customer_age + requested_tenure


    if maturity_age <= 75:
        return {
    "eligible": True,
    "customer_age": customer_age,
    "requested_tenure": requested_tenure,
    "maturity_age": maturity_age,
    "maximum_allowed_maturity_age": 75,
    "message": 
    f"Customer is eligible. "
    f"Maturity age is {maturity_age} years. "
    f"Maximum allowed maturity age is 75 years."
}

    else:
        return {
    "eligible": False,
    "customer_age": customer_age,
    "requested_tenure": requested_tenure,
    "maturity_age": maturity_age,
    "maximum_allowed_maturity_age": 75,
    "message":
    f"Customer is not eligible. "
    f"Maturity age is {maturity_age} years, "
    f"which exceeds the maximum allowed maturity age of 75 years."
}