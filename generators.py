# Python program to illustrate for loop in the generator function
def odd_num(start, end):
    for i in range(start, end + 1):
        if i % 2 != 0:
            yield (i)


print(odd_num)

# print("Odd numbers are:")
# # Using for loop
# for num in odd_num(1, 10):
#     print(num)
