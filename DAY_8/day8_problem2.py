# Symmetric Tree (Medium)
# This solution uses recursion to compare nodes at opposite ends of the tree.
# It ensures that the left subtree is a mirror reflection of the right subtree.
class Solution(object):
    def real(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val==right.val and self.real(left.left,right.right) and self.real(left.right,right.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root==None):
            return True
        return self.real(root.left,root.right)
