#To execute the parallel method and module so that to install parallel plugin
# pre-requisite : install a pytest plugin "pytest-xdist" to run test parallel
#   pip install pytest-xdist

# parallel execution command -> pytest day17/test_parallel.py -s -v -n 2
# given number 1,2,3,4,5 that are workers 

import pytest


def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1


def test_loginbyfacebook():
    print("this is login by facebook test")
    assert 1 == 1


def test_loginbygoogle():
    print("this is login by google test")
    assert 1 == 1


def test_signupbyemail():
    print("this is signup by email test")
    assert 1 == 1


def test_signupbyfacebook():
    print("this is signup by facebook test")
    assert 1 == 1


def test_signupbygoogle():
    print("this is signup by google test")
    assert 1 == 1
