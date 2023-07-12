from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from PySide2.QtGui import QIcon, QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sys
import re
import numpy as np
import matplotlib.pyplot as plt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Function Plotter")
        self.setGeometry(600, 300, 600, 300)
        self.setMinimumWidth(600)
        self.setMinimumHeight(600)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')

        self.layout.addWidget(self.canvas, 90)

        self.horizontalLayout = QHBoxLayout()
        self.layout.addLayout(self.horizontalLayout)

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

        self.minWidget = QWidget()
        self.minLayout = QVBoxLayout(self.minWidget)
        self.minLabel = QLabel("Min X:")
        self.minValueEdit = QLineEdit()
        self.minLayout.addWidget(self.minLabel)
        self.minLayout.addWidget(self.minValueEdit)

        self.maxWidget = QWidget()
        self.maxLayout = QVBoxLayout(self.maxWidget)
        self.maxLabel = QLabel("Max X:")
        self.maxValueEdit = QLineEdit()
        self.maxLayout.addWidget(self.maxLabel)
        self.maxLayout.addWidget(self.maxValueEdit)

        self.rangeWidget = QWidget()
        self.rangeLayout = QHBoxLayout(self.rangeWidget)
        self.rangeLayout.addWidget(self.minWidget)
        self.rangeLayout.addWidget(self.maxWidget)

        self.button = QPushButton("Draw")
        self.button.setStyleSheet(
            "background-color: orange; color: white; font-size: 16px; font-weight: bold; cursor: pointer; border: 1px solid transparent; outline: none; border-radius: 5px; height:30%; width: 20%;")
        self.button.clicked.connect(self.plotEquation)

        self.rangeWithButtonWidget = QWidget()
        self.rangeWithButtonLayout = QVBoxLayout(self.rangeWithButtonWidget)
        self.rangeWithButtonLayout.addWidget(self.rangeWidget)
        self.rangeWithButtonLayout.addWidget(self.button)

        self.horizontalLayout.addWidget(self.rangeWithButtonWidget)

        self.setIcon()

    #################################################################################################

    def setIcon(self):
        appIcon = QIcon("Icons\plotter.png")
        self.setWindowIcon(appIcon)

    #################################################################################################

    def printValues(self):
        minValue = self.minValueEdit.text()
        maxValue = self.maxValueEdit.text()
        print("Min Value:", minValue)
        print("Max Value:", maxValue)

    ################################################################################################

    def calcY(self, expression, x):
        # Todo: check for the supported operations and show error message for the user for invalid expression

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
                print(
                    f"Supported Operators: {', '.join(allowed)}"
                )
                self.error.setText(
                    f"Supported Operators: {', '.join(allowed)}")
                return

        toBeReplaced = {
            '^': '**',
        }
        for old, new in toBeReplaced.items():
            expression = expression.replace(old, new)

        self.error.setText("")
        return (eval(expression))

    ################################################################################################

    def isNumber(self, number):
        pattern = r'^[-+]?\d*\.?\d+$'
        return re.match(pattern, number) is not None

    ################################################################################################
    def plotEquation(self):
        if (self.isNumber(self.minValueEdit.text()) == False or self.isNumber(self.maxValueEdit.text()) == False):
            self.error.setText("Max x and Min x should be numbers only")
            return

        minX = int(self.minValueEdit.text())
        maxX = int(self.maxValueEdit.text())

        # Todo: show error message for the user
        if (maxX < minX):
            print("Max x should be greater than Min x")
            self.error.setText("Max x should be greater than Min x")
            return

        xList = np.linspace(minX, maxX, num=1000)
        yList = self.calcY(str(self.equation.text()), xList)

        if self.error.text() == "":
            self.ax.clear()
            self.ax.plot(xList, yList)
            self.ax.set_title(str(self.equation.text()))
            self.ax.grid(True)
            self.canvas.draw()
        else:
            print("There is an error")

##################################################################################################


myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
sys.exit(0)
