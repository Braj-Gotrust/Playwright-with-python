'''
To control the order of the method like a priority base , to install a order plugin
   pre-requisite: install pytest-order plugin

   pip install pytest-order

'''

import pytest

@pytest.mark.order(1)   # this method is print into the order wise
def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1

@pytest.mark.order(3)
def test_loginbyfacebook():
    print("this is login by facebook test")
    assert 1 == 1

@pytest.mark.order(2)
def test_loginbygoogle():
    print("this is login by google test")
    assert 1 == 1

@pytest.mark.order(4)
def test_signupbyemail():
    print("this is signup by email test")
    assert 1 == 1

@pytest.mark.order(6)
def test_signupbyfacebook():
    print("this is signup by facebook test")
    assert 1 == 1

@pytest.mark.order(5)
def test_signupbygoogle():
    print("this is signup by google test")
    assert 1 == 1
