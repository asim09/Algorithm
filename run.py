def fact(num):
    if num == 0 or num == 1:
        return 1

    else:
        return num * fact(num -1)
    
print(fact(5))


# sample_list = [1, 2, 3, 3, 3, 4, 1, 10, 5, 6, 7, 8, 8, 9, 10, 12]
# iterator = sample_list[0]
# missing_list = []
# duplicate_list = []

# for num in sample_list:
#     print(num, iterator)

#     if iterator < num:
#         missing_list.append(iterator)
#         iterator += 2

#     elif iterator > num:
#         duplicate_list.append(num)

#     elif iterator == num:
#         iterator += 1

# print(missing_list, duplicate_list)



# a = [1, 2, 3, 4, 5]
# sum = 0
# new_list = []
# for i in a:
#     sum = sum + i
#     new_list.append(sum)
# print(new_list)


# x = "AABCCDE"


# stack = []

# for i in x:
#     if stack and stack[-1] == i:
#         stack.pop()
#     else:
#         stack.append(i)

# print(stack)






# from collections import Counter

# data = ["geeks", "for", "geeks"]

# def find_dup_and_remove(input):
#     d1 = Counter(input)
#     duplicates = [i for i, j in d1.items() if j > 1]
#     d2 = list(dict.fromkeys(data))
#     return duplicates, d2


# print(find_dup_and_remove(data))



# a = 'ab cd'

# l = len(a.replace(' ', ''))
# print(l)




data = [
    {
        "eid": 95,
        "weekStartdate": "2021-03-18 12:40:11",
        "workHours": 12.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 95,
        "weekStartdate": "2021-03-19 12:40:11",
        "workHours": 11.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 95,
        "weekStartdate": "2021-03-20 12:40:11",
        "workHours": 10.0,
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
# res = sorted(data, key=lambda x: x['workHours'])
# import json
# print(json.dumps(res, indent=4))
# list = ['hello', 'king', 'word', 'sword','swear', 'hi']

# res_dict = {}

# for obj in list:
#     if obj[0] not in res_dict.keys():
#         res_dict[obj[0]]  = []
#         res_dict[obj[0]].append(obj)
#     else:
#         res_dict[obj[0]].append(obj)
# print(res_dict)





# grades = ["A", "A", "B", "C", "D", "C", "B", "C", "A", "C", "B"]

# res_dict = {}

# for grade in grades:
#     if grade not in res_dict.keys():
#         res_dict[grade] = 1
#     res_dict[grade] = res_dict[grade]  + 1

# print(res_dict)

input = 'asim'
output = '?asim#'

def append_char(func):
    def inner(user_input):
        s = '?' + user_input + '*'
        return func(s)
    return inner

@append_char
def alter_name(user_name):
    return user_name
# print(alter_name(input))
