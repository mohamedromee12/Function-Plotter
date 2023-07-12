import re


def isNumber(number):
    """
    The function `isNumber` checks if a given input is a valid number.

    :param number: The parameter "number" is a string that represents a number
    :return: a boolean value indicating whether the input "number" is a valid number or not.
    """
    pattern = r'^[-+]?\d*\.?\d+$'
    return re.match(pattern, number) is not None


##########################################################################################################


def calcY(expression, x, error=None):
    """
    The function `calcY` calculates the value of a mathematical expression involving the variable `x`,
    with support for basic arithmetic operations and exponentiation.

    :param expression: The expression parameter is a string that represents a mathematical expression.
    It can contain variables, operators, and numbers
    :param x: The value of x that you want to evaluate the expression at
    :param error: The `error` parameter is a widget or object that is used to display any error messages
    or notifications to the user. It could be a label, text box, or any other UI element that can
    display text
    :return: The function `calcY` returns the result of evaluating the expression after performing some
    operations and replacements.
    """
    expression = expression.lower()
    allowed = [
        'x',
        '/',
        '+',
        '*',
        '^',
        '-',
    ]

    for word in re.findall('[a-zA-Z_]+', expression):
        if word not in allowed:
            if error is not None:
                error.setText(
                    f"Supported Operators: {', '.join(allowed)}")
            return False

    toBeReplaced = {
        '^': '**',
    }
    for old, new in toBeReplaced.items():
        expression = expression.replace(old, new)

    if error is not None:
        error.setText("")
    return (eval(expression))
