from bank import value #type: ignore

def test_value():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("What's happening") == 100
    assert value("hi there") == 20
    assert value("") == 100
    assert value("  HELLO  ") == 0
    assert value("hey") == 20


