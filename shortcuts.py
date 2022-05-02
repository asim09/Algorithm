import json
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
# print(id(d1))
# print(id(d2))
# print(id(merged_dict))
# print(merged_dict)

d3 = d1.update(d2)      # This will modify the original first dictionary.

# print(id(d3))
# print(d3)
