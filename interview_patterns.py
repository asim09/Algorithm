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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    
    # Test Tree Operations
    # Create a sample tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("Level Order Traversal:", level_order_traversal(root))
    print("Tree Paths:", tree_paths(root))
    
    # Test Top K Elements
    print("K Largest Elements:", find_k_largest([3, 1, 5, 12, 2, 11], 3))
    
    # Test Search in Rotated Array
    print("Search in Rotated Array:", search_in_rotated_array([4, 5, 6, 7, 0, 1, 2], 0))
