"""
617. Merge Two Binary Trees

You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover
the other, some nodes of the two trees are
overlapped while the others are not.
You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap,
then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]

"""

from typing import Optional, List
import doctest

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"val: {self.val}, left: {self.left}, right: {self.right}"

    def __str__(self) -> str:
        return str(self.val)

    def to_binary_tree(items: List[int]):
        """Create BT from list of values."""
        n = len(items)
        if n == 0:
            return None

        def inner(index: int = 0) -> TreeNode:
            """Closure function using recursion bo build tree"""
            if n <= index or items[index] is None:
                return None

            node = TreeNode(items[index])
            node.left = inner(2 * index + 1)
            node.right = inner(2 * index + 2)
            return node

        return inner()

    def create_list(tree, templist=[]):
        """
        >>> tree = TreeNode(2, TreeNode(29, TreeNode(26)),\
        TreeNode(4, None, TreeNode(2, TreeNode(9))))
        >>> TreeNode.create_list(tree)
        [2, 29, 4, 26, None, None, 2, None, None, \
None, None, None, None, 9, None]

        """
        items = []
        queue = [tree]

        while queue:
            copy = queue[:]
            queue = []

            for item in copy:
                if item is None:
                    items.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    items.append(item.val)
                    queue.append(item.left)
                    queue.append(item.right)

            if all((x is None for x in queue)):
                break
        if items[-1] is None:
            items = items[:-1]
        return items


class Solution:
    def mergeTrees(
        self, t1: Optional[TreeNode], t2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not t1:
            return t2

        if not t2:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


doctest.testmod()
