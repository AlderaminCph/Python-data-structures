import pytest

from day8.merge_two_binary_trees import TreeNode, Solution
from typing import List


@pytest.mark.parametrize(
    ["first_tree", "second_tree", "expected"],
    [
        ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7]),
        ([1], [1, 2], [2, 2]),
    ],
)
def test_merge(
    first_tree: List[int], second_tree: List[int], expected: List[int]
):
    t1 = TreeNode.to_binary_tree(first_tree)
    t2 = TreeNode.to_binary_tree(second_tree)
    Solution_instance = Solution()
    merged_tree = Solution_instance.mergeTrees(t1, t2)
    assert expected == TreeNode.create_list(merged_tree)
