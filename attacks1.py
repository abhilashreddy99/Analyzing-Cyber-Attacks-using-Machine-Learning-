import sys
import os
from attacks import *
from PyQt5 import QtWidgets, QtGui, QtCore

class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton_2.clicked.connect(self.dsetf)
     self.ui.pushButton_7.clicked.connect(self.compare)
     self.ui.pushButton_6.clicked.connect(self.lr1)
     self.ui.pushButton_4.clicked.connect(self.gnb1)
     self.ui.pushButton_5.clicked.connect(self.htmap)
       

  def dsetf(self):
    os.system("python attack2.py")

  def compare(self):
    os.system("python compare1.py")

  def lr1(self):
    os.system("python lr1.py")
	
  def gnb1(self):
    os.system("python gnb1.py")

  def htmap(self):
    os.system("python attack1.py")


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
