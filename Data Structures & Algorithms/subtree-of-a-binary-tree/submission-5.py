# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        
        if root.val == subRoot.val and self.isSametree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)
        


    
    def isSametree(self, p:Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.isSametree(p.left,q.left)
        if not left:
            return False
        right = self.isSametree(p.right,q.right)
        if not right:
            return False
        return True
        
        