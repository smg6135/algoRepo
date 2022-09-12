# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        if root.left is None and root.right is None:
            return [root.val]
        
        res = []

        if root.left is None:
            res += [root.val]
            res += self.inorderTraversal(root.right)
        
        elif root.right is None:
            res += self.inorderTraversal(root.left)
            res += [root.val]
        
        else:
            res += self.inorderTraversal(root.left)
            res += [root.val]
            res += self.inorderTraversal(root.right)
        return res