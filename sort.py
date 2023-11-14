from operator import itemgetter

'12. Sort the array as,  1"s and 0"s in a list'
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
result = []


def sort_binary01(arr):
    arr_length = len(arr)
    count = 0
    for i in arr:
        if arr[i] == 0:
            count = count + 1
    for i in range(count):
        arr[i] = 0
    for i in range(count, arr_length):
        print(i)
        arr[i] = 1
    return arr


# print(sort_binary(arr))

"Method: Two pointers"
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]


def sort_binary02(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        while arr[left] == 0 and left < right:
            left = left + 1
        while arr[right] == 1 and left < right:
            right = right - 1
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

    return arr


# print(sort_binary(arr))
# ************************************************************************************************************************************

"2. Sort list of dictionary"

lst = [
    {"name": "Nandini", "age": 20},
    {"name": "Manjeet", "age": 20},
    {"name": "Nikhil", "age": 19},
]


def sort_list_of_dict01(array):
    sorted_list = sorted(lst, key=lambda i: (i["age"], i["name"]))
    return sorted_list


def sort_list_of_dict02(array):
    sorted_list = sorted(lst, key=itemgetter("age", "age"))
    return sorted_list


# print(sort_list_of_dict01(lst))

my_dict01 = {"num6": 6, "num3": 3, "num2": 2, "num4": 4, "num1": 1, "num5": 5}
my_dict02 = {"Ausebio": 120, "Eusebio": 120, "Cruyff": 104, "Pele": 150, "Ronaldo": 132, "Messi": 125}


def sort_dict01(my_dict01):
    sorted_dict = sorted(my_dict01.items(), key=lambda i: i[1])
    return sorted_dict

def sort_dict02(my_dict02):
    sorted_dict = sorted(my_dict02.items(), key=lambda i: (i[1], i[0]))
    return sorted_dict
print(sort_dict02(my_dict02))




# ************************************************************************************************************************************
