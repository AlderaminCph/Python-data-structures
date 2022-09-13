import pytest

from day2.squares_of_sorted_array import sortedSquares


@pytest.mark.parametrize(
    ["nums", "expected_result"],
    [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ],
)
def test_sortedSquares(nums: list, expected_result: list):
    assert expected_result == sortedSquares(nums)
