
number_list = [1,2,3]


for n, i in enumerate(number_list):
    print()
    if i > 50:
        print(f"Greater Numbers: {i} with index {n}, new list-{[len(number_list)]}-| {number_list}")
        number_list.remove(i)
        print(f"Removed Greater Numbers- {i}, iteration: {n} new list-{[len(number_list)]}-| {number_list}")

