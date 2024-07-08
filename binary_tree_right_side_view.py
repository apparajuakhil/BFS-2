"""
# BFS-2

## Problem 1

Binary Tree Right Side View (https://leetcode.com/problems/binary-tree-right-side-view/)

Time Complexity : O(n)
Space Complexity : O(n) ~ diameter of the tree
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Your code here along with comments explaining your approach:
Trick is to follow the same BFS approach of traversing a binary tree using a queue but instead of pushing all the elements
present at the level, push only the last element at the level by using the size-1 condition.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque()
        queue.append(root)

        result = []

        while len(queue) > 0:
            size = len(queue)

            for i in range(size):
                popped_node = queue.popleft()

                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                    queue.append(popped_node.right)

                if i == size-1:
                    result.append(popped_node.val)


        return result
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # O(n) O(h)
        if not root:
            return []

        result = []

        def dfs(root, lvl):
            if not root:
                return 

            if lvl == len(result):
                result.append(root.val)

            dfs(root.right, lvl+1)
            dfs(root.left, lvl+1)

        dfs(root, 0)
        return result
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]: # O(n) O(h)
        if not root:
            return []

        result = []

        def dfs(root, lvl):
            if not root:
                return 

            if lvl == len(result):
                result.append(root.val)
            else:
                result[lvl] = root.val

            dfs(root.left, lvl+1)
            dfs(root.right, lvl+1)

        dfs(root, 0)
        return result