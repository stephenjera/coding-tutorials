import pytest
import math_func

def test_add():
    assert math_func.add(1,2,3) == 6
    assert math_func.add(0) == 0
    assert math_func.add(1,1) == 2
    with pytest.raises(TypeError):
        math_func.add()

def test_multiply():
    assert math_func.multiply(1,2,3) == 6
    assert math_func.multiply(0) == 0
    assert math_func.multiply(1,1) == 1
    with pytest.raises(TypeError):
        math_func.multiply()