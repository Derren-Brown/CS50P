import pytest
from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.0.0.0") == False
    assert validate("1.2.3.1000") == False
    assert validate("vat") == False
    assert validate("2.256.0.0") == False
