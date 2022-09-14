import pytest

from day3.valid_perfect_square import isPerfectSquare


@pytest.mark.parametrize(
    ["num", "expected_result"], [(16, True), (12, False), (1, True)]
)
def test_isPerfectSquare(num: int, expected_result: bool):
    assert expected_result == isPerfectSquare(num)
