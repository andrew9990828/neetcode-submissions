class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        longest = 1
        count = 1
        if not nums:
            return 0
            
        for n in nums:
            seen[n] = 1 + seen.get(n, 0)
            og_num = n
            n -= 1

            while n in seen:
                count += 1
                n -= 1
            
            og_num += 1
            while og_num in seen:
                count += 1
                og_num += 1
            
            longest = max(longest, count)
            count = 1
        
        return longest