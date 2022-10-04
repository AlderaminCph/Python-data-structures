import pytest
from day10_recursion_backtracking.reversed_linked_list import (
    Solution,
    LinkedList,
)
from typing import List


@pytest.mark.parametrize(
    ["initial_list", "reverse_list"],
    [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2], [2, 1]), ([], [])],
)
def test_reverse_list(initial_list: List[int], reverse_list: List[int]):
    initial = LinkedList()
    for item in initial_list[::-1]:
        initial.push(item)
    s = Solution()
    curr = s.reverseList(initial.head)
    res = []
    while curr:
        res.append(curr.val)
        curr = curr.next
    assert res == reverse_list
