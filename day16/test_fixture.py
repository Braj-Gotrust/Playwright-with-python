# Fixture :- Fixture is a re-usable function in python. It is a normal function not a test function
import pytest


@pytest.fixture
def braj():  # Normal function
    print("This is braj")

def test_m1(braj):  # pytest function
    print("This is method one")
def test_m2(braj):
    print("This is method two")
def test_m3(braj):
    print("This is method three")
