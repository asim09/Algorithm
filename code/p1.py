import json
from collections import Counter

## Find longest non repeative sub string

s = 'abcabcbb'

max_len = 0

for i in range(len(s)):
    _map = {}
    _map[s[i]] = 1

    for j in range(i + 1, len(s)):
        if s[j] not in _map.keys():
            _map[s[j]] = 1
        else:
            break
        

    max_len = max(max_len, len(_map))

print(max_len)

'''*****************************************************************************************'''


input ='This is a full code problem'

output = 'sihT si a lluf edoc melborp'

def f(s):
    t = ' '.join(e[::-1] for e in s.split())
    return t

# f(input)



## Prob -1
# Sort in descending order by second element but if values are same then sort on the basis of string(first elemt):

data =[["aaa",30.0],["bac",40.0],["adc",20.0],["aac",20.0],["abc",20.0]]



def arrangement():
    print(id(data))
    lst = len(data)
    swapped = False

    for i in range(lst):
        for j in range(lst-i-1):
            if data[j][1] < data[j+1][1]:
                data[j][1], data[j + 1][1] = data[j + 1][1], data[j][1]
                swapped = True
            elif data[j][1] == data[j + 1][1]:
                if data[j][0] > data[j + 1][0]:
                    data[j][0], data[j + 1][0] = data[j + 1][0], data[j][0]
                    swapped = True
            if not swapped:
                break
            print()

    return data

# print(arrangement())

'''*****************************************************************************************'''
## Prob -2
input = [
        {
            "cell_name": "Living cells",
            "children": [
                {"name": "Events", "value": "7888"},
                {"name": "Parent", "value": "86.7"},
                {"name": "CD38 PE-A Median", "value": "7.1"},
            ]                                
        }
    ]

output =         [                          
        {
            "cell_name": "Living cells",
            "Events": "7888",
            "Parent": "86.7",
            "CD38 PE-A Median": "7.1",
        }
    ]

import json


sample_dict = input[0]
final_dict = dict()
output = list()

for obj in sample_dict:
    if 'children' == obj:
        for k in sample_dict[obj]:
            temp = {}
            temp[k['name']] = k['value']
            final_dict.update(temp)
    else:
        final_dict[obj] = sample_dict[obj]

output.append(final_dict)

# print(json.dumps(output, indent=2))




'''*****************************************************************************************'''

## Prob - 3

# Find Kth largest number:
# Method - 1
def find_nth_largest_num(arr, n):
    '''
    find second largest number
    '''
    n = n - 1
    if len(arr) > 1:
        unique_arr = list(set(arr))
        unique_arr.sort()
        unique_arr.reverse()
        second_lar_num = unique_arr[n]
        return second_lar_num
    return None


'''*****************************************************************************************'''

## Prob - 4

'''

Rover Problem - Simplified

- There are 4 directions North, East, South and West.
- Assume the Rover is facing a particular direction. Eg: North
- The rover can spin around without moving from it's place by receiving a command sequence.
- The command sequence can contain the combination of 'L' and 'R' which means to spin to Left or Right respectively.
- Given the initial direction the rover is facing and a command sequence, determine the current direction that the
rover will be facing at the end of sequence.


Sample Input:
-------------
initial direction: N
command sequence: LLLLL

Output:
-------
W
'''

# Method - 1

def check_direction(path):
    N = 0
    E = 1
    S = 2
    W = 3
    dir = N
    for i in range(len(path)):
        move = path[i]
        if move == 'R':
            dir = (dir + 1) % 4
        elif move == 'L':
            dir = (4 + dir - 1) % 4

    return dir



dir_dict = {
    "L_to_N": "W",
    "R_to_N": "E",
    "L_to_W": "S",
    "R_to_W": "N",
    "L_to_E": "N",
    "R_to_E": "S",
    "L_to_S": "W",
    "R_to_S": "E",
}

# Method - 2

def calculate_direction(sequence_arr, initial_position):
    direction = ['N','E','S','W']
    spins = ['L', 'R']
    if len(sequence_arr) > 0 and initial_position in direction:
        for comm in sequence_arr:
            key = f'{comm}_to_{initial_position}'
            initial_position = dir_dict.get(key, None)
        return initial_position
    return 'flash msg'


command_sequence = 'LLLLR'
initial_position = 'N'
direction = ['N','E','S','W']

'''*****************************************************************************************'''

## Prob - 5
# Find the second largest value, considering case of redundant values as well.
input = d = {
    'Satish':1,
    'A':2,
    'B':2,
    'D':3
}
def get_sec_highest_sal(dic):
    lst_val = list(d.values())
    sorted_lst = sorted(lst_val, reverse=True)
    sec_highest = sorted_lst[1]
    obj1 = {obj:d[obj] for obj  in d if d[obj] == sec_highest}
    return set(obj1)

# k = dict(sorted(d.items(), key=lambda x: x[1]))
# l = list(k.values())

# d = {'a': 10, 'b': 20, 'c': 30,'d':20}
# k = sorted(d.values(), reverse=True)

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



final_dict = {}

for sample_data in data:
    if not sample_data['eid'] in final_dict:
        final_dict[sample_data['eid']] = []
    final_dict[sample_data['eid']].append(sample_data)

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
# print(id(d1))
# print(id(d2))
# print(id(merged_dict))
# print(merged_dict)

d3 = d1.update(d2)      # This will modify the original first dictionary.

# print(id(d3))
# print(d3)


'''*****************************************************************************************'''


array = [1,23,654,9870]
output = [1,2,3,6,5,4,9,8,7,0]

# Method - 1
def split_integers(input):
    l = []
    n = 0
    while n < len(array):
        if len(str(array[n])) > 1:
            [l.append(int(i)) for i in str(array[n])]
        else:
            l.append(int(array[n]))
        n += 1
    return l
print(split_integers(array))


# Method -2
def split_integers(input):
    l = []
    n = 0
    while n < len(array):
        [l.append(int(i)) for i in str(array[n])] if len(str(array[n])) > 1 else l.append(int(array[n]))
        n += 1
    return l
print(split_integers(array))




# Method -3
resultant_array = list()
for obj in array:
    str_ele = str(obj)
    element_length = len(str_ele)

    while element_length > 0:
        for x in str_ele:
            resultant_array.append(int(x))
            element_length -= 1
# print(resultant_array)

'''*****************************************************************************************'''

sample_string = 'hello mr we are here hello you'
output = {'hello': 2, 'mr': 1, 'we': 1, 'are': 1, 'here': 1, 'you': 1}

# Method -1  
def count_word_occurence(input_str):
    return(dict(Counter(sample_string.split(' '))))



# Method -2
def count_word_occurence(input_str):
    arr_list = sample_string.split(' ')
    resultant_dict = {}
    for ele in arr_list:
        if ele in resultant_dict.keys():
            resultant_dict[ele] = resultant_dict[ele] + 1
        else:
            resultant_dict[ele] = 1
    return resultant_dict

print(count_word_occurence(sample_string))
# arr_list = sample_string.split(' ')


'''*****************************************************************************************'''

input = {'a':'A', 'b':2, 'c':3, 'd':'c'}
output = {'A': 2, 'B': 1, 'C': 2, 'D': 1, 2: 1, 3: 1}

# Method - 1
def get_occurence_of_each_element(input):
    sample_list = list(input.keys()) + list(input.values())
    for n, i in enumerate(sample_list):
        if isinstance(i, str):
            sample_list[n]= i.upper()
    return dict(Counter(sample_list))

print(get_occurence_of_each_element(input))


# Method - 2
def get_occurence_of_each_element(input):
    sample_list = list(input.keys()) + list(input.values())
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

    return resultant_dict
print(get_occurence_of_each_element(input))



'''**********************************************************************************'''


list = ['hello', 'king', 'word', 'sword','swear', 'hi']
resultant_dict = dict()

for word in list:
    if word[0] not in resultant_dict:
        resultant_dict[word[0]] = []
        resultant_dict[word[0]].append(word)
    else:
        resultant_dict[word[0]].append(word)


for i, j in resultant_dict.items():
    print(i, ':', j)

print(resultant_dict)


data = [
    {
        "name":"asim",
        "company":"marutsakah"
    },
    {

        "name": "asim",
        "company": "capgemini"

    },
    {
        "name": "yoku",
        "company": "noida"
    },
    {

        "name": "asim",
        "company": "hyderabad"

    }
]


resul = [
    {
    "name": "asim",
    "company":["marutsakah","capgemini"]
    }
]


'''**********************************************************************************'''

import pandas as pd

df = pd.read_csv('student.csv')
print(df)



# t = (2,3,4)
#
# print(dir(t))
#
# print(len(t))

# import sys,os
# import resource
# if os.name == 'posix':import resource
#
#
# def main():
#     for i in range(5):
#         return i**i
#
#
# # print(nums.__sizeof__())
# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)







# print('--------------HELLO---------------------')
# target = __import__("test_code.py")
# sum = target.sum

# from test_code import *
# import unittest
#
# class TestCuboid(unittest.TestCase):
#     def test_volume(self):
#         self.assertAlmostEqual(cuboid_volume(2),8)
#         self.assertAlmostEqual(cuboid_volume(1),1)
#         self.assertAlmostEqual(cuboid_volume(0),0)
#         self.assertAlmostEqual(cuboid_volume(5.5),166.375)



# from itertools import permutations
# sentence = ['ate']
#
#
#
# import itertools
#
# lis = ['tea','eat', 'ate','race','care','rat']
#
# # possible_combinations = []
#
# for s in lis:
#     possible_combinations = []
#     t = list(itertools.permutations(s, len(s)))
#     for i in range(0, len(t)):
#         possible_combinations.append(''.join(t[i]))
#     possible_combinations = list(set(possible_combinations))
#     print(possible_combinations)
#     break

# possible_combinations = ['rat', 'raec', 'earc', 'cear', 'rcea', 'erac', 'crae', 'eta', 'tar',
#                          'acer', 'ecra', 'ate', 'eacr', 'tae', 'aerc', 'crea', 'arce', 'art', 'ecar',
#                          'care', 'tea', 'erca', 'aet', 'tra', 'atr', 'eat', 'cera', 'reca', 'aecr', 'race', 'arec',
#                          'acre', 'caer', 'rcae', 'reac', 'rta']

# counter = dict()
#
# for word in lis:
#     if word in possible_combinations

def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
# x = fib(5000000000000000000000000000000000000000000000000000000000000000000000000)

# print(x.__next__())# In Python 3, __next__()
# print(x.__next__())


# for i in x:
#     print(i)
#
#
# x = 10
# gen = (i for i in range(x) if i % 2 == 0)
#
# list_ = [i for i in range(x) if i % 2 == 0]
#
# print(gen)
# print(list_)
# for j in gen:
#     print(j)
#
# def fib(limit):
#     a,b = 0, 1
#
#     while  a < limit:
#         yield a
#         a , b = b, b + a




'''**********************************************************************************'''
#check if palindrome
input = 'malayalam'
str = 'malayalam'

index = - 1
flag = 1
for elem in str:
    print (elem + '-------' +str[index])

    if elem != str[index]:
        flag = 0
        break
    index = index - 1

if flag:
    print('---tes')
else:
    print('---No')



'''**********************************************************************************************'''


#Reverse str

str = "geeks quiz practice code"

temp = ''
list = str.split(' ')
# print(list)
for i in list:
    temp = i +' ' +  temp
temp = temp.rstrip()
print(len(temp))
print(temp)


'''**********************************************************************************************'''


#pop i-th element:
test_str = "GeeksForGeeks"
new_str = ''

for i in range(len(test_str)):
    if i != 2:
        new_str = new_str + test_str[i]

print(new_str)


'''**********************************************************************************************'''


#sort all 0 at left

arr = [0,1,1,1,0,1,0]


n = len(arr)
count = 0

for i in range(0, n):
    if arr[i] == 0:
        count+=1

for i in range(0,count):
    arr[i] = 0

for i in range(count,n):
    arr[i] = 1

'''**********************************************************************************************'''


# sample_str = 'AsimKhan'

# sample_lst = list(sample_str)

# counter = {}

# for char in range(len(sample_lst)):
#     sample_str = str()

#     if sample_lst[char].isupper():
#         if 'upper' not in counter.keys():
#             counter['upper'] = 1
#             sample_str = sample_str + char
#         else:
#             counter['upper'] = 1 + counter['upper']
#             sample_str = sample_str + ' ' +char


    
# print(counter)

''''*****************************************************************************************'''
# Find the missing elements from the array

new_list = [1, 2, 4, 5, 6, 7, 10]

def missing_num_in_arr(new_list):
    missing_elements = []

    for id, elem in enumerate(new_list):
        if id > 0:
            next_elem = new_list[id - 1] + 1
            if next_elem != elem:
                missing_elements.append(next_elem)
    return missing_elements


print(missing_num_in_arr(new_list))


''''*****************************************************************************************'''




# sample_lst = sample_str.split(' ')

# res_list = list()
# for word in sample_lst:
#     rever_str = ''
#     for char in word:
#         rever_str = char +  rever_str
#     res_list.append(rever_str)

# final_str = ''
# for nchar in res_list:
#     final_str = final_str + ' ' +nchar



'''**********************************************************************************'''

'''
Given an integer array A ( below example )
Write a function which takes integer array A as an input parameter 
and returns the integer from this function based on the below condition 

Output => return an integer which is smallest +ve no > 0 and not present in A 

Sample Examples : 
'''


A= [1,3,6,4,1,2,5] # Case - 1
Output :  5 

A = [1,2,3] 
Output :  4 

A =[-1,-3]
Output :  1


def get_smalles_missing_digit(arr):
    arr.sort()
    # print(arr)
    possible_output_arr = list(range(arr[0] + 1, arr[-1])) # [2, 3, 4, 5]
    print(possible_output_arr)
    for i in possible_output_arr:
        if not i in arr:
            if i > 0:
                return i
            return 1
    else:
        return arr[-1] + 1


arr = [1,3,6,4,1,2,5, 0, -1, -1, -2]
# arr = [-1,-3]
print(get_smalles_missing_digit(arr))


'''**********************************************************************************************'''

# Find the expected output:

input = "abbcccddddaa"
output="a1b2c3d4a2"

def get_occurance_str(input):
    final_list = list()
    str_len = len(input)
    for n, char in enumerate(input):
        # print(input[n])
        if n < str_len -1:
            if n == 0:
                temp = dict()
                temp[char] = 1
            else:
                if input[n] == input[n-1]:
                    # temp[char] = temp[char] + 1
                    temp[input[n]] = temp[input[n]] + 1
                else:
                    final_list.append(temp)
                    temp = dict()
                    temp[char] = 1
        else:
            # temp[char] = temp[char] + 1
            temp[input[n]] = temp[input[n]] + 1
            final_list.append(temp)
    
    output = ''
    for i in final_list:
        output = output + list(i.keys())[0] + str(list(i.values())[0])
    print(output)
    return output

get_occurance_str(input)




'''**********************************************************************************************'''

f"1 - Find the first non repeating element from string example: 'SILVER FOR SILVER'."

def first_non_repeating_element(arr):
    occuranc_str = [x for x in Counter(arr) if Counter(arr)[x]  == 1]
    return occuranc_str[0]

s = 'SILVER FOR SILVER'
print(first_non_repeating_element(s))



'''**********************************************************************************'''

f"2- Write a program to delete only second occurence of a element in a list."
a = [9, 8, 2, 3, 8, 3, 5, 8]

d = {}
for n, i in enumerate(a):
    if not i in d.keys():
        d[i] = 1
    else:
        d[i] = d[i] + 1
        if d[i] == 2:
            del a[n]
    
print(a)

'''***********************************************************************************'''

s = ['I', 'want', 4, 'apples', 'and', 18, 'bananas']

# l = ' '.join(map(str,s))


l = ' '.join([str(e) for e in s])









'''**********************************************************************************'''



'''***********************************************************************************'''










'''**********************************************************************************'''



'''***********************************************************************************'''