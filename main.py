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
        
        self.si2 = QtWidgets.QPushButton("Si")
        self.no2 = QtWidgets.QPushButton("No")

        self.si2.setEnabled(False)
        self.no2.setEnabled(False)
        
        self.si3 = QtWidgets.QPushButton("Si")
        self.no3 = QtWidgets.QPushButton("No")

        self.si3.setEnabled(False)
        self.no3.setEnabled(False)
        
        self.si4 = QtWidgets.QPushButton("Si")
        self.no4 = QtWidgets.QPushButton("No")

        self.si4.setEnabled(False)
        self.no4.setEnabled(False)
        
        self.si5 = QtWidgets.QPushButton("Si")
        self.no5 = QtWidgets.QPushButton("No")

        self.si5.setEnabled(False)
        self.no5.setEnabled(False)
        
    

        self.si.setToolTip("Puede tomar una pastilla generica")

        


        self.respuesta = QtWidgets.QLabel("")

        grid = QtWidgets.QGridLayout(self)
       


         
        grid.addWidget(self.si,1,0)
        grid.addWidget(self.no,1,1)

        grid.addWidget(self.si2,3,0)
        grid.addWidget(self.no2,3,1)

        grid.addWidget(self.si3,5,0)
        grid.addWidget(self.no3,5,1)

        grid.addWidget(self.si4,7,0)
        grid.addWidget(self.no4,7,1)

        grid.addWidget(self.si5,9,0)
        grid.addWidget(self.no5,9,1)

        grid.addWidget(QtWidgets.QLabel("Le duele la cabeza?"),0,0)
        grid.addWidget(QtWidgets.QLabel("Tiene dolor de garganta?"),2,0)
        grid.addWidget(QtWidgets.QLabel("Tiene dolor de pansa?"),4,0)
        grid.addWidget(QtWidgets.QLabel("Tiene dolor de Cuerpo?"),6,0)
        grid.addWidget(QtWidgets.QLabel("Tiene mareos?"),8,0)
        
        
        grid.addWidget(QtWidgets.QLabel("Enfermedad"),10,0)

        self.si.clicked.connect(self.activar1)
        self.si2.clicked.connect(self.activar3)
        self.si3.clicked.connect(self.activar4)
        
        

       

        self.show()

    def activar1(self):
        self.si2.setEnabled(True)
        self.no2.setEnabled(True)


    def activar2(self):
        self.si3.setEnabled(True)
        self.no3.setEnables(True)
  
    def activar3(self):
        self.si4.setEnabled(True)
        self.no4.setEnabled(True)


    def activar4(self):
        self.si5.setEnabled(True)
        self.no5.setEmabled(True)
        

calc = calculo()

sys.exit(app.exec_())
