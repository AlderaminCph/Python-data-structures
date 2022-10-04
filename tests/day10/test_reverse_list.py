import pytest
from day10.reversed_linked_list import Solution, LinkedList
from typing import List


@pytest.mark.parametrize(
    ["initial_list", "reverse_list"],
    [([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), ([1, 2], [2, 1]), ([], [])],
)
def test_reverse_list(initial_list: List[int], reverse_list: List[int]):
    initial, reverse = LinkedList(), LinkedList()
    for item, rev in zip(initial_list[::-1], reverse_list[::-1]):
        initial.push(item)
        reverse.push(rev)
    s = Solution()
    assert reverse.head == s.reverseList(initial.head)
