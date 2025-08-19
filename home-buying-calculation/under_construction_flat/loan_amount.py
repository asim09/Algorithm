def calculate_home_loan():
    # Input details from user
    carpet_area = float(input("Enter the carpet area of the flat (in sq. ft): "))
    price_per_sqft = float(input("Enter the price per square foot (₹): "))
    stamp_duty_rate = 5  # Stamp duty rate (5%)
    max_loan_percentage = 95  # Max loan percentage (95%)

    # Parking charges (assumed default if not provided)
    parking_cost = input("Enter the parking cost (default ₹10,00,000): ")
    parking_cost = float(parking_cost) if parking_cost.strip() else 1000000  # ₹10 Lakh

    # Calculate basic cost of the flat (excluding GST, possession, and other charges)
    basic_cost = carpet_area * price_per_sqft

    # Calculate stamp duty
    stamp_duty = basic_cost * (stamp_duty_rate / 100)

    # Calculate total flat cost (basic cost + stamp duty + parking)
    total_flat_cost = basic_cost + stamp_duty + parking_cost

    # Calculate max home loan amount (95% of basic cost + stamp duty)
    max_loan_amount = (basic_cost + stamp_duty) * (max_loan_percentage / 100)

    # Display the results
    print("\n--- Cost Breakdown ---")
    print(f"Basic cost (carpet area * price per sq. ft): ₹{basic_cost:,.2f}")
    print(f"Stamp duty ({stamp_duty_rate}%): ₹{stamp_duty:,.2f}")
    print(f"Parking cost (excluded from home loan): ₹{parking_cost:,.2f}")
    print(f"\nTotal flat cost (basic + stamp duty + parking): ₹{total_flat_cost:,.2f}")
    print(f"Maximum home loan sanctioned (95% of basic cost + stamp duty): ₹{max_loan_amount:,.2f}")

# Call the function to calculate home loan
calculate_home_loan()
