print("hello")

PSF = 25000
CARPET_AREA = 700
GST = 0.05
STAMP_DUTY = 0.06
POSESSION_CHARGES = 500000
LOAN_SANCTION_COMPONENT = 0.95
def carpet_cost():
    return PSF * CARPET_AREA
def gst():
    return carpet_cost() * GST
def stamp_duty():
    print(f'sd cost------> {carpet_cost() * 0.06}')
    return carpet_cost() * 0.06

def flat_cost():
    # flat_cost = PSF * CARPET_AREA
    flat_cost = carpet_cost()
    print(f'carpet area cost is----> {flat_cost}')
    # gst_amount = flat_cost * GST
    gst_amount = gst()
    stamp_amount = flat_cost * STAMP_DUTY + 30000
    total_flat_cost = flat_cost + gst_amount + stamp_amount + POSESSION_CHARGES
    print(f'Final flat cost is----> {total_flat_cost}')
    return total_flat_cost

# print(flat_cost())
def tentative_loan_amount():
    flat_cost()
    basic_flat_cost = carpet_cost()+ gst() + POSESSION_CHARGES
    tentative_loan_sanction_amount = basic_flat_cost * LOAN_SANCTION_COMPONENT
    print(f'tentative_loan_sanction_amount @95% is----> {tentative_loan_sanction_amount}')
    return tentative_loan_sanction_amount

print(tentative_loan_amount())


