import pytest
from day2_two_pointers.rotate_array import rotate


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([-1], 2, [-1]),
        ([1, 2], 3, [2, 1]),
    ],
)
def test_rotate(nums: list, k: int, expected_result: list):
    rotate(nums, k)
    assert expected_result == nums
