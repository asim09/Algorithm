from access_fun import evaluate_test_cases


def locate_card(cards):
    position = 0
    lo = 0
    hi = len(cards['input']['cards']) - 1
    query = cards['input']['query']
    output = cards['output']
    cards = cards['input']['cards']

    while position < len(cards):
        mid = (lo + hi) // 2
        print(f"lo: {lo} hi: {hi} mid - {mid} cards[mid]: {cards[mid]} query {query}")
        result = test_loaction(cards, query, mid)

        if result == 'found':
            return mid

        if result == 'left':
            hi = mid - 1

        if result == 'right':
            lo = mid + 1

        position += 1
    return -1


def test_loaction(cards, query, mid):
    print(query, cards[mid])
    if query == cards[mid]:

        if mid - 1 > 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'

    elif query > cards[mid]:
        return 'left'
    else:
        return 'right'


tests = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},
     'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
               'query': 6},
     'output': 2}
]


evaluate_test_cases(locate_card, tests)

# for index, test in enumerate(tests):
#     print('=' * 30)
#     print()
#     print(f"Test Case {index}")
#
#     res = locate_card(test)
#     test_count['TOTAL'] = len(tests)
#
#     if res == test['output']:
#         test_count['PASSED'] += 1
#         print(f"Input {test['input']['cards']}, {test['input']['query']}")
#         print()
#         print(f"Expected Output {test['output']}")
#         print()
#         print(f"Actual Output {res}")
#         print()
#         print(f"PASSED")
#     else:
#         test_count['FAILED'] += 1
#         print(f"Input {test['input']['cards']}, {test['input']['query']}")
#         print()
#         print(f"Expected Output {test['output']}")
#         print()
#         print(f"Actual Output {res}")
#         print()
#         print(f"FAILED")
#     print(test_count)

import shortcuts
# import sys,os
# import resource
# if os.name == 'posix':import resource
#
#
# def main():
#     for i in range(5):
#         return i**i
#
#
# # print(nums.__sizeof__())
# print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
# print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
# print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)







# print('--------------HELLO---------------------')
# target = __import__("test_code.py")
# sum = target.sum

# from test_code import *
# import unittest
#
# class TestCuboid(unittest.TestCase):
#     def test_volume(self):
#         self.assertAlmostEqual(cuboid_volume(2),8)
#         self.assertAlmostEqual(cuboid_volume(1),1)
#         self.assertAlmostEqual(cuboid_volume(0),0)
#         self.assertAlmostEqual(cuboid_volume(5.5),166.375)



# from itertools import permutations
# sentence = ['ate']
#
#
#
# import itertools
#
# lis = ['tea','eat', 'ate','race','care','rat']
#
# # possible_combinations = []
#
# for s in lis:
#     possible_combinations = []
#     t = list(itertools.permutations(s, len(s)))
#     for i in range(0, len(t)):
#         possible_combinations.append(''.join(t[i]))
#     possible_combinations = list(set(possible_combinations))
#     print(possible_combinations)
#     break

# possible_combinations = ['rat', 'raec', 'earc', 'cear', 'rcea', 'erac', 'crae', 'eta', 'tar',
#                          'acer', 'ecra', 'ate', 'eacr', 'tae', 'aerc', 'crea', 'arce', 'art', 'ecar',
#                          'care', 'tea', 'erca', 'aet', 'tra', 'atr', 'eat', 'cera', 'reca', 'aecr', 'race', 'arec',
#                          'acre', 'caer', 'rcae', 'reac', 'rta']

# counter = dict()
#
# for word in lis:
#     if word in possible_combinations


