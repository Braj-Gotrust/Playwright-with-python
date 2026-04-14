import pytest


@pytest.fixture
def setup():
    print("\nsetup browser") # before execute
    yield
    print("\nclose browser") # after execute

def test_m1(setup):
    print("This is method one") # middle execute
def test_m2(setup):
    print("This is method two")
def test_m3(setup):
    print("This is method three")

