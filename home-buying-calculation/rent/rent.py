from pprint import pprint

def rent_paid_in_given_years():
    initial_rent = 72000*12
    roi = 3.5
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

print(rent_paid_in_given_years())