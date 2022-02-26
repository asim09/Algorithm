print('--------------HELLO---------------------')
target = __import__("test_code.py")
sum = target.sum

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


