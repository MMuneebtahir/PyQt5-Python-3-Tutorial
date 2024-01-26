from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication ,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self): # constructor
        super(MyWindow, self).__init__()
        xpos = 200
        ypos = 200
        width = 300
        height = 300
        self.setGeometry(xpos, ypos, width, height) # setting width , height , position (x,y) of window
        self.setWindowTitle("PyQt5 Tutorial") # Title of window/GUI
        self.initUI()

    def initUI(self): 
        """
         we initialize  all the stuff that we want
        in our window
        """
        label_xpos = 50
        label_ypos = 50
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(label_xpos, label_ypos)
        
        # create button with label 
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        # map this button to event / function
        self.b1.clicked.connect(self.clicked)
    
    def clicked(self):
        """
        change the label when you click the button
        """
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        """
        adjust the size of label when text is long
        """
        self.label.adjustSize()

# main code
def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()   # use  to show window
    sys.exit(app.exec_())  # create a cross button on GUI to exit

# calling a window function
window()