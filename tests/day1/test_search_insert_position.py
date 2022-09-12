import pytest

from day1.search_insert_position import searchInsert


@pytest.mark.parametrize(
    ["nums", "target", "expected_result"],
    [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4)],
)
def test_searchInsert(nums: list, target: int, expected_result: int):
    assert expected_result == searchInsert(nums, target)
