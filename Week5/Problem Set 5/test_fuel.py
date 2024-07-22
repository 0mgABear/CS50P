import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("100/100") == 100

    with pytest.raises(ValueError):
        convert("2/1")

    with pytest.raises(ValueError):
        convert("a/b")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(25) == "25%"

if __name__ == "__main__":
    pytest.main()
