from collections import Counter

def find_shortest_substring(main_string, target):
    """
    Find shortest substring in main_string that contains all characters from target.
    
    Example:
    main_string = "HELLO WORLD"
    target = "LO"
    Result: "LO" (shortest part containing 'L' and 'O')
    """
    # Step 1: Count how many times each character appears in target
    needed_chars = Counter(target)
    # Example: if target = "LO", then needed_chars = {'L': 1, 'O': 1}
    
    # Step 2: Initialize variables
    window_start = 0
    current_window = Counter()  # Counts chars in current window
    
    shortest_length = float('inf')
    shortest_substring = ""
    
    # Step 3: Move through the string character by character
    for window_end, char in enumerate(main_string):
        # Add new character to our window
        current_window[char] += 1
        
        # Check if we have all needed characters
        have_all_chars = True
        for needed_char in needed_chars:
            if current_window[needed_char] < needed_chars[needed_char]:
                have_all_chars = False
                break
        
        # If we have all characters, try to make window smaller
        while have_all_chars and window_start <= window_end:
            # Check if this is the shortest valid window so far
            current_length = window_end - window_start + 1
            if current_length < shortest_length:
                shortest_length = current_length
                shortest_substring = main_string[window_start:window_end + 1]
            
            # Remove leftmost character and move window start
            current_window[main_string[window_start]] -= 1
            window_start += 1
            
            # Check if window still has all needed characters
            have_all_chars = True
            for needed_char in needed_chars:
                if current_window[needed_char] < needed_chars[needed_char]:
                    have_all_chars = False
                    break
    
    return shortest_substring

# Test with examples
def test_with_example(main_string, target):
    print(f"\nFinding shortest substring in '{main_string}' containing all chars from '{target}'")
    print(f"Characters needed: {dict(Counter(target))}")
    result = find_shortest_substring(main_string, target)
    print(f"Result: '{result}'")
    
    # Show how result contains all needed characters
    if result:
        print("\nVerification:")
        result_counts = Counter(result)
        target_counts = Counter(target)
        for char in target_counts:
            print(f"Character '{char}': needed {target_counts[char]}, found {result_counts[char]}")

# Run examples
if __name__ == "__main__":
    # Example 1: Simple case
    test_with_example("HELLO WORLD", "LO")
    
    # Example 2: More complex case
    test_with_example("ADOBECODEBANC", "ABC")
    
    # Example 3: Repeated characters
    test_with_example("AAAAAA", "AA")
