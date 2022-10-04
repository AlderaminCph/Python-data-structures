import pytest
from day3_two_pointers.move_zeroes import moveZeroes


@pytest.mark.parametrize(
    ["nums", "expected_result"],
    [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0])],
)
def test_move_zeroes(nums, expected_result):
    assert expected_result == moveZeroes(nums)
