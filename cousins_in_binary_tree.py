"""
# BFS-2

## Problem 2

Cousins in binary tree (https://leetcode.com/problems/cousins-in-binary-tree/)

Time Complexity : O(n)
Space Complexity : O(n)
Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

Your code here along with comments explaining your approach:
Trick is to keep 2 variables to identify whether x & y are found or not. Now follow the default approach for the BFS, but once
level traversal is completed check if we found x and y then it's on the same level and in the level iteration we're already checking
if they're siblings so now we can simply go with returning True if they're not true but one of them is true then we can be sure that
both are not present in the same level.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool: #O(n) O(n)
        if not root:
            return False

        x_found = False
        y_found = False

        queue = collections.deque()
        queue.append(root)

        while len(queue) != 0:
            size = len(queue) 

            for i in range(size): # we should not use queue size directly here as we're removing them in the loop
                popped_node = queue.popleft()

                if popped_node.val == x:
                    x_found = True
                
                if popped_node.val == y:
                    y_found = True

                if popped_node.left and popped_node.right:
                    if popped_node.left.val == x and popped_node.right.val == y:
                        return False
                    if popped_node.left.val == y and popped_node.right.val == x:
                        return False
                
                if popped_node.left:
                    queue.append(popped_node.left)
                if popped_node.right:
                    queue.append(popped_node.right)

            if x_found == True and y_found == True: # this should come first
                return True
            if x_found == True or y_found == True:
                return False

        return "B" # junk doesn't matter


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        self.x_depth = -1
        self.y_depth = -1
        self.x_parent = None
        self.y_parent = None
        self.x = x
        self.y = y

        self.dfs(root, 0, None)

        if self.x_depth == self.y_depth and self.x_parent != self.y_parent:
            return True
        
        return False

    def dfs(self, root, level, parent):
        if root is None or (self.x_depth != -1 and self.y_depth != -1): # assuming we already found x or y
            return

        if root.val == self.x:
            self.x_depth = level
            self.x_parent = parent

        if root.val == self.y:
            self.y_depth = level
            self.y_parent = parent

        self.dfs(root.left, level+1, root.val)
        self.dfs(root.right, level+1, root.val)
