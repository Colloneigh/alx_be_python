#prompt the user to input their monthly income
monthly_income = int(input("Enter your monthly income:"))
#prompth the user to input their monthly expenses
monthly_expenses =int(input("Enter your monthly expenses:"))
#calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses
#projected annual savings
annual_interest_rate = 0.05
projected_savings = monthly_savings * 12 + monthly_savings * 12 * annual_interest_rate
print(f"Your monthly savings is: {monthly_savings}")
print(f"Your projected savings after one year with interest is: {projected_savings}")
