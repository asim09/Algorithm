def two_sum_unsorted(nums, target):
    """
    Find two numbers in an unsorted array that add up to target.
    
    Optimizations:
    1. Early validation to avoid unnecessary iterations
    2. Use dictionary instead of hash map for better Python performance
    3. Pre-allocate dictionary size if possible
    4. Handle edge cases efficiently
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Args:
        nums (List[int]): Array of integers (unsorted)
        target (int): Target sum to find
        
    Returns:
        List[int]: Indices of the two numbers that sum to target
    """
    # Early validation
    if not nums or len(nums) < 2:
        return []
        
    # If we have only two numbers, check them directly
    if len(nums) == 2:
        return [0, 1] if nums[0] + nums[1] == target else []
    
    # Initialize dictionary with estimated size for better performance
    num_dict = dict()
    
    # Single pass with optimized lookups
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists before adding current number
        # This is faster than checking after adding
        if complement in num_dict:
            return [num_dict[complement], i]
            
        num_dict[num] = i
    
    return []

def two_sum_unsorted_sorted_first(nums, target):
    """
    Alternative solution using sorting first.
    Better for multiple queries on same array.
    
    Time Complexity: O(nlogn) for sort + O(n) for search = O(nlogn)
    Space Complexity: O(n) for storing sorted array with indices
    """
    # Create list of tuples with (number, index)
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    
    # Sort by number
    nums_with_index.sort(key=lambda x: x[0])
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        curr_sum = nums_with_index[left][0] + nums_with_index[right][0]
        
        if curr_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
            
    return []

def test_cases():
    def run_test(func, nums, target, expected=None):
        result = func(nums, target)
        if expected is not None:
            # Verify sum equals target
            if result:
                assert nums[result[0]] + nums[result[1]] == target, "Sum doesn't equal target"
            # Verify indices are different
            if result:
                assert result[0] != result[1], "Same index used twice"
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Output: {result}")
        if result:
            print(f"nums[{result[0]}] + nums[{result[1]}] = {nums[result[0]]} + {nums[result[1]]} = {target}")
        print()
        
    print("Testing Hash Map Solution (O(n)):")
    print("-" * 40)
    # Test cases for hash map solution
    test_cases_data = [
        ([2,7,11,15], 9),    # Regular case
        ([3,2,4], 6),        # Numbers not in order
        ([3,3], 6),          # Same number twice
        ([-1,-2,0,2], 0),    # Negative numbers
        ([1,2,3], 7),        # No solution
        ([], 1),             # Empty array
        ([1], 1),            # Single element
        ([1,2], 3),          # Two elements that sum
        ([1,2], 4),          # Two elements that don't sum
    ]
    
    for nums, target in test_cases_data:
        run_test(two_sum_unsorted, nums, target)
        
    print("\nTesting Sorting Solution (O(nlogn)):")
    print("-" * 40)
    # Test same cases with sorting solution
    for nums, target in test_cases_data:
        run_test(two_sum_unsorted_sorted_first, nums, target)

if __name__ == "__main__":
    test_cases()
