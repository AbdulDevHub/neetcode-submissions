class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        # Scan backward from the end of the string
        for i in (range(len(s)-1, -1, -1)):
            if s[i] != ' ':
                length += 1
            elif length > 0:
                # We hit a space AFTER already finding the last word
                return length
        return length
        