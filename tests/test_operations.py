def test_addition():
    from app.operations import addition
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(-1, -1) == -2
def test_subtraction():
    from app.operations import subtraction
    assert subtraction(5, 3) == 2
    assert subtraction(0, 0) == 0
    assert subtraction(-1, -1) == 0
    assert subtraction(-1, 1) == -2
def test_multiplication():
    from app.operations import multiplication
    assert multiplication(2, 3) == 6
    assert multiplication(-1, 1) == -1
    assert multiplication(0, 5) == 0
    assert multiplication(-2, -3) == 6
def test_division():    
    from app.operations import division
    assert division(6, 3) == 2
    assert division(-6, 3) == -2
    assert division(5, 2) == 2.5
    try:
        division(5, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed."