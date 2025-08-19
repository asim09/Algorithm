def remove_duplicates(arr):
    """
    Remove duplicates from a sorted array in-place and return the length of unique elements.
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - modifying array in-place
    
    Example walkthrough with arr = [2, 3, 3, 3, 6, 9, 9]:
    
    Initial: arr = [2, 3, 3, 3, 6, 9, 9]
             i = 1, next_non_dupe = 1
    
    Step 1: arr[0] = 2 ≠ arr[1] = 3
           Keep arr[next_non_dupe] = 3
           next_non_dupe = 2, i = 2
           arr = [2, 3, 3, 3, 6, 9, 9]
    
    Step 2: arr[1] = 3 = arr[2]
           Skip duplicate, i = 3
           arr = [2, 3, 3, 3, 6, 9, 9]
    
    Step 3: arr[1] = 3 = arr[3]
           Skip duplicate, i = 4
           arr = [2, 3, 3, 3, 6, 9, 9]
    
    Step 4: arr[1] = 3 ≠ arr[4] = 6
           Place 6 at next_non_dupe
           next_non_dupe = 3, i = 5
           arr = [2, 3, 6, 3, 6, 9, 9]
    
    Step 5: arr[2] = 6 ≠ arr[5] = 9
           Place 9 at next_non_dupe
           next_non_dupe = 4, i = 6
           arr = [2, 3, 6, 9, 6, 9, 9]
    
    Step 6: arr[3] = 9 = arr[6]
           Skip duplicate, i = 7
           arr = [2, 3, 6, 9, 6, 9, 9]
    
    Return: 4 (length of unique elements [2, 3, 6, 9])
    
    Args:
        arr (List[int]): Sorted array of integers
        
    Returns:
        int: Length of array after removing duplicates
    """
    if not arr:
        return 0
        
    # Start from index 1 as first element is always unique
    i = 1
    # Position where we'll place the next non-duplicate
    next_non_dupe = 1
    
    while i < len(arr):
        # If current element is different from previous unique element
        if arr[next_non_dupe - 1] != arr[i]:
            # Place current element at next_non_dupe position
            arr[next_non_dupe] = arr[i]
            next_non_dupe += 1
        i += 1
    
    return next_non_dupe

def test_remove_duplicates():
    # Test case 1
    arr1 = [2, 3, 3, 3, 6, 9, 9]
    length1 = remove_duplicates(arr1)
    print(f"Test case 1:")
    print(f"Input array: [2, 3, 3, 3, 6, 9, 9]")
    print(f"Length of unique elements: {length1}")
    print(f"First {length1} elements: {arr1[:length1]}\n")
    
    # Test case 2
    arr2 = [2, 2, 2, 11]
    length2 = remove_duplicates(arr2)
    print(f"Test case 2:")
    print(f"Input array: [2, 2, 2, 11]")
    print(f"Length of unique elements: {length2}")
    print(f"First {length2} elements: {arr2[:length2]}\n")
    
    # Additional test cases
    # Test case 3: Empty array
    arr3 = []
    length3 = remove_duplicates(arr3)
    print(f"Test case 3 (Empty array):")
    print(f"Length: {length3}\n")
    
    # Test case 4: No duplicates
    arr4 = [1, 2, 3, 4]
    length4 = remove_duplicates(arr4)
    print(f"Test case 4 (No duplicates):")
    print(f"Input array: [1, 2, 3, 4]")
    print(f"Length of unique elements: {length4}")
    print(f"First {length4} elements: {arr4[:length4]}")

if __name__ == "__main__":
    test_remove_duplicates()
