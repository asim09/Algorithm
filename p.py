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
def get_sec_highest_sal(dic):
    lst_val = list(d.values())
    sorted_lst = sorted(lst_val, reverse=True)
    sec_highest = sorted_lst[1]
    obj1 = {obj:d[obj] for obj  in d if d[obj] == sec_highest}
    return set(obj1)

k = dict(sorted(d.items(), key=lambda x: x[1]))
# l = list(k.values())
# print(l)

# d = {'a': 10, 'b': 20, 'c': 30,'d':20}
# k = sorted(d.values(), reverse=True)



        


input = [
        {
            "cell_name": "Living cells",
            "children": [
                {"name": "Events", "value": "7888"},
                {"name": "Parent", "value": "86.7"},
                {"name": "CD38 PE-A Median", "value": "7.1"},
            ]
        }
    ]
import json

counter = 0
res = []
while counter < len(input):
    temp = {}
    # print(input[counter])
    # print('============1=', res)
    for obj in input[counter]:
        # print('======',input[counter][obj])
        # print('============2=', res, counter)

        if obj == 'children':

            for k in input[counter][obj]:
                # print('=============', res)
                # print(k)
                temp[k['name']] = k['value']
            # print(temp)
        else:
            temp['cell_name'] = input[counter][obj]
        res.append(temp)
    counter += 1

# print(json.dumps(res, indent=4))
# print(json.dumps(temp, indent=4))

dir_dict = {
    "L_to_N":"W",
    "R_to_N":"E",
    "L_to_W":"S",
    "R_to_W":"N",
    "L_to_E":"N",
    "R_to_E":"S",
    "L_to_S":"W",
    "R_to_S":"E",
}


def calculate_direction01(sequence_arr, initial_position):
    direction = ['E', 'W', 'N', 'S']
    spins = ['L', 'R']
    if len(sequence_arr) > 0 and initial_position in direction:
        for comm in sequence_arr:
            key = comm + '_to_' + initial_position
            initial_position = dir_dict.get(key, None)
        return initial_position
    return 'flash msg'


command_sequence= 'LLLLL'
initial_position = 'N'

def find_direction(*args):

    return -1

print(find_direction())




