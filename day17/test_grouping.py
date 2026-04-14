'''
grouping test:-
test_loginbyemail -> sanity, regression
test_loginbyfacebook -> sanity
test_loginbygoogle -> regression
test_signupbyemail -> sanity, regression
test_signupbyfacebook -> regression
test_signupbygoogle -> sanity
test_paymentindoller -> sanity, regression
test_paymentinrupees -> regression

'''

# sanity and regression in user define name, not a keyword

'''
1) Run sanity tests command -> pytest day17/test_grouping.py -s -v -m "sanity"
2) Run regression tests command -> pytest day17/test_grouping.py -s -v -m "regression"
3) Run tests which are belong to both sanity and regression command -> pytest day17/test_grouping.py -s -v -m "sanity and regression"
4) Run only sanity tests which are not belong to regression command -> pytest day17/test_grouping.py -s -v -m "sanity" -m "not regression"
5) Run only regression tests which are not belong to sanity command -> pytest day17/test_grouping.py -s -v -m "regression" -m "not sanity"

'''

import pytest


@pytest.mark.sanity
@pytest.mark.regression
def test_loginbyemail():
    print("this is login by email test")
    assert 1 == 1


@pytest.mark.sanity
def test_loginbyfacebook():
    print("this is login by facebook test")
    assert 1 == 1


@pytest.mark.regression
def test_loginbygoogle():
    print("this is login by google test")
    assert 1 == 1


@pytest.mark.sanity
@pytest.mark.regression
def test_signupbyemail():
    print("this is signup by email test")
    assert 1 == 1


@pytest.mark.regression
def test_signupbyfacebook():
    print("this is signup by facebook test")
    assert 1 == 1


@pytest.mark.sanity
def test_signupbygoogle():
    print("this is signup by google test")
    assert 1 == 1


@pytest.mark.sanity
@pytest.mark.regression
def test_paymentindoller():
    print("this is payment in doller test")
    assert 1 == 1


@pytest.mark.regression
def test_paymentinrupees():
    print("this is payment in rupees test")
    assert 1 == 1
