import pytest
from day3_two_pointers.distance_value_between_two_arrays import (
    findTheDistanceValue,
)


@pytest.mark.parametrize(
    ["arr1", "arr2", "d", "expected_result"],
    [
        ([4, 5, 8], [10, 9, 1, 8], 2, 2),
        ([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3, 2),
        ([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6, 1),
    ],
)
def test_distance(arr1, arr2, d, expected_result):
    assert expected_result == findTheDistanceValue(arr1, arr2, d)
