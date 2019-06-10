# Make first letter key and all the words starting with
# same char should be mapped as values.

s = 'hello world program programs word test'
words = s.split()
result_dict = {}

for word in words:
    if word[0] not in result_dict:
        result_dict[word[0]] = []
        result_dict[word[0]].append(word)
    if word not in result_dict[word[0]]:
        result_dict[word[0]].append(word)

print(result_dict)

