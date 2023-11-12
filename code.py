
s = 'abcabcbb'

# Python3 program to find and print longest
# substring without repeating characters.

# Function to find and print longest
# substring without repeating characters.


def findLongestSubstring(string):
    n = len(string)
    st = 0
    maxlen = 0
    start = 0
    pos = {}
    pos[string[0]] = 0

    for i in range(1, n):
        if string[i] not in pos:
            
            pos[string[i]] = i
            # print(f'={pos}=={[string[i]]}===={i}')
            # print()
            
            
        else:
            
            # print(f'={pos}=={[string[i]]}===={i}')
            if pos[string[i]] >= st:
                currlen = i - st
                if maxlen < currlen:
                    maxlen = currlen
                    start = st
                st = pos[string[i]] + 1
            

            
            # print(f'==={pos}')
            # print(f'==={pos[string[i]]}==={i}')
            pos[string[i]] = i
            # print(f'={pos}=={[string[i]]}===={i}')

    # if maxlen < i - st:
    #     print('==================================')
    #     maxlen = i - st
    #     start = st
    print(start,start + maxlen)
    return string[start: start + maxlen]


if __name__ == "__main__":
    # string = "GEEKSFORGEEKS"
    string = "abcabcbb"
    print(findLongestSubstring(string))




max_len = 0
for i in range(len(s)):
    _map = {}
    _map[s[i]] = 1
    for j in range(i + 1, len(s)):
        if s[j] not in _map.keys():
            _map[s[j]] = 1
        else:
            break
    max_len = max(max_len, len(_map))

# print(max_len)



def lengthOfLongestSubstring(s):
    if len(s) == 0:
        return 0
    
    max_len = 0
    
    for i in range(len(s)):
        _map = {}
        _map[s[i]] = 1
        print(_map)
        
        for j in range(i+1, len(s)):
            temp = j
            if s[j] not in _map:
                _map[s[j]] = 1
            else:
                break
        # print(max_len, len(_map))
        
        max_len = max(max_len, len(_map))
    return max_len
s = 'abcabcbb'
# lengthOfLongestSubstring(s)
# print(max(12, 4))









































marks = {
    "class":{
        "student":{
            "name":"Tom",
            "mark":[
                ("physics",70),
                ("history",80)
            ]
        }
    }
}


# print(marks['class']['student']['mark'][1][1])

student = {"name":"Tom", "class":8, "marks":75}

key_list = list(student.keys())
val_list = list(student.values())

# print(key_list)
# print()
# print(val_list)

colors = ['red', 'blue', 'orange','red','yellow','orange', 'red','white', 'black','pink','red','white','blue']

# print(json.dumps(Counter(colors), indent=2))

# even 1-30




def get_even_arr(start, end):
    lst = list(filter(lambda x : x % 2 == 0, list(range(start, end + 1))))
    # lst = [x for x in list(range(start, end + 1)) if x % 2 == 0]
    return lst

start = 1
end = 30
# print(get_even_arr(start, end))


list_1 = [4, 5, 6, 7]
list_2 = [3, 6, 5, 7]

# common_elem = [x for x in list_1 if x in list_2]

common_elem = set(list_1).intersection(list_2)


# print(common_elem)



list1= ['w','e','l','c','o','m','e']
result =''
for c in list1:
    result = result+c



result = ''.join(e for e in list1)

# print(result)


# for i in range(1, 6):
#     print('*'*i, end='\n')






































































def func( list_items = [] ):
	list_items.append('PYTHON')
	return list_items
# print (func()) # ['PYTHON']
# print (func()) # ['PYTHON', 'PYTHON']

# ***********************************
list1 = ["C", "C#", "PYTHON", "JAVA"]
# ["C", "C#", "PYTHON", "JAVA"] - 0 -  'C'
# [C#", "PYTHON", "JAVA"] - 1 -  'PYTHON'
# [C#", "JAVA"] - 2 -  ''
for idx, item in enumerate(list1):
	list1.pop(idx)
# print(list1) # ['C', 'PYTHON' ]
# **********************************
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age
 
    # def display(self):
    #     print(self.name)
    #     print(self.__age)
 
person = Person('Dev', 30)

# person.display() # error
# print(person.name) # 'Dev'
# print(person.__age) # error
# **********************************

class A:
    def __init__(self, a):
        self.a = a
 
    # adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Best")
ob4 = A("One")
 
# print(ob1 + ob2)
# print(ob3 + ob4)




def age_above_input(arr, age):
    age_lst = [x['Age'] for x in arr]
    required_age = list(filter(lambda x: x > age, age_lst))
    final_dict = {x['Name']: x['Age'] for x in arr if x['Age'] in required_age}
    return final_dict
    


age = 18

arr = [
    {"Name" : "Arun", "Age" : 20},
    {"Name" : "Babu", "Age" : 30},
    {"Name" : "Charle", "Age" : 15},
    {"Name" : "Dinesh", "Age" : 18}
]
# print(age_above_input(arr, age))


































































































































s = 'm csjd nki b . nd,. n n.|'
# print(Counter(s))



s = '3132061.SAM.AXM.S1325.BLACK'



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
    {'id':1, 'stop':'a', 'start':1000},
    {'id':2, 'stop':'a', 'start':1200},
    {'id':1, 'stop':'b', 'start':1100},
    {'id':1, 'stop':'c', 'start':1200},
    {'id':2, 'stop':'d', 'start':1500},

]

'1,a-b-c,1000,1200'

path = [1,'a', 'b', 'c']

def calculate_path():
    vehice_id = path.pop(0)
    stops = '-'.join(path)
    final_dict = dict()
    for stop in path:
        data = get_time_of_path(vehice_id, stop)
        if not vehice_id in final_dict.keys():
            final_dict[vehice_id] = {}
        if not 'vehice_id' in final_dict[vehice_id].keys():
            final_dict[vehice_id].update({'vehice_id':vehice_id})
        final_dict[vehice_id].update({'vehice_id':vehice_id,'stop':stops, 'end':data})

    print(final_dict)
    return final_dict

def get_time_of_path(vehice_id, stop):
    for obj in routes:
        if vehice_id == obj['id'] and stop == obj['stop']:
            start = obj['start']
    return start

# calculate_path()

'''
vehicleid,stops,start,end
1,a-b-c,1000,1200
2,a-d,1200,1500
'''
import csv


# cities           = 'Delhi, Bhopal, Hyderabad, Chennai'
cities = 'Bengaluru, Hyderabad, Bhopal'


pairs = [
    {
        'source': 'Delhi',
        'destination': 'Bhopal',
        'distance': 786
    },
    {
        'source': 'Bhopal',
        'destination': 'Hyderabad',
        'distance': 850
    },
    {
        'source': 'Hyderabad',
        'destination': 'Chennai',
        'distance': 626
    },
    {
        'source': 'Bengaluru',
        'destination': 'Hyderabad',
        'distance': 576
    }

]


def calculate_circuit_distance(cities):
    citties_arr = cities.split(', ')
    distance = 0
    for n, city in enumerate(citties_arr):
        if n <= len(citties_arr) - 2:
            source = citties_arr[n]
            destination = citties_arr[n + 1]
            distance = distance + calculate_pair_distance(source, destination)
    return distance


def calculate_pair_distance(source, destination):
    for obj in pairs:
        if obj['source'] == source and obj['destination'] == destination or obj['source'] == destination and obj['destination'] == source:
            distance = obj['distance']
    return distance


# print(calculate_circuit_distance(cities))







data = [
  {
    "data": [
      {
        "latitude": 49.283026,
        "longitude": -123.122826,
        "type": "address",
        "name": "970 Robson Street",
        "number": "970",
        "postal_code": None,
        "street": "Robson Street",
        "confidence": 1,
        "region": "British Columbia",
        "region_code": "BC",
        "county": "Greater Vancouver",
        "locality": "Vancouver",
        "administrative_area": None,
        "neighbourhood": "Downtown",
        "country": "Canada",
        "country_code": "CAN",
        "continent": "North America",
        "label": "970 Robson Street, Vancouver, BC, Canada"
      }
    ]
  },
  {
    "data": [
      {
        "latitude": 52.372253,
        "longitude": 4.886162,
        "type": "address",
        "name": "Hartenstraat 13",
        "number": "13",
        "postal_code": None,
        "street": "Hartenstraat",
        "confidence": 1,
        "region": "Noord-Holland",
        "region_code": "NH",
        "county": None,
        "locality": "Amsterdam",
        "administrative_area": None,
        "neighbourhood": "Grachtengordel-West",
        "country": "Netherlands",
        "country_code": "NLD",
        "continent": "Europe",
        "label": "Hartenstraat 13, Amsterdam, NH, Netherlands"
      },
      {
        "latitude": 52.372245,
        "longitude": 4.886167,
        "type": "address",
        "name": "Hartenstraat 13-H",
        "number": "13-H",
        "postal_code": "1016BZ",
        "street": "Hartenstraat",
        "confidence": 1,
        "region": "Noord-Holland",
        "region_code": "NH",
        "county": None,
        "locality": "Amsterdam",
        "administrative_area": None,
        "neighbourhood": "Grachtengordel-West",
        "country": "Netherlands",
        "country_code": "NLD",
        "continent": "Europe",
        "label": "Hartenstraat 13-H, Amsterdam, NH, Netherlands"
      },
      {
        "latitude": 52.372245,
        "longitude": 4.886167,
        "type": "address",
        "name": "Hartenstraat 13-2",
        "number": "13-2",
        "postal_code": "1016BZ",
        "street": "Hartenstraat",
        "confidence": 1,
        "region": "Noord-Holland",
        "region_code": "NH",
        "county": None,
        "locality": "Amsterdam",
        "administrative_area": None,
        "neighbourhood": "Grachtengordel-West",
        "country": "Netherlands",
        "country_code": "NLD",
        "continent": "Europe",
        "label": "Hartenstraat 13-2, Amsterdam, NH, Netherlands"
      },
      {
        "latitude": 52.372245,
        "longitude": 4.886167,
        "type": "address",
        "name": "Hartenstraat 13-3",
        "number": "13-3",
        "postal_code": "1016BZ",
        "street": "Hartenstraat",
        "confidence": 1,
        "region": "Noord-Holland",
        "region_code": "NH",
        "county": None,
        "locality": "Amsterdam",
        "administrative_area": None,
        "neighbourhood": "Grachtengordel-West",
        "country": "Netherlands",
        "country_code": "NLD",
        "continent": "Europe",
        "label": "Hartenstraat 13-3, Amsterdam, NH, Netherlands"
      },
      {
        "latitude": 52.372245,
        "longitude": 4.886167,
        "type": "address",
        "name": "Hartenstraat 13-1",
        "number": "13-1",
        "postal_code": "1016BZ",
        "street": "Hartenstraat",
        "confidence": 1,
        "region": "Noord-Holland",
        "region_code": "NH",
        "county": None,
        "locality": "Amsterdam",
        "administrative_area": None,
        "neighbourhood": "Grachtengordel-West",
        "country": "Netherlands",
        "country_code": "NLD",
        "continent": "Europe",
        "label": "Hartenstraat 13-1, Amsterdam, NH, Netherlands"
      }
    ]
  },
  {
    "data": [
      {
        "latitude": 40.780094,
        "longitude": -73.959558,
        "type": "address",
        "name": "1146 Madison Ave",
        "number": "1146",
        "postal_code": "10028",
        "street": "Madison Ave",
        "confidence": 1,
        "region": "New York",
        "region_code": "NY",
        "county": "New York County",
        "locality": "New York",
        "administrative_area": None,
        "neighbourhood": "Upper East Side",
        "country": "United States",
        "country_code": "USA",
        "continent": "North America",
        "label": "1146 Madison Ave, New York, NY, USA"
      },
      {
        "latitude": 42.666342,
        "longitude": -73.792632,
        "type": "address",
        "name": "1146 Madison Avenue",
        "number": "1146",
        "postal_code": "12208",
        "street": "Madison Avenue",
        "confidence": 1,
        "region": "New York",
        "region_code": "NY",
        "county": "Albany County",
        "locality": "Albany",
        "administrative_area": "Albany",
        "neighbourhood": None,
        "country": "United States",
        "country_code": "USA",
        "continent": "North America",
        "label": "1146 Madison Avenue, Albany, NY, USA"
      },
      {
        "latitude": 40.780095,
        "longitude": -73.959571,
        "type": "address",
        "name": "1146 Madison Avenue",
        "number": "1146",
        "postal_code": None,
        "street": "Madison Avenue",
        "confidence": 1,
        "region": "New York",
        "region_code": "NY",
        "county": "New York County",
        "locality": "New York",
        "administrative_area": None,
        "neighbourhood": "Upper East Side",
        "country": "United States",
        "country_code": "USA",
        "continent": "North America",
        "label": "1146 Madison Avenue, New York, NY, USA"
      }
    ]
  },
  {
    "data": [
      {
        "latitude": 47.664027,
        "longitude": -122.297896,
        "type": "address",
        "name": "2656 NE University Village St",
        "number": "2656",
        "postal_code": "98105",
        "street": "NE University Village St",
        "confidence": 1,
        "region": "Washington",
        "region_code": "WA",
        "county": "King County",
        "locality": "Seattle",
        "administrative_area": None,
        "neighbourhood": "Ravenna",
        "country": "United States",
        "country_code": "USA",
        "continent": "North America",
        "label": "2656 NE University Village St, Seattle, WA, USA"
      },
      {
        "latitude": 47.66401,
        "longitude": -122.29806,
        "type": "address",
        "name": "2656 Northeast University Village Street",
        "number": "2656",
        "postal_code": "98105",
        "street": "Northeast University Village Street",
        "confidence": 1,
        "region": "Washington",
        "region_code": "WA",
        "county": "King County",
        "locality": "Seattle",
        "administrative_area": None,
        "neighbourhood": "Ravenna",
        "country": "United States",
        "country_code": "USA",
        "continent": "North America",
        "label": "2656 Northeast University Village Street, Seattle, WA, USA"
      }
    ]
  }
]



d = {
    "data": [
      {
        "latitude": 49.283026,
        "longitude": -123.122826,
        "type": "address",
        "name": "970 Robson Street",
        "number": "970",
        "postal_code": None,
        "street": "Robson Street",
        "confidence": 1,
        "region": "British Columbia",
        "region_code": "BC",
        "county": "Greater Vancouver",
        "locality": "Vancouver",
        "administrative_area": None,
        "neighbourhood": "Downtown",
        "country": "Canada",
        "country_code": "CAN",
        "continent": "North America",
        "label": "970 Robson Street, Vancouver, BC, Canada"
      }
    ]
  }
storeId = '00120'
import json

output = {
  "00120": {
    "street_address": "970 Robson Street",
    "locality": "Vancouver",
    "region": "British Columbia",
    "country": "Canada",
    "geopoint": {
      "lat": 49.283026,
      "long": -123.122826
    }
  }
}


sample_dict = {}

for i in d['data']:
    temp = {}
    temp['locality'] = i['locality']
    temp['region'] = i['region']
    temp['country'] = i['country']
    temp['locality'] = i['locality']
    temp['geopoint'] = {'latitude':i['locality'], 'long':i['longitude']}
    sample_dict[storeId] = temp

# print(json.dumps(sample_dict, indent=2))




























































user_name = 'Asim Khan'
# pwd = 'AsimnahK'


def gen_pwd(user_name):
    lst_user_name = user_name.split(' ')
    second_name = lst_user_name[-1]
    second_name = second_name[::-1]
    # print(second_name)
    lst_user_name[1] = second_name
    pwd = ''.join(lst_user_name)
    print(pwd)
    return pwd


# gen_pwd(user_name)



fruits = [
    {

        'fruit_name':'bananna',
        'color':'yellow',
        'weight':2,
    },
    {

        'fruit_name':'mango',
        'color':'pink',
        'weight':5,
    },
    {

        'fruit_name':'apple',
        'color':'red',
        'weight':3,
    }
]


in_stock = {'bananna':10, 'mango':20}

import json
def get_fruit_price(fruits,in_stock):
    for n,obj in enumerate(fruits):
        # print(n, obj)
        # print(fruits[])
        if obj['fruit_name'] in in_stock.keys():
            obj['price'] = in_stock[obj['fruit_name']]

    return fruits

# get_fruit_price(fruits, in_stock)
# print()






# def decorator_list(fnc):
#     def inner(list_of_tuples):
#         return [fnc(val[0], val[1]) for val in list_of_tuples]
#     return inner


# @decorator_list
# def add_together(a, b):
#     return a + b


def decorator_list(func):
    def inner(list_of_tuple):
        return [func(v[0], v[1]) for v in list_of_tuple]
    return inner


@decorator_list
def add_together(a,b):
    return a+b

# print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))