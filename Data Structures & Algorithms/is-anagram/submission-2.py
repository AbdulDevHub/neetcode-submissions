class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        seen_letters = []
        for i in range(len(s)):
            if s[i] not in seen_letters:
                # Count occurrences using split, matching your TypeScript logic
                a_letter_in_s_count = s.count(s[i])
                a_letter_in_t_count = t.count(s[i])
                
                if a_letter_in_s_count != a_letter_in_t_count: return False
                seen_letters.append(s[i]) # Python uses append instead of push
                
        return True