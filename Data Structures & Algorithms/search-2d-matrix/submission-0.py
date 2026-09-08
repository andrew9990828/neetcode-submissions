class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        
        while l <= r:
            m = r - l // 2

            left = 0
            right = len(matrix[m]) - 1
            smallest = matrix[m][0]
            largest = matrix[m][right]

            while left <= right:
                mid = right - left // 2
                point = matrix[m][mid]

                if point == target:
                    return True

                elif point < target:
                    left = mid + 1
                
                else:
                    right = mid - 1
            
            if target < smallest:
                r = m - 1

            elif target > largest:
                l = m + 1
            
            else:
                return False
        
        return False
                
            