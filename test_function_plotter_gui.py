import pytest
from PySide2.QtCore import Qt
from function_plotter import Window


@pytest.fixture
def app(qapp, qtbot):
    window = Window()
    window.show()
    qtbot.addWidget(window)
    return window


def test_plot_equation(app, qtbot):
    # Find the relevant widgets
    equation = app.equation
    minValueEdit = app.minValueEdit
    maxValueEdit = app.maxValueEdit
    button = app.button

    ######################################## Test-1  ########################################

    # Simulate user input
    equation.setText("x**2")
    minValueEdit.setText("0")
    maxValueEdit.setText("10")

    # Click the draw button
    qtbot.mouseClick(button, Qt.LeftButton)

    # Retrieve the plot widget and assert the plot is drawn correctly
    plot_widget = app.canvas
    assert len(plot_widget.figure.axes) == 1  # Verify that one axis is present
    assert len(plot_widget.figure.axes[0].lines) == 1  # Verify that one line is drawn


    ######################################## Test-2  ########################################


    # Simulate user input
    equation.setText("x**2")  # Invalid equation with "^" instead of "**"
    minValueEdit.setText("b")
    maxValueEdit.setText("10")

    # Click the draw button
    qtbot.mouseClick(button, Qt.LeftButton)

    # Retrieve the error label and verify that an error message is displayed
    error_label = app.error
    assert error_label.text() == "Max x and Min x should be numbers only"

    ######################################## Test-3  ########################################


    # Simulate user input
    equation.setText("x**2")  # Invalid equation with "^" instead of "**"
    minValueEdit.setText("20")
    maxValueEdit.setText("10")

    # Click the draw button
    qtbot.mouseClick(button, Qt.LeftButton)

    # Retrieve the error label and verify that an error message is displayed
    error_label = app.error
    assert error_label.text() == "Max x should be greater than Min x"


    ######################################## Test-4  ########################################


    # Simulate user input
    equation.setText("x**2 + c")  # Invalid equation with "^" instead of "**"
    minValueEdit.setText("0")
    maxValueEdit.setText("10")

    # Click the draw button
    qtbot.mouseClick(button, Qt.LeftButton)

    # Retrieve the error label and verify that an error message is displayed
    error_label = app.error
    assert error_label.text() == "Supported Operators: x, /, +, *, ^, -"



if __name__ == "__main__":
    pytest.main()