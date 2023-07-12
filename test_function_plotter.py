from helper_function import *
import numpy as np


def test_isNumber():
    """
    The function `test_isNumber` tests whether a given string is a number or not.
    """
    assert isNumber("5") == True
    assert isNumber("c") == False


###############################################################################################################

def test_calcY():
    """
    The function `test_calcY()` tests the `calcY()` function by checking if the calculated y-values
    match the expected values for two different expressions.
    """
    expression = "x^2 + 5"
    xList = np.linspace(1, 5, num=5)
    expectedList = [6, 9, 14, 21, 30]
    assert np.array_equal(calcY(expression, xList), expectedList)

    expression = "x^2 + c + 5"
    xList = np.linspace(1, 5, num=5)
    assert calcY(expression, xList) == False
