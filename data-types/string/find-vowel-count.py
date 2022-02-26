# Python Program to Count the Number of Vowels in a String

l = 'Hello worldeeE'
vowels = ['a', 'e', 'i', 'o', 'u']
c = 0
for i in l:
    if i in vowels:
        c = c + 1
print(c)
