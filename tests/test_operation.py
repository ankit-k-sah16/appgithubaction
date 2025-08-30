from src.math_operation import add,subtract,multiply,divide

def test_add():
    assert add(2,3)==5
    assert add(34+24)==68

def test_subtract():
    assert subtract(200-50)==150
    assert subtract(43-43)==0

