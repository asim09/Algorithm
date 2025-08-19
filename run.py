def longest_substring_without_repeating(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Example: s = "abcabcbb"
    When we find duplicate 'a':
    - Previous 'a' was at index 0
    - Current window starts at index 0
    - Move window to start after previous 'a' (index 1)
    """
    if not s:
        return 0
    
    char_index = {}  # stores last position of each character
    window_start = 0
    max_length = 0
    
    for i, char in enumerate(s):
        # If we find a duplicate character
        last_seen = char_index.get(char, -1)  # -1 if char not seen before
        if last_seen >= window_start:
            # Move window to start after the last occurrence
            window_start = last_seen + 1
        
        # Update max length and character's last position
        max_length = max(max_length, i - window_start + 1)
        char_index[char] = i
    
    return max_length

print(longest_substring_without_repeating('abcabcbb'))




# from threading import Thread
# from requests import request


# #  Function

# URLS = ['url1', 'url2', 'url3']

# def fetch_file_data():
#     file_data = request.get(url=URLS)
#     # Further code


# def fetch_data_load():
#     data = Thread(target=fetch_file_data, URLS=URLS)
#     # Further code




# # Cases
# # Too much time taking
# # File curropt
# # Error Handling
# # Retries





# input_string = "ABCDEFA"
# output = "BCDEF"

# def find_longest_substring(input_string):
#     seen = {}
#     for char in input_string:
#         longest_string = ""
#         if char in seen:
#             char_kesy_in_seen = list(seen.keys())
#             # make a string from  list char_kesy_in_seen:
#             for element in char_kesy_in_seen:
#                 longest_string = longest_string + element
#         else:
#             seen[char] = 1

#     return longest_string

# print(find_longest_substring(input_string))




# import requests
# from concurrent.futures import ThreadPoolExecutor, TimeoutError

# # Function to download a file with a timeout
# def download_file(url, timeout):
#     try:
#         # Use requests with a timeout for the download
#         response = requests.get(url, stream=True, timeout=timeout)
#         filename = url.split("/")[-1]

#         # Save the content to a file
#         with open(filename, "wb") as file:
#             for chunk in response.iter_content(chunk_size=8192):
#                 file.write(chunk)

#         print(f"Downloaded: {filename}")
#     except requests.exceptions.Timeout:
#         print(f"Download of {url} timed out.")
#     except Exception as e:
#         print(f"Failed to download {url}: {e}")

# # List of URLs to download
# urls = [
#     'https://example.com/file1.zip',
#     'https://example.com/file2.jpg',
#     'https://example.com/file3.pdf'
# ]

# # Set the timeout duration in seconds for each download
# timeout_limit = 10  # Timeout after 10 seconds

# # Function to download files concurrently using ThreadPoolExecutor
# def download_files_concurrently(urls, timeout):
#     # Create a ThreadPoolExecutor to manage concurrent downloads
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         # Submit download tasks with a timeout for each URL
#         futures = [executor.submit(download_file, url, timeout) for url in urls]
        
#         for future in futures:
#             try:
#                 # Wait for the download to complete and check if it raised any exceptions
#                 future.result(timeout=timeout)
#             except TimeoutError:
#                 print(f"A download took too long and was terminated.")
#             except Exception as e:
#                 print(f"Error during download: {e}")

# # Call the function to download files concurrently
# download_files_concurrently(urls, timeout_limit)

# print("Downloads completed (or terminated if timed out).")



string = "python is a open sourec language"
result = "y"

def find_f_occ(string):
    temp = {}
    for i in string:
        temp[i] = temp.get(i, 0) + 1
        print(temp)

print(find_f_occ(string))








# test_str = "GeeksForGeeks"
# position = 3


# def pop_character(test_str, position):
#     print(test_str[:position] )
#     res = test_str[:position] + test_str[position + 1 :]
#     return res

# print(pop_character(test_str, position))

# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
    
# for i in range(10, 100):
#     if is_prime(i):
#         print(i)

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):  # Check till square root of the number
#         if num % i == 0:
#             return False
#     return True

# # Print prime numbers between 10 and 100
# for i in range(10, 101):
#     if is_prime(i):
#         print(i)


# nums = [2, 7, 11, 15]
# target = 9

# def two_sum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
# print(two_sum(nums, target))
# def remove_second_occurrence(lst):
#     temp = {}
#     n = 0
#     while n < len(lst):
#         i = lst[n]
#         temp[i] = temp.get(i, 0) + 1
#         print(temp)
        
#         # Remove the second occurrence
#         # if temp[i] == 2:
#         #     del lst[n]
#         #     continue  # Don't increment `n` as the list has shifted

#         print('after continiue', lst[n])
#         n += 1

#     return lst

# l = ['a', 'b', 'c', 'a', 'b']
# remove_second_occurrence(l)

# @decorate_name
# def chnage_name(name):
#     "This is decorated"
#     return name

# print(chnage_name('asim'))
# print(chnage_name.__name__)
# print(chnage_name.__doc__)
# def fibonacci():
#     a,b = 0,1
#     while True:
#         yield a
#         a,b = b , a + b
# def call_me(num):
#     f = fibonacci()
#     for _ in range(num):
#         print(next(f))
# call_me(10)

# import time

# from functools import wraps

# def timer(func):
#     @wraps(func)
#     def wrapper(*a, **b):
#         s = time.time()
#         res = func(*a, **b)
#         e = time.time()
#         ex_t = e - s
#         print(f"Execution time: {e - s:.2f} seconds")
#         return res
#     return wrapper



# @timer
# def slow(sec):
#     time.sleep(sec)
#     print('something')

# print(slow(3))







# numerator = [1, 2, 3, 4]
# denominator = [2, 5, 4, 8]
# fractions = list(zip(numerator, denominator))
# sorted_fractions = sorted(fractions, key=lambda x: x[0] / x[1])
# sorted_numerator, sorted_denominator = zip(*sorted_fractions)
# print(type(sorted_numerator))
# print(sorted_denominator)


# a = [0, 1,1,1,0,0,1,0,1]
# z = [x for x in a if x == 0]  
# y = [x for x in a if x == 1]
# b = z+y
# print(b)

# for num in range(1, 101):
#     is_prime = True
#     if num > 1:
#         # Check if the number is divisible by any number from 2 to num-1
#         for i in range(2, num):
#             if num % i == 0:
#                 # If the number is divisible, then it is not a prime number
#                 is_prime = False
#                 break
#     if is_prime:
#         print("prime hai", num)


# # from coun
# "14.Find the first non repeating character"

# string = "python is a open sourec language"Cascade | Write mode (Ctrl + .)
# result = "y"

# def foo(s):
#     t = {}
#     for i in s:
#         if not i.isspace():
#             t[i] = t.get(i, 0) + 1
#     first_key = next((key for key, val in t.items() if val == 1), None)
#     print(first_key)
# foo(string)



# def is_prime(n):
#     """Check if a number is prime"""
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def get_primes(start, end):
#     return [num for num in range(start, end + 1) if is_prime(num)]

# primes = get_primes(1, 100)
# print(primes)


# sample_dict = {"a": "A", "b": 2, "c": 3, "d": "c"}

# "Method-1"


# def frequncy(sample_dict):
#     resultant_dic = {}
#     sample_list = list(sample_dict.keys()) + list(sample_dict.values())

#     for elem in sample_list:
#         resultant_dic[elem] = resultant_dic.get(elem, 0) + 1

#     print(resultant_dic)
# frequncy(sample_dict)

















# import functools

# def authenticate(get_user_role):
#     def decorator(func):
#         @functools.wraps(func)  # This will preserve the metadata of 'func'
#         def wrapper(*args, **kwargs):
#             # Dynamically get the user role
#             user_role = get_user_role()
#             if user_role != "admin":
#                 print("Access denied: You are not an admin!")
#                 return None
#             return func(*args, **kwargs)
#         return wrapper
#     return decorator

# # Simulating a function to get user role dynamically
# def get_current_user_role():
#     # For simplicity, return a hardcoded role
#     # Replace this with logic to fetch the actual user role (e.g., from a session)
#     return "guest"  # Change this to "admin" to grant access

# class App:
#     @authenticate(get_current_user_role)
#     def admin_dashboard(self):
#         print("Accessing admin dashboard")

#     @authenticate(get_current_user_role)
#     def guest_page(self):
#         print("Accessing guest page")

# app = App()
# app.admin_dashboard()  # Output: Access denied: You are not an admin!
# app.guest_page()       # Output: Access denied: You are not an admin!










# def authorize(get_current_user_role):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, ** kwargs):
#             role = get_current_user_role()
#             if role != "admin":
#                 print("Access denied to Admin dash")
#                 return None
                
#             return func(*args, ** kwargs)
#         return wrapper
#     return decorator

# from functools import wraps
# def get_current_user_role():
#     return "guest"


# class App:

#     @authorize(get_current_user_role)
#     def admin_dash(self):
#         print("Accessing admin dash")

#     @authorize(get_current_user_role)
#     def guest_dash(self):
#         print("Accessing guest dash")

# app = App()
# # app.admin_dash()
# app.guest_dash()

# def authorization(user_role):
#     def decorator(func):
#         def wrapper(*a, **b):
#             if user_role != "admin":
#                 print("Access denied, not admin")
#                 return None
#             return func(*a, **b)
#         return wrapper
#     return decorator



# class App:
#     @authorization("admin")
#     def admin_dash(self):
#         print("Accessing Admin Dash")

#     @authorization("guest")
#     def guest_dash(self):
#         print("Accessing Guest Dash")

# app = App()
# # app.admin_dash()
# app.guest_dash()

def remove_second_occurrence(lst):
    temp = {}
    n = 0
    while n < len(lst):
        i = lst[n]
        temp[i] = temp.get(i, 0) + 1
        
        # Remove the second occurrence
        # if temp[i] == 2:
        #     del lst[n]
        #     continue  # Don't increment `n` as the list has shifted

        print('after continiue', lst[n])
        n += 1

    return lst

l = ['a', 'b', 'c', 'a', 'b']
# print(remove_second_occurrence(l))  # Output: ['a', 'b', 'c']






# from pprint import pprint
# def rent():
#     initial_rent = 72000*12
#     roi = 5
#     new_rent = 0
#     sum = 0
#     anuula_rent_list = []
#     tenure = 25

#     for i in range(tenure):
#         anuula_rent_list.append(initial_rent)
#         sum = sum + initial_rent
#         print(f"Rent for {i + 1} year----> {initial_rent} | Monthly is {initial_rent//12}")
#         cal_next_year_rent = initial_rent + (initial_rent*roi*1)//100
#         initial_rent = cal_next_year_rent
#     print(f"Total rent paid--->{sum}")
#     return sum, anuula_rent_list

# print(rent())

# def first_element():
#     st = 'SILVER FOR SILVER'
#     d = {}
#     for i in st:
#         if i not in d.keys():
#             d[i] = 1
#         else:
#             d[i] = d[i] + 1
#     print(d)
#     for j, k in d.items():
#         if k == 1:
#             return j

# print(first_element())




# def sort013(array):
#     array_len = len(array)
#     lo, mid = 0, 0
#     hi = array_len - 1
#     while mid <=hi:
#         if array[mid] == 0:
#             array[lo], array[mid] = array[mid], array[lo]
#             lo+=1
#             mid+=1
#             print(array)
            
#         elif array[mid] == 1:
#             mid+=1
#             print(array)
#     return arr
# arr = [1, 1, 1, 0, 1, 1, 0, 1, 1]
# print(sort013(arr))

















# def fact(num):
#     if num == 0 or num == 1:
#         return 1

#     else:
#         return num * fact(num -1)
    
# print(fact(5))


# sample_list = [1, 2, 3, 3, 3, 4, 1, 10, 5, 6, 7, 8, 8, 9, 10, 12]
# iterator = sample_list[0]
# missing_list = []
# duplicate_list = []

# for num in sample_list:
#     print(num, iterator)

#     if iterator < num:
#         missing_list.append(iterator)
#         iterator += 2

#     elif iterator > num:
#         duplicate_list.append(num)

#     elif iterator == num:
#         iterator += 1

# print(missing_list, duplicate_list)



# a = [1, 2, 3, 4, 5]
# sum = 0
# new_list = []
# for i in a:
#     sum = sum + i
#     new_list.append(sum)
# print(new_list)


# x = "AABCCDE"


# stack = []

# for i in x:
#     if stack and stack[-1] == i:
#         stack.pop()
#     else:
#         stack.append(i)

# print(stack)






# from collections import Counter

# data = ["geeks", "for", "geeks"]

# def find_dup_and_remove(input):
#     d1 = Counter(input)
#     duplicates = [i for i, j in d1.items() if j > 1]
#     d2 = list(dict.fromkeys(data))
#     return duplicates, d2


# print(find_dup_and_remove(data))



# a = 'ab cd'

# l = len(a.replace(' ', ''))
# print(l)




data = [
    {
        "eid": 95,
        "weekStartdate": "2021-03-18 12:40:11",
        "workHours": 12.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 95,
        "weekStartdate": "2021-03-19 12:40:11",
        "workHours": 11.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 95,
        "weekStartdate": "2021-03-20 12:40:11",
        "workHours": 10.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 97,
        "weekStartdate": "2021-03-17 12:40:11",
        "workHours": 8.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    },
    {
        "eid": 97,
        "weekStartdate": "2021-03-21 12:40:11",
        "workHours": 9.0,
        "test": "No value",
        "test1": "some value",
        "test3": "total value",
    }
]
# res = sorted(data, key=lambda x: x['workHours'])
# import json
# print(json.dumps(res, indent=4))
# list = ['hello', 'king', 'word', 'sword','swear', 'hi']

# res_dict = {}

# for obj in list:
#     if obj[0] not in res_dict.keys():
#         res_dict[obj[0]]  = []
#         res_dict[obj[0]].append(obj)
#     else:
#         res_dict[obj[0]].append(obj)
# print(res_dict)





# grades = ["A", "A", "B", "C", "D", "C", "B", "C", "A", "C", "B"]

# res_dict = {}

# for grade in grades:
#     if grade not in res_dict.keys():
#         res_dict[grade] = 1
#     res_dict[grade] = res_dict[grade]  + 1

# print(res_dict)

# input = 'asim'
# output = '?asim#'

# def append_char(func):
#     def inner(user_input):
#         s = '?' + user_input + '*'
#         return func(s)
#     return inner

# @append_char
# def alter_name(user_name):
#     return user_name
# print(alter_name(input))



# sample_list = [1,3,7,9,2]
# target_sum = 11

# def finsd_sum(sample_list, target_sum):
#     p1 = 0
#     target = target_sum - p1
#     for i in range(len(sample_list)):
#         for j in range(len(sample_list)):
#             if j < len(sample_list) - 1:
#             # j = i + 1
#                 print(sample_list[i], sample_list[j + 1])
#             # j = j + 1
#             # print(j)
#             # print()

#     return None

# finsd_sum(sample_list, target_sum)

# Different approaches to solve Two Sum problem

def two_sum_brute_force(nums, target):
    """
    Approach 1: Brute Force
    Time Complexity: O(n²) - nested loops
    Space Complexity: O(1) - constant space
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_two_pass_hash(nums, target):
    """
    Approach 2: Two-pass Hash Table
    Time Complexity: O(n) - two passes through array
    Space Complexity: O(n) - hash table
    """
    hash_map = {}
    # First pass to build hash map
    for i in range(len(nums)):
        hash_map[nums[i]] = i
    # Second pass to find complement
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_map and hash_map[complement] != i:
            return [i, hash_map[complement]]
    return []

def two_sum_one_pass_hash(nums, target):
    """
    Approach 3: One-pass Hash Table (Most Efficient)
    Time Complexity: O(n) - single pass
    Space Complexity: O(n) - hash table
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def two_sum_sorted(nums, target):
    """
    Approach 4: Two Pointers (requires sorted array)
    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(1) if not counting the space for sorting
    Note: Returns values that sum to target, not indices
    """
    nums_sorted = sorted(nums)
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums_sorted[left] + nums_sorted[right]
        if current_sum == target:
            return [nums_sorted[left], nums_sorted[right]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Example usage and testing
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    
    print("Brute Force:", two_sum_brute_force(nums, target))
    print("Two-pass Hash:", two_sum_two_pass_hash(nums, target))
    print("One-pass Hash:", two_sum_one_pass_hash(nums, target))
    print("Two Pointers (sorted):", two_sum_sorted(nums, target))

# Common Interview Problem Patterns

"""
Here are some of the most common patterns in coding interviews:

1. Two Pointers Pattern
2. Sliding Window Pattern
3. Fast & Slow Pointers Pattern
4. Merge Intervals Pattern
5. Cyclic Sort Pattern
6. In-place Reversal of Linked List Pattern
7. Tree BFS Pattern
8. Tree DFS Pattern
9. Binary Search Pattern
10. Top K Elements Pattern
"""

# Pattern 1: Two Pointers
def reverse_array(arr):
    """
    Two Pointers Pattern: Array Reversal
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Pattern 2: Sliding Window
def max_sum_subarray(arr, k):
    """
    Sliding Window Pattern: Find max sum subarray of size k
    Time: O(n), Space: O(1)
    """
    max_sum = window_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum

# Pattern 3: Fast & Slow Pointers
def has_cycle(head):
    """
    Fast & Slow Pointers Pattern: Detect cycle in linked list
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Pattern 4: Merge Intervals
def merge_intervals(intervals):
    """
    Merge Intervals Pattern: Merge overlapping intervals
    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged

# Pattern 5: Binary Search
def binary_search(arr, target):
    """
    Binary Search Pattern: Find target in sorted array
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Pattern 6: BFS in Binary Tree
from collections import deque

def level_order_traversal(root):
    """
    Tree BFS Pattern: Level order traversal
    Time: O(n), Space: O(n)
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    return result

# Pattern 7: DFS in Binary Tree
def tree_paths(root):
    """
    Tree DFS Pattern: Find all root-to-leaf paths
    Time: O(n), Space: O(h) where h is height
    """
    def dfs(node, path, paths):
        if not node:
            return
        
        path.append(str(node.val))
        
        if not node.left and not node.right:
            paths.append('->'.join(path))
        else:
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)
            
        path.pop()
    
    paths = []
    dfs(root, [], paths)
    return paths

# Pattern 8: Top K Elements
import heapq

def find_k_largest(nums, k):
    """
    Top K Elements Pattern: Find k largest elements
    Time: O(n log k), Space: O(k)
    """
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap

# Pattern 9: Modified Binary Search
def search_in_rotated_array(arr, target):
    """
    Modified Binary Search Pattern: Search in rotated sorted array
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
            
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

# Pattern 10: Cyclic Sort
def cyclic_sort(nums):
    """
    Cyclic Sort Pattern: Sort numbers from 1 to n
    Time: O(n), Space: O(1)
    """
    i = 0
    while i < len(nums):
        correct_pos = nums[i] - 1
        if nums[i] != nums[correct_pos]:
            nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
        else:
            i += 1
    return nums

# Example usage and testing
if __name__ == "__main__":
    # Test Two Pointers
    print("Two Pointers - Array Reversal:", reverse_array([1, 2, 3, 4, 5]))
    
    # Test Sliding Window
    print("Sliding Window - Max Sum Subarray:", max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 3))
    
    # Test Binary Search
    print("Binary Search:", binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    
    # Test Cyclic Sort
    print("Cyclic Sort:", cyclic_sort([3, 1, 5, 4, 2]))
    
    # Test Merge Intervals
    print("Merge Intervals:", merge_intervals([[1,3], [2,6], [8,10], [15,18]]))
