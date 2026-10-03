# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(r, s):
            if r is None and s is None:
                return True
            
            if r and s and r.val == s.val:
                return (sameTree(r.left, s.left) and 
                    sameTree(r.right, s.right))
            
            return False

        def dfs(r, s):
            if s is None: return True
            if r is None: return False

            if sameTree(r,s):
                return True
            
            return dfs(r.left, s) or dfs(r.right, s)
        
        return dfs(root, subRoot)
