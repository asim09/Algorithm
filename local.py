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
