# Python Program to sort a list according to the length of the elements
a = ['Apple', 'Ball', 'Cat', 'Ox']
for i in range(len(a)):
    for j in range(len(a) - i - 1):
        if len(a[j]) > len(a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]
print(a[-1])
