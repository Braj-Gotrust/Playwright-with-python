import pytest


def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1

@pytest.mark.skip   # To skip this function
def test_loginbyfacebook():
    print("this is login by facebook test")
    assert 1 == 1


def test_loginbygoogle():
    print("this is login by google test")
    assert 1 == 1


def test_signupbyemail():
    print("this is signup by email test")
    assert 1 == 1

@pytest.mark.skip
def test_signupbyfacebook():
    print("this is signup by facebook test")
    assert 1 == 1


def test_signupbygoogle():
    print("this is signup by google test")
    assert 1 == 1
