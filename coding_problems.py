from os.path import join, dirname, realpath
import os
from collections import Counter

"1 - Find the first non repeating element from string example: 'SILVER FOR SILVER'."
"2-Write a program to delete second occurence of a element in a list."
"3 - find prime num between 100 to 200"


"1. Replace multiple characters ['s','l', 'a'] at once with 'AA':"

sample_input = "String with replaced Content :  Hello, ThiX iX a Xample Xtring"
output = "AAtring with repAAAAced Content :  HeAAAAo, ThiX iX AA XAAmpAAe Xtring"
ref_list = ["s", "l", "a"]
replace_with = "AA"


def replecement(sample_input, ref_list, replace_with):
    """using list comprehension"""
    output = "".join(
        [replace_with if i.lower() in ref_list else i for i in sample_input]
    )
    return output


"2. Replace multiple characters {'a': 'b', 'b': 'a'}:"

sample_input = "String with replaced Content :  Hello, ThiX iX a Xample Xtring"
output = "AAtring with repAAAAced Content :  HeAAAAo, ThiX iX AA XAAmpAAe Xtring"
replacements = {"a": "b", "b": "a"}


def replecement(sample_input, replacements):
    """using list comprehension"""
    replaced_chars = [replacements.get(char, char) for char in sample_input]
    output = "".join(replaced_chars)
    return output


"3. using generator: Replace multiple characters {'e': '1', 'b': '6', 'i': '4'} :"

sample_input = "'geeksforgeeks is best'"
replacements = {"e": "1", "b": "6", "i": "4"}


def replecement(sample_input, replacements):
    """using generator expression"""
    replaced_chars = (
        idx if idx not in replacements else replacements[idx] for idx in sample_input
    )
    output = "".join(replaced_chars)
    return output


# print(sample_input)
# print(replecement(sample_input, replacements))
# ************************************************************************************************************************************

"4. Check if frequencies of all characters of a string are different"

sample_input = "abbaccc"

"""'a'  occurs two times, 'b' occurs once
and 'c' occurs three times."""


def check_frequency(sample_input):
    is_different = False
    freq = Counter(sample_input)
    freq_set = set(freq.values())
    if len(freq_set) == len(set(sample_input)):
        is_different = True
    return is_different


# ************************************************************************************************************************************

"5. Find the frequency of each character / element in dict"
sample_dict = {"a": "A", "b": 2, "c": 3, "d": "c"}

"Method-1"


def frequncy(sample_dict):
    resultant_dic = {}
    sample_list = list(sample_dict.keys()) + list(sample_dict.values())

    for elem in sample_list:
        if isinstance(elem, int):
            if elem not in resultant_dic.keys():
                resultant_dic[elem] = sample_list.count(elem)
        else:
            if elem.upper() not in resultant_dic.keys():
                resultant_dic[elem.upper()] = 1
            else:
                resultant_dic[elem.upper()] = resultant_dic[elem.upper()] + 1
    return resultant_dic


print(frequncy(sample_dict))


"Method-2"


def frequncy(sample_dict):
    resultant_dic = {}
    sample_list = list(sample_dict.keys()) + list(sample_dict.values())

    for elem in sample_list:
        if isinstance(elem, int):
            if elem not in resultant_dic.keys():
                resultant_dic[elem] = sample_list.count(elem)
        else:
            if elem.upper() not in resultant_dic.keys():
                resultant_dic[elem.upper()] = 1
            else:
                resultant_dic[elem.upper()] = resultant_dic[elem.upper()] + 1
    return resultant_dic


# ************************************************************************************************************************************

"8. Find current file path"


# STORAGE_FILE = join(dirname(realpath(__file__))
def find_path_current_file():
    return os.path.abspath(os.path.dirname(__file__))


# ************************************************************************************************************************************

"9. Capitalize first letter o each word:"

a = "hello world lol"
result = "Hello World Lol"


def capitalize_string(string):
    lst_a = a.split(" ")
    for index, char in enumerate(lst_a):
        if char[0].isalpha() and char[0].islower():
            new_str = char[0].upper() + char[1:]
            lst_a[index] = new_str
    str = " ".join(e for e in lst_a)
    return str


# ************************************************************************************************************************************


# ************************************************************************************************************************************
"12. pop i-th element:"
test_str = "GeeksForGeeks"
position = 3


def pop_character(test_str, position):
    res = test_str[:position] + test_str[position + 1 :]
    return res


# print(pop_character(test_str, position))
# ************************************************************************************************************************************


# ************************************************************************************************************************************


"14.Find the first non repeating character"

string = "python is a open sourec language"
result = "y"


def find_first_non_repeating_char(string):
    freq = Counter(string)
    for i in string:
        if freq[i] == 1:
            break
    return i


# print(find_first_non_repeating_char(string))
# ************************************************************************************************************************************

"15.Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp."
"""
Input: {([])}
Output:  true

Input: ([]
Output: false
"""


def ispar(x):
    stack = []

    for char in x:
        print()
        if char in ["[", "{", "("]:
            stack.append(char)
        elif char == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        elif char == "}":
            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif char == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
        print(f"adding--{char}, Stack-- {' '.join(e for e in stack)}")
        print()
    if len(stack) == 0:
        return True
    return False


case1 = "[()]{}{[()()]()}"
case2 = ""
# print(ispar(case1))

# ******************************************************************

"16. Find the final direction of a pivot which is given commands to move left / right:"
'explanation: initial position is required and should br passed as a parameter.'


def find_direction(commands, initial_pos):
    directions = ("N", "E", "S", "W")
    command_bounderies = ("L", "R")
    initial_pos_index = directions.index(initial_pos)
    print(initial_pos_index)
    counter = initial_pos_index
    for command in commands:
        if command in command_bounderies:
            counter = counter + -1 if command == "L" else 1
            new_position = directions[counter]
    return new_position


initial_pos = "S"
commands = "LLR L"
output = "W"
print(find_direction(commands, initial_pos))

# ******************************************************************

f"3 - find prime num between 100 to 200"
def foo():
    for num in range(100, 200):
        if all(num %i !=0 for i in range(2,num)):
            print(num)
foo()