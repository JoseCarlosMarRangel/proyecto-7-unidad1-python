import sys

from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import pyqtSlot

app = QtWidgets.QApplication(sys.argv)

class calculo(QtWidgets.QWidget):
    def __init__(self):

       
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Medic")
        self.setGeometry(300, 300, 400, 400)
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

        self.si6 = QtWidgets.QPushButton("Si")
        self.no6 = QtWidgets.QPushButton("No")

        self.si6.setEnabled(False)
        self.no6.setEnabled(False)
        
        self.si7 = QtWidgets.QPushButton("Si")
        self.no7 = QtWidgets.QPushButton("No")

        self.si7.setEnabled(False)
        self.no7.setEnabled(False)
        
        self.si8 = QtWidgets.QPushButton("Si")
        self.no8 = QtWidgets.QPushButton("No")

        self.si8.setEnabled(False)
        self.no8.setEnabled(False)
        
        self.si9 = QtWidgets.QPushButton("Si")
        self.no9 = QtWidgets.QPushButton("No")

        self.si9.setEnabled(False)
        self.no9.setEnabled(False)
        
        self.si10 = QtWidgets.QPushButton("Si")
        self.no10 = QtWidgets.QPushButton("No")

        self.si10.setEnabled(False)
        self.no10.setEnabled(False)

        self.salir = QtWidgets.QPushButton("Salir")

        self.salir.setEnabled(False)
        
    

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

        grid.addWidget(self.si6,11,0)
        grid.addWidget(self.no6,11,1)

        grid.addWidget(self.si7,13,0)
        grid.addWidget(self.no7,13,1)

        grid.addWidget(self.si8,15,0)
        grid.addWidget(self.no8,15,1)

        grid.addWidget(self.si9,17,0)
        grid.addWidget(self.no9,17,1)

        grid.addWidget(self.si10,19,0)
        grid.addWidget(self.no10,19,1)

        grid.addWidget(self.respuesta,21,0)

        grid.addWidget(self.salir,21,2)

        grid.addWidget(QtWidgets.QLabel("Le duele la cabeza?"),0,0)
        grid.addWidget(QtWidgets.QLabel("Tiene dolor de espalda?"),2,0)
        grid.addWidget(QtWidgets.QLabel("Tiene ojos cansados regularmente?"),4,0)
        grid.addWidget(QtWidgets.QLabel("Tiene fiebre?"),6,0)
        grid.addWidget(QtWidgets.QLabel("Tiene dolor de garganta?"),8,0)
        grid.addWidget(QtWidgets.QLabel("Se siente cansado regularmente?"),10,0)
        grid.addWidget(QtWidgets.QLabel("Tiene dolor de pansa?"),12,0)
        grid.addWidget(QtWidgets.QLabel("Tiene dolor de pecho?"),14,0)
        grid.addWidget(QtWidgets.QLabel("Tiene tos?"),16,0)
        grid.addWidget(QtWidgets.QLabel("Tiene desmayos constantes?"),18,0)
                
        grid.addWidget(QtWidgets.QLabel("Enfermedad"),20,0)

        self.si.clicked.connect(self.activar2)
        self.si2.clicked.connect(self.activar2)
        self.si3.clicked.connect(self.terminar1)
        self.si4.clicked.connect(self.activar4)
        self.si5.clicked.connect(self.terminar2)
        self.si6.clicked.connect(self.activar7)
        self.si7.clicked.connect(self.activar7)
        self.si8.clicked.connect(self.activar4)
        self.si9.clicked.connect(self.terminar4)
        self.si10.clicked.connect(self.terminar5)
        
        self.no.clicked.connect(self.activar5)
        self.no2.clicked.connect(self.activar2)
        self.no3.clicked.connect(self.activar3)
        self.no4.clicked.connect(self.terminar3)
        self.no5.clicked.connect(self.activar8)
        self.no6.clicked.connect(self.activar4)
        self.no7.clicked.connect(self.activar7)
        self.no8.clicked.connect(self.activar9)
        self.no9.clicked.connect(self.activar9)
        self.no10.clicked.connect(self.terminar3)

        self.salir.clicked.connect(self.cerrar)

        self.show()

    def activar1(self):
        self.si2.setEnabled(True)
        self.no2.setEnabled(True)


    def activar2(self):
        self.si3.setEnabled(True)
        self.no3.setEnabled(True)
  
    def activar3(self):
        self.si4.setEnabled(True)
        self.no4.setEnabled(True)


    def activar4(self):
        self.si5.setEnabled(True)
        self.no5.setEnabled(True)


    def activar5(self):
        self.si6.setEnabled(True)
        self.no6.setEnabled(True)


    def activar6(self):
        self.si7.setEnabled(True)
        self.no7.setEnabled(True)
  
    def activar7(self):
        self.si8.setEnabled(True)
        self.no8.setEnabled(True)


    def activar8(self):
        self.si9.setEnabled(True)
        self.no9.setEnabled(True)
        self.respuesta.setText("Probablemente Alzhaimer")
        self.salir.setEnabled(True)

    def activar9(self):
        self.si10.setEnabled(True)
        self.no10.setEnabled(True)




    def terminar1(self):
        self.respuesta.setText("Epilepsia")
        self.salir.setEnabled(True)

    def terminar2(self):
        self.respuesta.setText("Sinusitis o hipotermia")
        self.salir.setEnabled(True)

    def terminar3(self):
        self.respuesta.setText("Covid o Asma")
        self.salir.setEnabled(True)

    def terminar4(self):
        self.respuesta.setText("Ictericia")
        self.salir.setEnabled(True)

    def terminar5(self):
        self.respuesta.setText("Golpe de calor o Diabetes")
        self.salir.setEnabled(True)

        


    def cerrar(self):
         self.salir.clicked.connect(self.close)

calc = calculo()

sys.exit(app.exec_())
