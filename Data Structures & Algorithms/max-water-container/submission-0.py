class Solution:
    def maxArea(self, heights: List[int]) -> int:
        most = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            smallest = min(heights[l], heights[r])
            area = smallest * (r - l)

            most = max(area, most)

            if heights[l] == smallest:
                l += 1
            else:
                r -= 1
        
        return most