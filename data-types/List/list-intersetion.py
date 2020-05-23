a = [2,3,5,2,4,5]
b = [2,3,4,1,4,6]
c = []
print a
for i in a:
    print i
    if i in b:
        if i not in c:
            c.append(i)
print c
