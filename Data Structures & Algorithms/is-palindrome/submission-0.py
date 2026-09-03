class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()
        s = s.lower()
        word = ""

        for ch in s:
            if ch.isalnum():
                word += ch

        l = 0 
        r = len(word) - 1

        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        
        return True