# scope="function" -> fixture will be called before every test function executes
# scope="module" -> fixture will be called only once before test functions executes
# scope="class" -> fixture will be called only once before the class
# scope="session" -> fixture will be called only once for session

# module->class->function

import pytest


@pytest.fixture
def braj(scope="function"):  # Normal function
    print("This is braj")

def test_m1(braj):  # pytest function
    print("This is method one")
def test_m2(braj):
    print("This is method two")
def test_m3(braj):
    print("This is method three")

