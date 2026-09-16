class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_chars = {}
        for ch in s1:
            s1_chars[ch] = 1 + s1_chars.get(ch, 0)
        
        s2_chars = {}
        k = len(s1)
        l = 0
        for r in range(len(s2)):
            s2_chars[s2[r]] = 1 + s2_chars.get(s2[r], 0)

            if (r - l + 1) > k:
                s2_chars[s2[l]] -= 1
                if s2_chars[s2[l]] == 0:
                    del s2_chars[s2[l]]
                l += 1
            
            if s2_chars == s1_chars:
                return True

        return False