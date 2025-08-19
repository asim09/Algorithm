
from pprint import pprint
def rent():
    initial_rent = 72000*12
    roi = 5
    new_rent = 0
    sum = 0
    anuula_rent_list = []
    tenure = 20

    for i in range(tenure):
        anuula_rent_list.append(initial_rent)
        sum = sum + initial_rent
        print(f"Rent for {i + 1} year----> {initial_rent} | Monthly is {initial_rent//12}")
        cal_next_year_rent = initial_rent + (initial_rent*roi*1)//100
        initial_rent = cal_next_year_rent
    print(f"Total rent paid--->{sum}")
    return sum, anuula_rent_list

def buying_opportunity():
    print()
    flat_cost = 22500000
    anuual_emi = 3420000
    total_amount_paid = 34200000
    emi_sum, emi_array  = rent()
    diff_of_annual_emi_and_rent = [anuual_emi - i for i in emi_array]
    for n, annual_saving in enumerate(diff_of_annual_emi_and_rent):
        print(f"Saving on Year {n+1} after paying rent will be -- > {annual_saving}")
    return diff_of_annual_emi_and_rent

# buying_opportunity()

def annual_saving_componding():
    print()
    annual_saving_from_rent = buying_opportunity()
    r = 12
    t = 1
    new_principal = 0
    ts = 0
    for n, i in enumerate(annual_saving_from_rent):
        actual_principal = new_principal + i
        annual_return = actual_principal + (actual_principal*r*t)//100
        print(f"principal amount for year {n+1}--> {actual_principal} and return at the end of year {n+1}--> {annual_return- actual_principal} and amount at the end of year--> {annual_return}")
        new_principal = annual_return
        ts = ts + new_principal
    print(f"Total return at the end of 10th year--{ts}")
    return ts
annual_saving_componding()