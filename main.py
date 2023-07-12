import sys
from PySide2.QtWidgets import QApplication

from function_plotter import Window

myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
sys.exit(0)
