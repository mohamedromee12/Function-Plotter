from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel
from PySide2.QtGui import QIcon, QFont
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

        self.blankBlock = QWidget()
        self.blankBlock.setStyleSheet("background-color: #eee;")
        self.layout.addWidget(self.blankBlock, 90)

        self.horizontalLayout = QHBoxLayout()
        self.layout.addLayout(self.horizontalLayout)

        self.equation = QLineEdit()
        self.equation.setFont(QFont("Arial", 13))
        self.horizontalLayout.addWidget(self.equation)

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


    def calcY(self, expression, numbers):
        expression = expression.replace(" ", "")
        pattern = r"([+-]?[0-9]*\.?[0-9]*)\*x\^([0-9]+)"
        terms = re.findall(pattern, expression)
        results = []
        for x in numbers:
            result = 0
            for term in terms:
                print(term)
                coefficient, exponent = float(term[0]), int(term[1])
                result += coefficient * (x ** exponent)
            results.append(result)
        return results


################################################################################################

    def plotEquation(self):
        minX = int(self.minValueEdit.text())
        maxX = int(self.maxValueEdit.text())

        print(minX)
        print(maxX)

        xList = np.linspace(minX, maxX, num=1000)
        yList = self.calcY(str(self.equation.text()), xList)

        plt.figure(num=0, dpi=120)
        plt.plot(xList, yList)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(str(self.equation.text()))
        plt.grid(True)
        plt.show()

##################################################################################################


myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
sys.exit(0)
