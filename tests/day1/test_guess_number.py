import pytest

from day1.guess_number import guessNumber


@pytest.mark.parametrize(
    ["n", "p", "expected_result"], [(10, 6, 6), (2, 1, 1), (1, 1, 1)]
)
def test_guessNumber(n, p, expected_result):
    assert expected_result == guessNumber(n, p)
