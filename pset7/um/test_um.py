import pytest
from um import count

def test_whole():
    assert count("yummy") == 0

def test_one():
    assert count("um") == 1

def test_two():
    assert count("Um, um...") == 2