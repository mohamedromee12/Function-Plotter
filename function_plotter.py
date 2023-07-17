from PySide2.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from PySide2.QtGui import QIcon, QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import numpy as np
import matplotlib.pyplot as plt

from helper_function import *


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # Setting the properties of the main window.
        self.setWindowTitle("Function Plotter")
        self.setGeometry(600, 300, 600, 300)
        self.setMinimumWidth(600)
        self.setMinimumHeight(600)

        # Creating a central widget for the main window and setting it as the
        # central widget using `setCentralWidget()`. The central widget is the main area of the window
        # where other widgets and layouts can be added.
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        # Creating a figure, a canvas, and an axis for plotting the graph.
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.layout.addWidget(self.canvas, 90)

        # Creating a horizontal layout.
        self.horizontalLayout = QHBoxLayout()
        self.layout.addLayout(self.horizontalLayout)

        # Creating a widget and a vertical layout to hold the equation-related elements.
        self.equationWidget = QWidget()
        self.equationLayout = QVBoxLayout(self.equationWidget)
        self.equation = QLineEdit()
        self.equation.setFont(QFont("Arial", 13))
        self.error = QLabel("", self)
        self.error.setStyleSheet(
            "color: red; font-weight: bold; font-size: 14;")
        self.equationLabel = QLabel("Equation:", self)
        self.equationLayout.addWidget(self.equationLabel)
        self.equationLayout.addWidget(self.equation)
        self.equationLayout.addWidget(self.error)
        self.horizontalLayout.addWidget(self.equationWidget)

        # Creating a widget and a vertical layout to hold the elements related to the minimum x value.
        self.minWidget = QWidget()
        self.minLayout = QVBoxLayout(self.minWidget)
        self.minLabel = QLabel("Min X:")
        self.minValueEdit = QLineEdit()
        self.minLayout.addWidget(self.minLabel)
        self.minLayout.addWidget(self.minValueEdit)

        # Creating a widget and a vertical layout to hold the elements related to the maximum x value.
        self.maxWidget = QWidget()
        self.maxLayout = QVBoxLayout(self.maxWidget)
        self.maxLabel = QLabel("Max X:")
        self.maxValueEdit = QLineEdit()
        self.maxLayout.addWidget(self.maxLabel)
        self.maxLayout.addWidget(self.maxValueEdit)

        # Creating a widget and a horizontal layout to hold the elements related to the minimum and maximum x values.
        self.rangeWidget = QWidget()
        self.rangeLayout = QHBoxLayout(self.rangeWidget)
        self.rangeLayout.addWidget(self.minWidget)
        self.rangeLayout.addWidget(self.maxWidget)

        # Creating a QPushButton widget , the `clicked` signal of the button is connected to the `plotEquation` method, which
        # will be called when the button is clicked.
        self.button = QPushButton("Draw")
        self.button.setStyleSheet(
            "background-color: orange; color: white; font-size: 16px; font-weight: bold; cursor: pointer; border: 1px solid transparent; outline: none; border-radius: 5px; height:30%; width: 20%;")
        self.button.clicked.connect(self.plotEquation)

        # Creating a widget and a vertical layout to hold the elements related to the minimum and maximum
        # x values and the button. The `rangeWithButtonWidget` is added to the `horizontalLayout`. This arrangement allows the minimum and maximum x value
        # inputs and the button to be displayed horizontally in the main window.
        self.rangeWithButtonWidget = QWidget()
        self.rangeWithButtonLayout = QVBoxLayout(self.rangeWithButtonWidget)
        self.rangeWithButtonLayout.addWidget(self.rangeWidget)
        self.rangeWithButtonLayout.addWidget(self.button)
        self.horizontalLayout.addWidget(self.rangeWithButtonWidget)

        # Calling the function which set the icon of the gui program
        self.setIcon()

    #################################################################################################

    def setIcon(self):
        """
        The function sets the icon for a window in a Python application.
        """
        appIcon = QIcon("Icons\plotter.png")
        self.setWindowIcon(appIcon)

    ################################################################################################

    def plotEquation(self):
        """
        The function plots an equation on a graph based on user input, with error handling for invalid
        inputs.
        :return: The function does not explicitly return anything.
        """

        # Check if there is any input field.
        if (len(self.equation.text()) == 0 or len(self.minValueEdit.text()) == 0 or len(self.maxValueEdit.text()) == 0):
            self.error.setText("All input fields should be filled")
            self.ax.clear()
            self.canvas.draw()
            return

        # Ensure the max and min are numbers.
        if (isNumber(self.minValueEdit.text()) == False or isNumber(self.maxValueEdit.text()) == False):
            self.error.setText("Max x and Min x should be numbers only")
            self.ax.clear()
            self.canvas.draw()
            return


        # Convert max and min to numbers
        minX = float(self.minValueEdit.text())
        maxX = float(self.maxValueEdit.text())


        # Ensure that max is greater than min
        if (maxX < minX):
            self.error.setText("Max x should be greater than Min x")
            self.ax.clear()
            self.canvas.draw()
            return


        # Get x values inbetween the min and max, y values from the expression.
        xList = np.linspace(minX, maxX, num=1000)
        yList = calcY(str(self.equation.text()), xList, self.error)


        # Check if there is any error, if there is not error plot the function, else clear the figure.
        if self.error.text() == "":
            self.ax.clear()
            self.ax.plot(xList, yList)
            self.ax.set_title(str(self.equation.text()))
            self.ax.grid(True)
            self.canvas.draw()
        else:
            self.ax.clear()
            self.canvas.draw()
