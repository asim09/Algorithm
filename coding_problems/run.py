print('======RUN===========')

add = lambda a, b : a + b
# print(add(3,6))

original_list = [[11, 22, 33, 44], [55, 66, 77], [88, 99]]
d = [2, [3, [5 , 6]]]

final = []
for i in d:
    if isinstance(i, list):
        final.extend(i)
print(final)