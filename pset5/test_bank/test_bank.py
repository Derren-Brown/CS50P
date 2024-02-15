from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello world ") == 0

def test_h():
    assert value("hees") == 20

def test_other():
    assert value("aksk") == 100