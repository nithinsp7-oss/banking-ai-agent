from app.tools.emi_calculator import calculate_emi


result = calculate_emi(
    500000,
    6,
    25
)

print(result)