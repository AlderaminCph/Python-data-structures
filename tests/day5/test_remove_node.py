import pytest
from day5.remove_node_from_end import LinkedList, removeNthFromEnd


@pytest.mark.parametrize(
    ["listvalues", "n", "expected"],
    [([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]), ([1], 1, []), ([1, 2], 1, [1])],
)
def test_removeNthFromEnd(listvalues, n, expected):
    llist = LinkedList()
    for i in listvalues[::-1]:
        llist.push(i)
    resllist = removeNthFromEnd(llist.head, n)
    res = []
    while resllist:
        res.append(resllist.val)
        resllist = resllist.next
    assert expected == res
