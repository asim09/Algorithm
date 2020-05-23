a = 12

for i in range(2, a):
    if a%i == 0:
        print('Not Prime')
        break
else:
    print('Prime hai')


#MEthod-2

def is_prime(val):
    is_P = True
    if val > 1:
        for num in range(2,val):
            if val % num == 0:
                break
        else:
            is_P = True
            return is_P
    is_P = False
    return is_P
