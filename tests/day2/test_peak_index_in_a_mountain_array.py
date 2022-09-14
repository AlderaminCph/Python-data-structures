import pytest

from day2.peak_index_in_a_mountain_array import peakIndexInMountainArray


@pytest.mark.parametrize(
    ["arr", "expected_result"],
    [([0, 1, 0], 1), ([0, 2, 1, 0], 1), ([0, 10, 5, 2], 1)],
)
def test_peak(arr, expected_result):
    assert expected_result == peakIndexInMountainArray(arr)
