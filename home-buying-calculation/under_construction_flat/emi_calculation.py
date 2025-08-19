from tabulate import tabulate

def calculate_loan_emi():
    # User input for loan amount and tenure with default values
    try:
        loan_amount = float(input("Enter the loan amount (default: ₹11,970,000): ") or 11970000)
        loan_tenure_years = int(input("Enter the loan tenure in years (default: 10): ") or 10)
    except ValueError:
        print("Invalid input. Using default values.")
        loan_amount = 11970000
        loan_tenure_years = 10

    # Default rate of interest
    rate_of_interest = 8.6  # Default rate of interest: 8.6%
    
    # Convert interest rate to monthly rate and tenure to months
    monthly_interest_rate = rate_of_interest / 12 / 100
    loan_tenure_months = loan_tenure_years * 12
    
    # Calculate EMI using the formula: EMI = P * r * (1+r)^n / ((1+r)^n - 1)
    emi = loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**loan_tenure_months / ((1 + monthly_interest_rate)**loan_tenure_months - 1)
    emi = round(emi, 0)  # Round off EMI for display
    
    # Prepare data for tabular display
    table_data = []
    total_principal = 0
    total_interest = 0
    total_emi = 0
    
    # Print loan details
    print("\n" + "="*60)
    print(f"{'Loan EMI Breakdown':^60}")
    print("="*60)
    print(f"Loan Amount: ₹{loan_amount:,.0f}")
    print(f"Rate of Interest (Annual): {rate_of_interest}%")
    print(f"Loan Tenure: {loan_tenure_years} years ({loan_tenure_months} months)")
    print(f"Monthly EMI: ₹{emi:,.0f}")
    print("="*60)
    
    # Loop through each month to calculate and display the EMI components
    outstanding_principal = loan_amount
    for month in range(1, loan_tenure_months + 1):
        interest_payment = outstanding_principal * monthly_interest_rate
        principal_payment = emi - interest_payment
        outstanding_principal -= principal_payment
        
        # Round off values
        interest_payment = round(interest_payment, 0)
        principal_payment = round(principal_payment, 0)
        outstanding_principal = round(outstanding_principal, 0)
        
        # Accumulate totals
        total_principal += principal_payment
        total_interest += interest_payment
        total_emi += emi
        
        # Append month data to table
        table_data.append([month, emi, principal_payment, interest_payment, outstanding_principal])
    
    # Append totals as the last row
    table_data.append(["Total", total_emi, total_principal, total_interest, "N/A"])
    
    # Print the EMI breakdown in tabular form with totals
    headers = ['Month', 'EMI', 'Principal Payment', 'Interest Payment', 'Outstanding Principal']
    print(tabulate(table_data, headers, tablefmt="fancy_grid", floatfmt=(".0f", ".0f", ".0f", ".0f", ".0f")))
    print("="*60)

# Call the function to calculate EMI and breakdown
calculate_loan_emi()
