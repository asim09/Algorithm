
# # Python program to illustrate for loop in the generator function
# def odd_num(start, end):
#     for i in range(start, end + 1):
#         if i % 2 != 0:
#             yield (i)

# # for num in odd_num(1, 10):
# #     print(num)


# def sqr():
#     i = 1
#     while True:
#         yield i * i
#         i += 1


# for i in sqr():
#     # print('=====', i)
#     if i > 10:
#         break
#     # print(i)

# def pow(max):
#     n = 0
#     while n < max:
#         yield n*n
#         print()
#         n+=1

# # print(pow(4))


# class Sentence:
#     def __int__(self, sentence):
#         self.sentence = sentence
#         self.index = 0
#         self.words = self.sentence.split()

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.sentence):
#             raise StopIteration
#         index = self.index
#         self.index += 1
#         return self.sentence[index]

# # s1 = Sentence('This is my world')

# # for char in s1:
# #     print(char)


# import json
# Student_Data =  [
#  {
#    'Prtky': 'P001',
#    'Srtky': 'S001',
#    'Name': 'Abc',
#    'Subj': 'Math1',
#    'Country': 'India'
#  },
#  {
#    'Prtky': 'P002',
#    'Srtky': 'S002',
#    'Name': 'Abc',
#    'Subj': 'Math2',
#    'Country': 'India'
#  },
#  {
#    'Prtky': 'P003',
#    'Srtky': 'S003',
#    'Name': 'Pqr',
#    'Subj': 'Math3',
#    'Country': 'India2'
#  }
# ]


# output = [
#   {
#     'Abc': {
#       'Subj': 'Math',
#       'Country': 'India',
#       'keys': [
#         {
#           'Prtky': 'P001',
#           'Srtky': 'S001'
#         },
#         {
#           'Prtky': 'P002',
#           'Srtky': 'S002'
#         }
#       ]
#     }
#   },
#   {
#     'Pqr': {
#       'Subj': 'Math',
#       'Country': 'India',
#       'keys': [
#         {
#           'Prtky': 'P003',
#           'Srtky': 'S003'
#         }
#       ]
#     }
#   }
# ]


# def sample_output(students):
#     final_dict = {}
#     for obj in students:
#         if obj['Name'] not in final_dict.keys():
#             final_dict[obj['Name']] = {}
#             temp_list = []
#             temp_list.append({'Prtky': obj['Prtky'], 'Srtky': obj['Srtky']})
#             temp_dict = {'Subj': obj['Subj'], 'Country': obj['Country']}
#             temp_dict.update({'Keys': temp_list})
#             final_dict[obj['Name']].update(temp_dict)
#         else:
#             temp_dict = {'Subj': obj['Subj'], 'Country': obj['Country']}
#             temp_list.append({'Prtky': obj['Prtky'], 'Srtky': obj['Srtky']})
#             temp_dict.update({'Keys': temp_list})
#             final_dict[obj['Name']].update(temp_dict)
#     return json.dumps(final_dict, indent=2)


# print(sample_output(Student_Data))


# importing the module
import pandas as pd
import os





if __name__ == "__main__":
    read_file_from_files_lake(files_path="/Users/mkhan11/Documents/development/data")
    # create_sample_files()
import string


def findLongestSubstring(string):
    n = len(string)
    st = 0
    maxlen = 0
    start = 0
    pos = {}
    pos[string[0]] = 0

    for i in range(1, n):
        if string[i] not in pos:

            pos[string[i]] = i
            # print(f'={pos}=={[string[i]]}===={i}')
            # print()
        else:
            # print(f'={pos}=={[string[i]]}===={i}')
            if pos[string[i]] >= st:
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
                st = pos[string[i]] + 1
            # print(f'==={pos}')
            # print(f'==={pos[string[i]]}==={i}')
            pos[string[i]] = i
            # print(f'={pos}=={[string[i]]}===={i}')
    # if maxlen < i - st:
    #     print('==================================')
    #     maxlen = i - st
    #     start = st
    # print(start,start + maxlen)
    return string[start: start + maxlen]


def solve(str: str) -> int:
    if len(str) == 0:
        return 0
    maxans = -1
    for i in range(len(str)):
        set = {}
        for j in range(i, len(str)):
            print(f"i-->{i}, j--->{j}, set----{set},str[j]---->{str[j]},  maxans---- {maxans}")
            if str[j] in set:
                print()
                maxans = max(maxans, j - i)
                break
            set[str[j]] = 1
        print()
    return maxans


def findLongestSubstring(string: str):
    n = len(string)
    st = 0
    maxlen = 0
    start = 0
    pos = {}
    pos[string[0]] = 0

    for i in range(1, n):
        if string[i] not in pos:
            pos[string[i]] = i
        else:
            if pos[string[i]] >= st:
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
                st = pos[string[i]] + 1
            pos[string[i]] = i
    print(start, start + maxlen)
    return string[start: start + maxlen]

# find subarray with given sum:\





if __name__ == "__main__":
    string1 = "GEEKFORGEEKS"
    string2 = "abcaabcdba"
    # print(findLongestSubstring(string2))
    # print(solve(string2))
    # print(solve(string1))
    print(subarray_of_given_sum(array=[1, 4, 0, 0, 3, 10, 5], sum=7))
