import pytest
import math_func


@pytest.mark.parametrize(
    "args, expected",
    [((1, 2, 3), 6), ((1,), 1), ((1, 1), 2), ((0,), 0)],
)
def test_add(args, expected):
    assert math_func.add(*args) == expected
    with pytest.raises(TypeError):
        math_func.add()


@pytest.mark.parametrize(
    "args, expected",
    [((1, 2, 3), 6), ((1,), 1), ((1, 1), 1), ((0,), 0)],
)
def test_multiply(args, expected):
    assert math_func.multiply(*args) == expected
    with pytest.raises(TypeError):
        math_func.multiply()
