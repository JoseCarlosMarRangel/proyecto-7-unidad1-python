import sys

from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import pyqtSlot

app = QtWidgets.QApplication(sys.argv)

class calculo(QtWidgets.QWidget):
    def __init__(self):

       
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Medic")
        self.setGeometry(200, 200, 400, 400)
        self.c = QtWidgets.QLineEdit("Enfermedad")
       
        
        self.si = QtWidgets.QPushButton("Si")
        self.no = QtWidgets.QPushButton("No")
        self.si.setStyleSheet("background-color:white")
        self.no.setStyleSheet("background-color:white")

        self.si.setToolTip("Puede tomar una pastilla generica")

        


        self.respuesta = QtWidgets.QLabel("")

        grid = QtWidgets.QGridLayout(self)
       


         
        grid.addWidget(self.si,1,0)
        grid.addWidget(self.no,1,1)


        grid.addWidget(QtWidgets.QLabel("Le duele la cabeza?"),0,0)
        grid.addWidget(QtWidgets.QLabel("Enfermedad"),3,0)

        

       
 

        self.show()
        

calc = calculo()

sys.exit(app.exec_())
