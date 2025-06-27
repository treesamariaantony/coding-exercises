'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true'''


def isAnagram(s:str, t:str) -> bool:
    return sorted(s) == sorted(t)

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))