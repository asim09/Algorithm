


















# class shop:
#     charges = 10
#     def candy_count(self, candies):
#         result = {} 
#         for i, j in candies: 
#             result.setdefault(j, []).append(i) 
#         return result
         
#     def candy_count_result(self,a):
#         return a*shop.charges
    
# obj1 = shop()
# try:
#     candies = [(2, 1), (1, 1), (4, 4), (5, 6), (7, 5), (6, 4)] 
#     a = obj1.candy_count(candies) 
#     b = obj1.candy_count_result(a)
#     print(a)
# except Exception as e:
#     print(e)

'''
As part of the requirement, you have to send a request for the particular endpoint in a loop. Which of the following method would you use, so that each time the request is sent, there is no successive effect each time?
'''


# Note - Datatype is fixed (int)
sample_arr1 = [], 2 , None                          # Empty list.
sample_arr2 = [4, 2, 6, 3, 8, 1, 0], 2 , 6          # All positive and unique num.
sample_arr3 = [4, 2, 6, 3, 8, 1, 0, -5, -4], 2 , 6  # Input contains -ve numbers.
sample_arr4 = [4, 2, 6, 3, 8, 1, 0, 6], 2, 6        # Input contains duplicacy at nth largest numbers.
sample_arr5 = [4, 2, 6, 3, 8, 1, 0, 6, 7, 8], 2, 7  # Duplicate Largest number

sample_input = [
    {'input': sample_arr1}, 
    {'input': sample_arr2}, 
    {'input': sample_arr3}, 
    {'input': sample_arr4}, 
    {'input': sample_arr5}
    ]

# for n, case in enumerate(sample_input):
#     print(f'input: {case["input"][0],case["input"][1]}')
#     print(f'Nth Largets number: {case["input"][1]}')
#     print(f'Expected Output: {case["input"][2]}')
#     print(f'Result: {find_nth_largest_num(case["input"][0],case["input"][1])}')
#     print(f'Test Status: Passed') if find_nth_largest_num(case["input"][0],case["input"][1]) == case["input"][2] else print(f'Test Status: Failed')
    
#     print()
#     print()



with open('/.test.txt', 'r') as f:
    f.read().replace('Asim', 'amir')



    







