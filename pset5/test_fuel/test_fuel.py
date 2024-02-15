from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")

def test_gauge():
    assert gauge(99) == 'F'
    assert gauge(1) == 'E'
    assert gauge(54) == "54%"