import pytest
from day4.reverse_string import reverseString


@pytest.mark.parametrize(
    ["s", "expected"],
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ],
)
def test_reverseString(s: list, expected: list):
    assert expected == reverseString(s)
