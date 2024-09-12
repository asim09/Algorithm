dict = {'a':'A', 'b':2, 'c':3, 'd':'c'}
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




#Prog - 2: Count element occurence in fill it into dict
grades = ["A", "A", "B", "C", "D", "C", "B", "C", "A", "C", "B"]

counter = dict()
for grade in grades:
    if grade in counter:
        counter[grade] = counter[grade] + 1
    else:
        counter[grade] = 1


print(counter)

# count word starting have same first character.
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


# Prog-4

list = ['apple', 'king', 'word','swear','swear' ]
resultant_dict = dict()

for word in list:
    resultant_dict[word[0]] = word

print(resultant_dict)

'''*****************************************************************************************'''

#Sort a list based on a key
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
