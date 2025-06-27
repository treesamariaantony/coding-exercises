'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true'''
# Option 1: using sorting
    # return sorted(s) == sorted(t)
    # Time complexity: O(n log n) for sorting s + O(n log n) for sorting t + O(n) for comparing = O(n log n)
    # Space complexity: O(n) due to sorted lists

# Option 2: using Counter
    # Counts characters in both strings and compares the dictionaries
    # Time complexity: O(n) — building and comparing frequency counts
    # Space complexity: O(n) — for the frequency dictionaries
    
from collections import Counter

def isAnagram(s:str, t:str) -> bool:
    return Counter(s) == Counter(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))

