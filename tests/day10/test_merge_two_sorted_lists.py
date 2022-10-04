import pytest
from day10.merge_two_sorted_lists_21 import LinkedList, mergeTwoLists


@pytest.mark.parametrize(
    ["list1", "list2", "merged_list"],
    [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]), ([], [], []), ([], [0], [0])],
)
def test_mergeTwoList(list1, list2, merged_list):
    First = LinkedList()
    Second = LinkedList()
    for item in list1[::-1]:
        First.push(item)
    for item in list2[::-1]:
        Second.push(item)

    head_merged_list = mergeTwoLists(First, Second)
    result = []
    while head_merged_list:
        result.append(head_merged_list.val)
        head_merged_list = head_merged_list.next

    assert result == merged_list
