from langchain_core.tools import tool
from app.tools.emi_calculator import calculate_emi


@tool
def emi_calculator(
    principal: float,
    annual_rate: float,
    years: int
):
    """
    Calculate monthly EMI for a home loan.

    Args:
        principal: Loan amount
        annual_rate: Interest rate percentage
        years: Loan tenure in years
    """

    emi = calculate_emi(
        principal,
        annual_rate,
        years
    )

    return {
        "loan_amount": principal,
        "interest_rate": annual_rate,
        "tenure_years": years,
        "monthly_emi": round(emi, 2)
    }