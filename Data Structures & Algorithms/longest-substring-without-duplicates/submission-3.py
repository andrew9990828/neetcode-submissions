class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        l = 0
        longest = 0

        for r, ch in enumerate(s):
            if ch in seen:
                longest = max(longest, r - l)
                while ch in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(ch)
            else:
                seen.add(ch)
        
        return max(longest, len(seen))
                