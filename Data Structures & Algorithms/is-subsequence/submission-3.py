class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (0 == len(s)): return True
        if (len(s) > len(t)): return False
        sCompareIndex = 0
        for tLetter in t:
            if tLetter == s[sCompareIndex]: sCompareIndex += 1
            if sCompareIndex == len(s): return True
        return sCompareIndex == len(s)