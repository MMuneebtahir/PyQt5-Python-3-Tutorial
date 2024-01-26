# **PyQt5-Python-3-Tutorial**
PyQt5 is a python 3 module that allows for rapid development of GUI applications using its built in program Qt-Designer. PyQt5 runs on all operating systems which means all of the code you write will scale
## **DEVICE**
Linux Computer

## **Programming Language**
Python

## **OS**
Ubuntu Linux 18.04

## **PREREQUISITES**
	sudo add-apt-repository universe
	sudo apt update
	sudo apt updgrade
	sudo apt install libgl1-mesa-dev
	sudo apt install libglu1-mesa-dev
	sudo apt install libfontconfig1-dev libfreetype6-dev libx11-dev libx11-xcb-dev libxext-dev libxfixes-dev libxi-dev libxrender-dev libxcb1-dev libxcb-glx0-dev libxcb-keysyms1-dev libxcb-image0-dev libxcb-shm0-dev libxcb-icccm4-dev libxcb-sync-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-randr0-dev libxcb-render-util0-dev libxcb-util-dev libxcb-xinerama0-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev
	sudo apt-get install  freeglut3-dev

## Setup GUI Application
	pip3 install pyqt5
	pip3 install  pyqt5-tools

## **LIBRARIES VERSION**
	python3 --version

## **DEVELOPMENT**
### **1. Basic GUI Application**
* Create a window with label of specific size at specific location of screen .

### **2. Buttons and Events(Signals)**
* Create buttons that trigger certain functions that change the label text and adjust the size of label when text is long

### **3. How to Use Qt Designer**
* The first steps to using QtDesigner is to download and install pyqt5-tools (this can be done through pip)
* ui design contain button , label and menu bar. buttons  triggers certain functions that change the label text and adjust the size of label when text is long
* when you are done with design in QT-designer save that file as **file_name.ui**
* Convert `.ui` file to python using following command 
		pyuic5 -x QT_Design.ui -o QT_Design_PythonFile.py
* check the design run the following command
		 QT_Design_PythonFile.py
* When you run `QT_Design_PythonFile.py` file only GUI will display without functionality
* Open python `QT_Design_PythonFile.py` and assign functionality to button and label
* Now when you run `QT_Design_PythonFile.py` file only GUI run with user functionality

### **4. MenuBar (Shortcuts, Status Bar and Triggers)**


### **Project Structure**
<pre>
PyQt5_Tutorial
├── Basic_GUI_Application.py
├── Buttons_and_Events.py
├── QT_design
│   └── test.ui
├── readme.md
└── test_QT_design.py
</pre>

## **Developer**
* Muneeb

## **uninstall QT**
	sudo apt-get remove qtcreator
	sudo apt-get remove --auto-remove qtcreator

## **References**
* [Qt for X11 Requirements](https://doc.qt.io/qt-6/linux-requirements.html)
* [Qt Downloads](https://download.qt.io/archive/qt/)
* [Qt Configure Options](https://doc-snapshots.qt.io/qt6-dev/configure-options.html)
* [PyQt5 Python 3 Tutorial](https://www.youtube.com/playlist?list=PLzMcBGfZo4-lB8MZfHPLTEHO9zJDDLpYj)
