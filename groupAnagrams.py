# Time Complexity : O(n * k) where n is the number of strings and k is the length of the longest string
# Space Complexity : O(n) where n is the number of strings
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Approach:
# 1. We are going to use prime product method.
# 2. We will generate prime numbers and assign each character a prime number.
# 3. We will calculate the prime product of each string and store the strings with the same prime product in a hashmap.
from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We are going to use prime product method
        def prime(i, primes):
            for prime in primes:
                if not (i == prime or i % prime):
                    return False
            primes.add(i)
            return i
        # function to generate prime numbers
        def getPrimes(n):
            primes = set([2])
            i, p = 2, 0
            while True:
                if prime(i, primes):
                    p += 1
                    if p == n:
                        return primes
                i += 1

        # Initialize a hashmap to store the anagrams
        anagrams = defaultdict(list)
        # Get the prime numbers
        primes = list(getPrimes(26))
        for i in range(len(strs)):
            prime = 1
            # Calculate the prime product of each string
            for c in strs[i]:
                prime = prime * primes[ord(c) - ord('a')]
            # Append the string to the list
            anagrams[prime].append(strs[i])
        # Return the values of the hashmap
        return list(anagrams.values())