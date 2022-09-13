import pytest
from day2.rotate_array import rotate


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ],
)
def test_rotate(nums: list, k: int, expected_result: list):
    nums = nums
    rotate(nums, k)
    assert expected_result == nums
