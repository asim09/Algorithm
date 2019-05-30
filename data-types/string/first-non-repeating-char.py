# Find the first non repeating character

str = 'python is a open sourec language'

list = list(str)
new_list = []
for char in list:
    if list.count(char) == 1:
        new_list.append(char)
        break
print(new_list)
