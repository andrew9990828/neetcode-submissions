class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = {}
        longest = 1
        count = 1

        if not nums:
            return 0

        for n in nums:
            seen[n] = 1 + seen.get(n, 0)

        for n in nums:

            if n - 1 not in seen:
                count = 0
                cur = n + 1

                while n in seen:
                    count += 1
                    n += 1
                
                longest = max(longest, count)
        
        return longest