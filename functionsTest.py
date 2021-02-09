from functions import *


def run_tests():
    assert add(2, 3) == 5
    assert subtract(4, 3) == 1
    assert multiply(2, 3) == 6
    assert divide(4, 2) == 2
    assert square(2) == 4

run_tests()
