import pytest
from day3.twosum2 import twoSum


@pytest.mark.parametrize(
    ["numbers", "target", "expected_result"],
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
)
def test_twoSum(numbers, target, expected_result):
    assert expected_result == twoSum(numbers, target)
