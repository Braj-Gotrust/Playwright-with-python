# NOTE- Modules name, Classes name, and Functions should be start with 'test' keyword in pytest framework. Example- test_braj()
# This module, class, function no need to calling.It is not a normal function.

# It is calling with 'terminal' like a function address "pytest day16/test_demo.py -s -v"
# 'pytest day16/test_demo.py -s'  -  Normal details
# 'pytest day16/test_demo.py -s -v'  -   It is provided full information
# 'pytest day16/test_demo.py::test_fun3 -s -v'  -  Only specific function run to provided name

# -s -> you can see all print() outputs lines in the console while the test runs
# -v -> Run pytest in the "verbose" mode. Shows detailed test execution information

import pytest
def testfun1():
    print("hello braj")
def test_fun2():
    print("hello suraj")
def test_fun3():
    print("hello shahil")


class TestClass:
    def test_fun4(self):
        print("This is function number 4 ")
    def test_fun5(self):
        print("This is function number 5 ")


