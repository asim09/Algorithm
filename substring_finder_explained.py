

class SubstringFinder:
    @classmethod
    def shortest_substring(cls, string, word):
        """
        Find the shortest substring in 'string' that contains all characters from 'word'
        with their required frequencies.
        
        Example:
        string = "ADOBECODEBANC"
        word = "ABC"
        Result: "BANC" (shortest substring containing all characters A, B, and C)
        
        How it works:
        1. Count required characters from 'word'
        2. Use sliding window to find valid substrings
        3. Keep track of minimum valid substring
        """
        # Step 1: Count frequency of characters in word
        required = Counter(word)  # Example: "ABC" -> {'A': 1, 'B': 1, 'C': 1}
        
        # Initialize variables
        left = 0                   # Left pointer of sliding window
        min_len = float('inf')     # Length of shortest valid substring found
        min_sub = ""              # Shortest valid substring found
        window = Counter()        # Counter for current window
        
        # Step 2: Slide window through string
        for right, char in enumerate(string):
            # Add current character to window counter
            window[char] += 1
            
            # Check if window contains all required characters
            while all(window[c] >= required[c] for c in required) and left <= right:
                # If current window is smaller than previous minimum
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_sub = string[left:right+1]
                
                # Shrink window from left
                window[string[left]] -= 1
                left += 1
                
        return min_sub

# Example usage with detailed steps
if __name__ == "__main__":
    # Example 1
    string1 = "ADOBECODEBANC"
    word1 = "ABC"
    result1 = SubstringFinder.shortest_substring(string1, word1)
    print(f"\nExample 1:")
    print(f"String: {string1}")
    print(f"Word: {word1}")
    print(f"Required counts: {Counter(word1)}")
    print(f"Shortest substring: {result1}")
    
    # Example 2
    string2 = "HELLO WORLD"
    word2 = "LO"
    result2 = SubstringFinder.shortest_substring(string2, word2)
    print(f"\nExample 2:")
    print(f"String: {string2}")
    print(f"Word: {word2}")
    print(f"Required counts: {Counter(word2)}")
    print(f"Shortest substring: {result2}")

"""
Detailed Explanation of How It Works:

1. For string "ADOBECODEBANC" and word "ABC":

   required = {'A': 1, 'B': 1, 'C': 1}
   
   Window moves as follows:
   
   A | window = {'A': 1} | Not valid (missing B, C)
   AD | window = {'A': 1, 'D': 1} | Not valid
   ADO | window = {'A': 1, 'D': 1, 'O': 1} | Not valid
   ADOB | window = {'A': 1, 'B': 1, 'D': 1, 'O': 1} | Not valid
   ADOBE | window = {'A': 1, 'B': 1, 'D': 1, 'E': 1, 'O': 1} | Not valid
   ADOBEC | window contains all required -> Valid substring!
   DOBEC | window = {'B': 1, 'C': 1, 'D': 1, 'E': 1, 'O': 1} | Not valid
   ... continues ...
   BANC | window contains all required -> New shortest valid substring!

2. The sliding window technique:
   - Right pointer expands window until we have all required characters
   - Left pointer contracts window while maintaining required characters
   - Keep track of minimum valid window found

3. Counter usage:
   - required: keeps count of characters needed
   - window: keeps count of characters in current window
   - all(window[c] >= required[c] for c in required):
     checks if window has enough of each required character
"""
