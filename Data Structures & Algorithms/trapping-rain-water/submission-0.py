class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        water = 0
        lh = 0
        rh = len(height) - 1

        while l < r:
            left, right = height[l], height[r]
            left_side, right_side = height[lh], height[rh]
            smaller_side = min(left,right)

            if smaller_side == left:
                l += 1
                if left_side > height[l]:
                    water += left_side - height[l]
                else:
                    lh = l
            else:
                r -= 1
                if right_side > height[r]:
                    water += right_side - height[r]
                else:
                    rh = r
        
        return water