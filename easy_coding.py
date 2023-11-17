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
    }
]
# 1 -
# sort list of dictionary on the basis:
soeted_data = sorted(data, key=lambda x: x["eid"])

# print()
# print(soeted_data)
# print()

'''*****************************************************************************************'''
# 2 - :
# Get size of nay object:

import sys

# Generator comprehension: Memory efficient way:
my_gen = (i for i in range(10000))
# print(sys.getsizeof(my_gen), "bytes")

my_list = [i for i in range(10000)]
# print(sys.getsizeof(my_list), "bytes")

'''*****************************************************************************************'''
# 3- get occurrence of elements in list

from collections import Counter

sample_list =[1,2,1,1,1,1,2,2,2,5,5,5,5,8,8,8,8,8,8]

counter = Counter(sample_list)

# print(counter)

'''*****************************************************************************************'''



final_dict = {}

for sample_data in data:
    if not sample_data['eid'] in final_dict:
        final_dict[sample_data['eid']] = []
    # temp_data = dict()
    # temp_data["eid"] = sample_data["eid"]
    # temp_data["test1"] = sample_data["test1"]
    # temp_data["test3"] = sample_data["test3"]
    final_dict[sample_data['eid']].append(sample_data)


# id = 95
# print(final_dict[id]);
for id in final_dict:
    x = dict()
    x['eid'] = id
    x['test1'] = final_dict[id][0]['test']

# print(json.dumps(final_dict[id], indent=4))

'''*****************************************************************************************'''
# 4- Merge two dictionaries:

d1 = {
        "eid": 98,
        "weekStartdate": "2021-03-17 12:40:11",
        "workHours": 5.0,
        "test1": "No value"
    }

d2 = {
        "eid": 95,
        "weekStartdate": "2021-03-17 12:40:11",
        "workHours": 6.0,
        "test2": "No value"
    }

merged_dict = {**d1, **d2}  # This unpacks the two dictionary.

d3 = d1.update(d2)      # This will modify the original first dictionary.

li = [i for i in range(10)]


for x in li:
    print(x, end='\n')
    li.remove(x)
print(li)


'''**********************************************************************************************'''
# URL shortening service which can serve both a hash and name as a link
'''
https://goo.gl/maps/zsmfycRruhUni4ZL7
https://goo.gl/maps/asim.khan.bengaluru

'''
'''**********************************************************************************************'''

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

'''**********************************************************************************************'''
# Find Factorial
def fac(n):
    if n ==1:
        return 1
    print(n, (n-1))
    return n * fac(n - 1)


print(fac(5))


# method-2

def factorial(number):
    return 1 if number == 1 else factorial(number-1) * number


print(factorial(5))


'''**********************************************************************************************'''
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
        count+=1
obj = fib_series(10)


for i in obj:
    print(i)


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return ((recur_fibo(n-1) + recur_fibo(n-2)))

for i in range(10):
    print(recur_fibo(i))

