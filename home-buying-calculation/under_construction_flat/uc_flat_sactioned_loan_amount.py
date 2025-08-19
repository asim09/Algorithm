def calculate_flat_cost():
    # Input details from user
    carpet_area = float(input("Enter the carpet area of the flat (in sq. ft): "))
    price_per_sqft = float(input("Enter the price per square foot (₹): "))
    
    # Set default values
    gst_rate = 5  # 5%
    stamp_duty_rate = 5  # 5%
    other_charges = 50000  # ₹50,000
    max_loan_percentage = 95  # Max loan percentage (95%)
    
    # Parking and possession charges (default values if not provided)
    parking_cost = input("Enter the parking cost (default ₹10,00,000): ")
    parking_cost = float(parking_cost) if parking_cost.strip() else 1000000  # ₹10 Lakh
    
    possession_cost = input("Enter the possession charges (default ₹5,00,000): ")
    possession_cost = float(possession_cost) if possession_cost.strip() else 500000  # ₹5 Lakh

    # Calculate basic cost
    basic_cost = carpet_area * price_per_sqft
    # print('1-----', basic_cost)

    # Calculate GST
    gst = basic_cost * (gst_rate / 100)

    # Calculate stamp duty
    stamp_duty = basic_cost * (stamp_duty_rate / 100)
    # print('2-----', basic_cost + gst + stamp_duty + parking_cost + possession_cost + other_charges)

    # Calculate total cost
    total_cost = basic_cost + gst + stamp_duty + parking_cost + possession_cost + other_charges
    total_flat_cost_for_loan = basic_cost + stamp_duty + parking_cost

    # Calculate max home loan amount (95% of basic cost + stamp duty)
    max_loan_amount = (basic_cost + stamp_duty + parking_cost) * (max_loan_percentage / 100)

    # Display the results
    print("\n--- Cost Breakdown ---")
    print(f"Basic cost (carpet area * price per sq. ft): ₹{basic_cost:,.2f}")
    print(f"GST ({gst_rate}%): ₹{gst:,.2f}")
    print(f"Stamp duty ({stamp_duty_rate}%): ₹{stamp_duty:,.2f}")
    print(f"Parking cost: ₹{parking_cost:,.2f}")
    print(f"Possession charges: ₹{possession_cost:,.2f}")
    print(f"Other charges: ₹{other_charges:,.2f}")
    print(f"\nTotal cost of the flat: ₹{total_cost:,.2f}")
    print(f"\nTotal flat cost (basic + stamp duty + parking): ₹{total_flat_cost_for_loan:,.2f}")
    print(f"Maximum home loan sanctioned (95% of basic cost + stamp duty): ₹{max_loan_amount:,.2f}")

# Call the function to calculate the flat cost
calculate_flat_cost()

















# PSF = 23000
# CARPET_AREA = 700
# GST = 0.05
# STAMP_DUTY = 0.06
# POSESSION_CHARGES = 500000
# LOAN_SANCTION_COMPONENT = 0.95
# PARKING = 1000000
# def carpet_cost(carpet, psf):
#     return carpet* psf
# def gst():
#     return carpet_cost() * GST
# def stamp_duty():
#     print(f'sd cost------> {carpet_cost() * 0.06}')
#     return carpet_cost() * 0.06

# def flat_cost_no_tax(PARKING,  POSESSION_CHARGES):
#     basic_cost  = carpet_cost() + PARKING + POSESSION_CHARGES
#     print(f'basic_cost------> {basic_cost}')
#     return basic_cost

# def taxes():
#     tax = gst() + stamp_duty()
#     print(f'tax------> {tax}')
#     return tax

# def flat_cost_with_taxes():
#     cost  = flat_cost_no_tax() + taxes()
#     print(f'cost------> {cost}')
#     return cost

# def run():
#     carpet = int(input("Enter caret area: "))
#     psf = int(input("Enter PSF: "))
#     only_carpet_cost = carpet_cost(carpet, psf)
#     parking = int(input("Enter Parking: "))
#     posession = int(input("Enter Posession: "))
#     flat_cost_no_tax = flat_cost_no_tax(parking,  posession)
#     flat_cost_with_taxes = flat_cost_with_taxes()
#     return parking
# print(run())