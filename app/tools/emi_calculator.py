def calculate_emi(
    principal: float,
    annual_rate: float,
    years: int
):

    monthly_rate = annual_rate / (12 * 100)

    months = years * 12


    emi = (
        principal
        * monthly_rate
        * (1 + monthly_rate) ** months
    ) / (
        (1 + monthly_rate) ** months - 1
    )


    return round(emi, 2)