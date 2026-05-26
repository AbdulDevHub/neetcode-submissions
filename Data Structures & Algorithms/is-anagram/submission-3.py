from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # A one-liner that builds hash maps of the character counts and compares them
        return Counter(s) == Counter(t)