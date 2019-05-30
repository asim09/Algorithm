# Qus: Python Program to create a list of of all numbers in a range which are perfect squares and the sum of the digits of the number is less than 10

u = 40
l = 1
d = []
for i in range(l, u):
    if (int(i**0.5))**2 == i:
        camp = 0
        for j in str(i):
            camp = camp + int(j)
        if camp < 10:
            d.append(i)
print(d)


#Mehod-2

u = 40
l = 1
c = []
for i in range(l, u+1):
    if (int(i**0.5))**2 == i and sum(map(int, str(i))) < 10:
        print(i)
        c.append(i)
print(c)



