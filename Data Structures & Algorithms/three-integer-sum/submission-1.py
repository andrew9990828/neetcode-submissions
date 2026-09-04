class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                calc = nums[l] + nums[r] + n
                if calc == 0:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                    

                elif calc > 0:
                    r -= 1
                else:
                    l += 1
        
        return res
