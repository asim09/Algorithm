
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


files_path = '/Users/mkhan11/Documents/development/data'

def export_to_excel(files_path, file_name):
    print("Expoting initiated....")
    excel_data_df = pd.read_excel(files_path + '/' +file_name, sheet_name="Sheet1", index_col=0)
    # excel_data_df = pd.read_excel(files_path + '/' +file_name, sheet_name="Sheet1")
    print(f"data content of file---{file_name}-- is below")
    print('######################')
    print(excel_data_df)
    print('######################')
    from_file_columns = ["ID", "Name", "Marks", "Grade"]
    master_file = 'MarksData.xlsx'
    print(f"==writing to master file== ---{master_file}")
    print(files_path + '/' + master_file)
    # status = excel_data_df.to_excel(files_path + '/' + master_file, columns=from_file_columns, index=False)
    # with pd.ExcelWriter(files_path + '/' + master_file, mode="a", if_sheet_exists="overlay") as writer:
    #     excel_data_df.to_excel(writer,header=True, index=False)

    with pd.ExcelWriter(files_path + '/' + master_file, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
        excel_data_df.to_excel(writer, sheet_name="Sheet1", header=False, startrow=writer.sheets["Sheet1"].max_row, index=False)
    return 1


# file_one = "Athena01-01-2023.xlsx"
# print(export_to_excel(files_path, file_one))

def generate_file_names():
    file_prefix = "Athena"
    starting_month = 7
    ending_month = 8
    days_limit = 5
    suffix = "-2023.xlsx"
    files_list = []
    for str_month in range(starting_month, ending_month + 1):
        for day in range(1, days_limit + 1):
            day = '0' + str(day) if day <= 9 else day
            if int(str_month) <= 9:
                month = '0' + str(str_month)
                f = file_prefix + str(month) + '-' + str(day) + suffix
                files_list.append(f)
    # for index, file in enumerate(files_list):
    #     if index == 31:
    #         print()
    #         print()
    #     print(file)
    return files_list

def read_file_from_files_lake(files_path):
    files = generate_file_names()
    print('===reading files.....')
    print('=== files names.....', files)
    for file_name in files:
        print(f"for file----->{file_name}")
        if os.path.isfile(files_path + '/' + file_name):
            print(f"{file_name}--->True")
            export_to_excel(files_path, file_name)
    return True


# print(read_file_from_files_lake(files_path="/Users/mkhan11/Documents/development/data"))


# generate_file_names()

def create_sample_files():
    marks_data = pd.DataFrame({'ID': {0: 23, 1: 43, 2: 12,
                                    3: 13, 4: 67, 5: 89,
                                    6: 90, 7: 56, 8: 34},
                            'Name': {0: 'Ram', 1: 'Deep',
                                    2: 'Yash', 3: 'Aman',
                                    4: 'Arjun', 5: 'Aditya',
                                    6: 'Divya', 7: 'Chalsea',
                                    8: 'Akash' },
                            'Marks': {0: 89, 1: 97, 2: 45, 3: 78,
                                        4: 56, 5: 76, 6: 100, 7: 87,
                                        8: 81},
                            'Grade': {0: 'B', 1: 'A', 2: 'F', 3: 'C',
                                        4: 'E', 5: 'C', 6: 'A', 7: 'B',
                                        8: 'B'}})

    files_list = generate_file_names()
    # print(d)
    # file_name =  'Athena07-01-2023.xlsx'
    for abs_file_name in files_list:
        abs_file_name = os.path.join(files_path, abs_file_name)
        # print(abs_file_name)
        marks_data.to_excel(abs_file_name)
    print('DataFrame is written to Excel File successfully.')
    return None


if __name__ == "__main__":
    read_file_from_files_lake(files_path="/Users/mkhan11/Documents/development/data")
    # create_sample_files()

=======
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
