def twoSum(numbers, target):
    """
    Find two numbers in a sorted array that add up to target.
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only using two pointers
    
    Example walkthrough with numbers = [2,7,11,15] and target = 9:
    
    Iteration 1:
        left = 0, right = 3
        numbers[left] = 2, numbers[right] = 15
        sum = 17 > target(9), so move right pointer left
    
    Iteration 2:
        left = 0, right = 2
        numbers[left] = 2, numbers[right] = 11
        sum = 13 > target(9), so move right pointer left
    
    Iteration 3:
        left = 0, right = 1
        numbers[left] = 2, numbers[right] = 7
        sum = 9 == target(9), found answer!
        return [1, 2] (1-indexed positions)
    
    Args:
        numbers (List[int]): Sorted array of integers (1-indexed)
        target (int): Target sum to find
    Returns:
        List[int]: 1-indexed positions of the two numbers that sum to target
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        
        # For debugging/understanding, uncomment these print statements:
        # print(f"left={left}, right={right}")
        # print(f"numbers[left]={numbers[left]}, numbers[right]={numbers[right]}")
        # print(f"sum={curr_sum}, target={target}\n")
        
        if curr_sum == target:
            # Return 1-indexed positions
            return [left + 1, right + 1]
        elif curr_sum < target:
            # Current sum too small, need larger number
            # Example: if sum=4 < target=6, moving left pointer right
            # will give us a larger number since array is sorted
            left += 1
        else:
            # Current sum too large, need smaller number
            # Example: if sum=13 > target=9, moving right pointer left
            # will give us a smaller number since array is sorted
            right -= 1
    
    return []  # Not found (though problem guarantees a solution exists)

def test_cases():
    # Test case 1: Regular case
    print("Test case 1: [2,7,11,15], target=9")
    result = twoSum([2,7,11,15], 9)
    print(f"Result: {result}\n")
    assert result == [1,2]
    
    # Test case 2: Target at end of array
    print("Test case 2: [2,3,4], target=6")
    result = twoSum([2,3,4], 6)
    print(f"Result: {result}\n")
    assert result == [1,3]
    
    # Test case 3: Negative numbers
    print("Test case 3: [-1,0], target=-1")
    result = twoSum([-1,0], -1)
    print(f"Result: {result}\n")
    assert result == [1,2]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_cases()
