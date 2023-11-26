# Fiind the ....

'''
vehicleid,stops,start
1,a,1000
2,a,1200
1,b,1100
1,c,1200
2,d,1500

expected
vehicleid,stops,start,end
1,a-b-c,1000,1200
2,a-d,1200,1500

'''

routes = [
    {'id': 1, 'stop': 'a', 'start': 1000},
    {'id': 2, 'stop': 'a', 'start': 1200},
    {'id': 1, 'stop': 'b', 'start': 1100},
    {'id': 1, 'stop': 'c', 'start': 1200},
    {'id': 2, 'stop': 'd', 'start': 1500},

]

'1,a-b-c,1000,1200'

path = [1, 'a', 'b', 'c']


def calculate_path():
    vehice_id = path.pop(0)
    stops = '-'.join(path)
    final_dict = dict()
    for stop in path:
        data = get_time_of_path(vehice_id, stop)
        if not vehice_id in final_dict.keys():
            final_dict[vehice_id] = {}
        if not 'vehice_id' in final_dict[vehice_id].keys():
            final_dict[vehice_id].update({'vehice_id': vehice_id})
        final_dict[vehice_id].update({'vehice_id': vehice_id, 'stop': stops, 'end': data})

    print(final_dict)
    return final_dict


def get_time_of_path(vehice_id, stop):
    for obj in routes:
        if vehice_id == obj['id'] and stop == obj['stop']:
            start = obj['start']
    return start


calculate_path()


'''**********************************************'''
def decorator_list(func):
    def inner(list_of_tuple):
        return [func(v[0], v[1]) for v in list_of_tuple]
    return inner

@decorator_list
def add_together(a,b):
    return a+b

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))