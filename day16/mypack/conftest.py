# file name should be fix name "conftest.py"
import pytest

@pytest.fixture
def setup():
    print("\nsetup environment")