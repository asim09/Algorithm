def longest_substring_without_repeating(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Let's walk through each iteration with example string "abcabcbb":
    
    Iteration 1: char = 'a' (index 0)
        window_start = 0
        current_window = "a"
        char_index = {'a': 0}
        max_length = 1
        max_substring = "a"
    
    Iteration 2: char = 'b' (index 1)
        window_start = 0
        current_window = "ab"
        char_index = {'a': 0, 'b': 1}
        max_length = 2
        max_substring = "ab"
    
    Iteration 3: char = 'c' (index 2)
        window_start = 0
        current_window = "abc"
        char_index = {'a': 0, 'b': 1, 'c': 2}
        max_length = 3
        max_substring = "abc"
    
    Iteration 4: char = 'a' (index 3)
        Found duplicate 'a' at index 0
        window_start = 1 (move after previous 'a')
        current_window = "bca"
        char_index = {'a': 3, 'b': 1, 'c': 2}
        max_length = 3
        max_substring = "abc"
    
    Iteration 5: char = 'b' (index 4)
        Found duplicate 'b' at index 1
        window_start = 2 (move after previous 'b')
        current_window = "cab"
        char_index = {'a': 3, 'b': 4, 'c': 2}
        max_length = 3
        max_substring = "abc"
    
    Iteration 6: char = 'c' (index 5)
        Found duplicate 'c' at index 2
        window_start = 3 (move after previous 'c')
        current_window = "abc"
        char_index = {'a': 3, 'b': 4, 'c': 5}
        max_length = 3
        max_substring = "abc"
    
    Iteration 7: char = 'b' (index 6)
        Found duplicate 'b' at index 4
        window_start = 5 (move after previous 'b')
        current_window = "cb"
        char_index = {'a': 3, 'b': 6, 'c': 5}
        max_length = 3
        max_substring = "abc"
    
    Iteration 8: char = 'b' (index 7)
        Found duplicate 'b' at index 6
        window_start = 7 (move after previous 'b')
        current_window = "b"
        char_index = {'a': 3, 'b': 7, 'c': 5}
        max_length = 3
        max_substring = "abc"
    
    Final result: "abc" with length 3
    """
    if not s:
        return ""
    
    char_index = {}
    window_start = 0
    max_length = 0
    max_substring_start = 0
    
    for i, char in enumerate(s):
        # If we find a duplicate character in current window
        last_seen = char_index.get(char, -1)
        if last_seen >= window_start:
            window_start = last_seen + 1
        
        # Update max length and substring start if current window is longer
        current_length = i - window_start + 1
        if current_length > max_length:
            max_length = current_length
            max_substring_start = window_start
        
        char_index[char] = i
    
    return s[max_substring_start:max_substring_start + max_length]

def test_cases():
    """Test cases with actual substrings"""
    test_data = [
        ("abcabcbb", "abc"),    # Explained in detail in docstring
        ("bbbbb", "b"),         # All same characters
        ("pwwkew", "wke"),      # Longest substring in middle
        ("", ""),               # Empty string
        ("abba", "ab"),         # Immediate duplicate
        ("aab", "ab"),          # Duplicate at start
        ("dvdf", "vdf"),        # Duplicate in middle
    ]
    
    for input_str, expected in test_data:
        result = longest_substring_without_repeating(input_str)
        print(f"Input: '{input_str}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}'")
        print("-" * 30)

if __name__ == "__main__":
    test_cases()
