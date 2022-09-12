import pytest

from day1.binary_search import search


@pytest.mark.parametrize(
    ["nums", "target", "expected"],
    [
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ],
)
def test_search(nums: list, target: int, expected: int):
    assert search(nums, target) == expected
