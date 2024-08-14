# Binary Tree Level Order Traversal (Medium)
# This solution utilizes a queue (deque) to perform a level-order traversal of the binary tree.
# Nodes are visited level by level, and each level is stored in a list.
from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        Q = deque([root])
        levels = [[root.val]]
        temp = deque()

        while Q:
            node = Q.popleft()
            if node.left: temp.append(node.left)
            if node.right: temp.append(node.right)
            
            if not Q:
                if temp:
                    levels.append([n.val for n in temp])
                Q = temp
                temp = deque()

        return levels
