# from collections import Counter

# arr = [0,1,1,1,0,1,0]
# k = Counter(arr)

# for i in range(k[0]):
#     arr[i] = 0
# for i in range(k[0], (k[1] + k[0])):
#     arr[i] = 1
# print(arr)



input = d = {
    'Satish':1,
    'A':2,
    'B':2,
    'D':3
}
# def get_sec_highest_sal(dic):
#     lst_val = list(d.values())
#     sorted_lst = sorted(lst_val, reverse=True)
#     sec_highest = sorted_lst[1]
#     obj1 = {obj:d[obj] for obj  in d if d[obj] == sec_highest}
#     return set(obj1)

k = dict(sorted(d.items(), key=lambda x: x[1]))
# l = list(k.values())
# print(l)

# d = {'a': 10, 'b': 20, 'c': 30,'d':20}
# k = sorted(d.values(), reverse=True)
        



