from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication ,QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    xpos = 200
    ypos = 200
    width = 300
    height = 300
    label_xpos = 50
    label_ypos = 50
    win.setGeometry(xpos, ypos, width, height) # setting width , height , position (x,y) of window
    win.setWindowTitle("PyQt5 Tutorial") # Title of window/GUI
    label = QtWidgets.QLabel(win)
    label.setText("my first label!")
    label.move(label_xpos, label_ypos)
    win.show()   # use  to show window
    sys.exit(app.exec_())  # create a cross button on GUI to exit

window()