# find the cumulative sum of a list where the ith element is the sum of the first i+1 elements from the original list.

a = [1, 2, 3, 4, 5]
sum = 0
new_list = []
for i in a:
    sum = sum + i
    new_list.append(sum)
print(new_list)
