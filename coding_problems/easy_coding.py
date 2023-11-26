data = [
    {
        "eid": 95,
        "weekStartdate": "2021-03-18 12:40:11",
        "workHours": 5.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 95,
        "weekStartdate": "2021-03-19 12:40:11",
        "workHours": 6.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 95,
        "weekStartdate": "2021-03-20 12:40:11",
        "workHours": 7.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 97,
        "weekStartdate": "2021-03-17 12:40:11",
        "workHours": 8.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 97,
        "weekStartdate": "2021-03-21 12:40:11",
        "workHours": 9.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
]
# 1 -
# sort list of dictionary on the basis:
soeted_data = sorted(data, key=lambda x: x["eid"])

# print()
# print(soeted_data)
# print()

"""*****************************************************************************************"""
# 2 - :
# Get size of nay object:

import sys

# Generator comprehension: Memory efficient way:
my_gen = (i for i in range(10000))
# print(sys.getsizeof(my_gen), "bytes")

my_list = [i for i in range(10000)]
# print(sys.getsizeof(my_list), "bytes")

"""*****************************************************************************************"""
# 3- get occurrence of elements in list

from collections import Counter

sample_list = [1, 2, 1, 1, 1, 1, 2, 2, 2, 5, 5, 5, 5, 8, 8, 8, 8, 8, 8]

counter = Counter(sample_list)

# print(counter)

"""*****************************************************************************************"""


final_dict = {}

for sample_data in data:
    if not sample_data["eid"] in final_dict:
        final_dict[sample_data["eid"]] = []
    # temp_data = dict()
    # temp_data["eid"] = sample_data["eid"]
    # temp_data["test1"] = sample_data["test1"]
    # temp_data["test3"] = sample_data["test3"]
    final_dict[sample_data["eid"]].append(sample_data)


# id = 95
# print(final_dict[id]);
for id in final_dict:
    x = dict()
    x["eid"] = id
    x["test1"] = final_dict[id][0]["test"]

# print(json.dumps(final_dict[id], indent=4))

"""*****************************************************************************************"""
# 4- Merge two dictionaries:

d1 = {
    "eid": 98,
    "weekStartdate": "2021-03-17 12:40:11",
    "workHours": 5.0,
    "test1": "No value",
}

d2 = {
    "eid": 95,
    "weekStartdate": "2021-03-17 12:40:11",
    "workHours": 6.0,
    "test2": "No value",
}

merged_dict = {**d1, **d2}  # This unpacks the two dictionary.

d3 = d1.update(d2)  # This will modify the original first dictionary.

li = [i for i in range(10)]


for x in li:
    print(x, end="\n")
    li.remove(x)
print(li)


"""**********************************************************************************************"""
# URL shortening service which can serve both a hash and name as a link
"""
https://goo.gl/maps/zsmfycRruhUni4ZL7
https://goo.gl/maps/asim.khan.bengaluru

"""
"""**********************************************************************************************"""


def is_armstarong_number(value):
    string_number = str(value)
    power = len(string_number)

    sum = 0
    for i in string_number:
        sum = sum + pow(int(i), power)
    if sum == value:
        print(value)


for i in range(50001):
    is_armstarong_number(i)

"""**********************************************************************************************"""


# Find Factorial
def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


print(fac(5))


# method-2


def factorial(number):
    return 1 if number == 1 else factorial(number - 1) * number


print(factorial(5))


"""**********************************************************************************************"""
# Using Generator


def fib_series(n):
    x = 0
    y = 1
    count = 0
    while count < n:
        yield x

        z = x + y
        x = y
        y = z
        count += 1


obj = fib_series(10)


for i in obj:
    print(i)


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


for i in range(10):
    print(recur_fibo(i))

"""***********************************"""
user_name = "Asim Khan"


pwd = "AsimnahK"


def gen_pwd(user_name):
    lst_user_name = user_name.split(" ")
    second_name = lst_user_name[-1]
    second_name = second_name[::-1]
    # print(second_name)
    lst_user_name[1] = second_name
    pwd = "".join(lst_user_name)
    print(pwd)
    return pwd


"""***********************************"""

# Find age abbove the input given


def age_above_input(arr, age):
    age_lst = [x["Age"] for x in arr]
    required_age = list(filter(lambda x: x > age, age_lst))
    final_dict = {x["Name"]: x["Age"] for x in arr if x["Age"] in required_age}
    return final_dict


age = 18

arr = [
    {"Name": "Arun", "Age": 20},
    {"Name": "Babu", "Age": 30},
    {"Name": "Charle", "Age": 15},
    {"Name": "Dinesh", "Age": 18},
]
print(age_above_input(arr, age))

"""**********************************************************"""

grades = ["A", "A", "B", "C", "D", "C", "B", "C", "A", "C", "B"]
output = {"A": 3, "B": 3, "C": 4, "D": 1}
counter = dict()
for grade in grades:
    if grade in counter:
        counter[grade] = counter[grade] + 1
    else:
        counter[grade] = 1

print(counter)
"""**********************************************************"""
dict = {"a": "A", "b": 2, "c": 3, "d": "c"}
result = {"A": 2, "B": 1, "C": 2, "D": 1, 2: 1, 3: 1}
sample_list = list(dict.keys()) + list(dict.values())
resultant_dict = {}
for i in sample_list:
    if isinstance(i, int):
        if i not in resultant_dict.keys():
            resultant_dict[i] = sample_list.count(i)
    else:
        if i.upper() not in resultant_dict.keys():
            count_lower = sample_list.count(i.lower())
            count_upper = sample_list.count(i.upper())
            resultant_dict[i.upper()] = count_lower + count_upper
print(resultant_dict)
"""**********************************************************"""
# count word trarting have same first character.
list = ["hello", "king", "word", "sword", "swear", "hi"]
result = {"h": ["hello", "hi"], "k": ["king"], "w": ["word"], "s": ["sword", "swear"]}
resultant_dict = dict()

for word in list:
    if word[0] not in resultant_dict:
        resultant_dict[word[0]] = []
        resultant_dict[word[0]].append(word)
    else:
        resultant_dict[word[0]].append(word)


for i, j in resultant_dict.items():
    print(i, ":", j)

print(resultant_dict)
"""**********************************************************"""
# Make first letter as key
data = ["apple", "king", "word", "swear", "swear"]
res = {"a": "apple", "k": "king", "w": "word", "s": "swear"}
resultant_dict = dict()

for word in list:
    resultant_dict[word[0]] = word

print(resultant_dict)
"""**********************************************************"""

grades = ["A", "A", "B", "C", "D", "C", "B", "C", "A", "C", "B"]
res = {"A": 3, "B": 3, "C": 4, "D": 1}

counter = dict()
for grade in grades:
    if grade in counter:
        counter[grade] = counter[grade] + 1
    else:
        counter[grade] = 1
print(counter)
"""**********************************************************"""
# Prog - 1: convert two list into dict
keys = ["a", "b", "c"]
values = [1, 2, 3]
d = dict(zip(keys, values))
print(d)
"""**********************************************************"""
# Tuple to dict

# Method-1
t = ((1, "a"), (2, "b"))
l = dict(map(reversed, t))

# Method-2
t = ((1, "a"), (2, "b"))
l = {y: x for x, y in t}


# Method-3
t = ((1, "a"), (2, "b"))
l = dict((y, x) for x, y in t)
"""**********************************************************"""

"""**********************************************************"""
"""**********************************************************"""
"""**********************************************************"""
"""**********************************************************"""
