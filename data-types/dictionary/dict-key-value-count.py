




#Prog - 2: Count element occurence in fill it into dict
grades = ["A", "A", "B", "C", "D", "C", "B", "C", "A", "C", "B"]

counter = dict()
for grade in grades:
    if grade in counter:
        counter[grade] = counter[grade] + 1
    else:
        counter[grade] = 1


print(counter)

# count word trarting have same first character.
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
