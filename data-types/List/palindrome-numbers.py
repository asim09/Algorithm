# plindrome numbers which are odd and in in range of 200

# Method-1
a = []

for i in range(100,201):
    if str(i) == (str(i)[::-1]) and i %2 !=0:
        a.append(i)
print(a)


# Method-2


l = [x for x in range(100, 201) if str(x) == (str(x)[::-1]) and x % 2 != 0]
print(l)
