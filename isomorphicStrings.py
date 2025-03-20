# Time Complexity : O(n) where n is the length of the string
# Space Complexity : O(n) where n is the length of the string
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# 1. We will use two hashmaps to store the mapping of the characters of the strings.
# 2. We will iterate through the strings and check if the character is already present in the hashmap.
# 3. If the character is already present in the hashmap, we will check if the mapping of the character is the same as the character in the other string.
# 4. If the mapping is not the same, we will return False.
class TwoMaps:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize two hashmaps to store the mapping of the characters of the strings
        sMap, tMap = {}, {}

        for i in range(len(s)):
            # If the character is already present in sMap, check if the mapping of the character is the same as the character in t
            if s[i] in sMap and sMap[s[i]] != t[i]:
                return False
            # If the character is already present in tMap, check if the mapping of the character is the same as the character in s
            elif t[i] in tMap and tMap[t[i]] != s[i]:
                return False
            # If the character is not present in sMap, add s[i] to sMap and t[i] to tMap
            sMap[s[i]] = t[i]
            tMap[t[i]] = s[i]
        # Return True if the strings are isomorphic
        return True

# Time Complexity : O(n) where n is the length of the string
# Space Complexity : O(n) where n is the length of the string
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# 1. We will use a hashmap and a set to store the mapping of the characters of the strings.
# 2. We will iterate through the strings and check if the character is already present in the hashmap.
# 3. If the character is already present in the hashmap, we will check if the mapping of the character is the same as the character in the other string.
# 4. We will add the values to the set to check if the new value is already mapped to another key in the set.
class MapAndSet:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Initialize a hashmap and a set to store the mapping of the characters of the strings
        map = {}
        valSet = set()
        for i in range(len(s)):
            # Check if the character is already present in the hashmap and if the new value is already mapped to another key in the hashmap
            if (s[i] not in map) and (t[i] in valSet):
                    return False
            # Check if the character is already present in the hashmap and if the value of the key is not the same as the character in string t
            if (s[i] in map and map[s[i]] != t[i]):
                return False
            # Add the key-value pair to the hashmap and the value to the set
            map[s[i]] = t[i]
            valSet.add(t[i])
        # Return True if the strings are isomorphic
        return True