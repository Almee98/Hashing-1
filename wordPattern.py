# Time Complexity : O(n) where n is the length of the input string s
# Space Complexity : O(n) where n is the length of the input string
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# We use two hashmaps to store the mapping of pattern to string and string to pattern.
# If the length of the pattern and string is not equal, we return False, becaue the mapping is not possible.
# If the pattern character is in the pattern hashmap and the mapping is not equal to the string character, we return False.
# If the string character is in the string hashmap and the mapping is not equal to the pattern character, we return False.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the input string by space and store it in a list for easy access
        s = s.split(" ")
        # Initialize two hashmaps to store the mapping of pattern to string and string to pattern
        pMap, sMap = {}, {}
        # If the length of the pattern and string is not equal, return False
        if len(pattern) != len(s):
            return False
        # Iterate through the pattern and string
        for i in range(len(s)):
            # If the pattern character is in the pattern hashmap and the mapping is not equal to the string character, return False
            if pattern[i] in pMap and pMap[pattern[i]] != s[i]:
                return False
            # If the string character is in the string hashmap and the mapping is not equal to the pattern character, return False
            if s[i] in sMap and sMap[s[i]] != pattern[i]:
                return False
            # Store the mapping of pattern to string and string to pattern
            pMap[pattern[i]] = s[i]
            sMap[s[i]] = pattern[i]
        # If the mapping is possible, return True
        return True