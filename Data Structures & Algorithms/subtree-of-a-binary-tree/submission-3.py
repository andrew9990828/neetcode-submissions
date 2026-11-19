# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node1, node2):
            if node1 is None and node2:
                return False
            if node1 and node2 is None:
                return False
            if node1 is None and node2 is None:
                return True
            if node1.val != node2.val:
                return False
            
            
            left = isSameTree(node1.left, node2.left)
            right = isSameTree(node1.right, node2.right)
            
            return left and right
        
        def dfs(main, sub):
            if main is None:
                return False
            
            if main.val == sub.val:
                if isSameTree(main, sub):
                    return True
                
            left = dfs(main.left, sub)
            right = dfs(main.right, sub)

            return left or right
        
        return dfs(root, subRoot)