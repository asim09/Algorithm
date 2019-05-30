# Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc

import re
a = 'hello world lol'

list = re.split(r'(\s+)', a)
print(list)
result_list = []
for word in list:
    if word.isalnum() and word[0].islower():
        final_word = word[0].upper() + word[1:]
        result_list.append(final_word)
    else:
        result_list.append(word)
m = ''.join(e for e in result_list)

case1 = 'hello world'
case2 = 'hello w2orld'
case3 = 'hello 2world'
case4 = 'hEllo 2world'
case5 = 'hEllo   2world'
case6 = 'hEllo   2world  lol'
