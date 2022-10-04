import pytest

from day5_two_pointers.middle_of_the_linked_list import LinkedList, middleNode


@pytest.mark.parametrize(
    ["listvalues", "expected"],
    [([1, 2, 3, 4, 5], [3, 4, 5]), ([1, 2, 3, 4, 5, 6], [4, 5, 6])],
)
def test_middleNode(listvalues, expected):
    llist = LinkedList()
    for i in listvalues[::-1]:
        llist.push(i)
    node = middleNode(llist.head)
    res = []
    while node:
        res.append(node.val)
        node = node.next
    assert expected == res
