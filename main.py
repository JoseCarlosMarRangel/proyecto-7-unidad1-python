
import sys

from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtCore import pyqtSlot

app = QtWidgets.QApplication(sys.argv)

class calculo(QtWidgets.QWidget):
    
    contador = 0
    
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

        self.grid = QtWidgets.QGridLayout(self)
       


         
        self.grid.addWidget(self.si,1,0)
        self.grid.addWidget(self.no,1,1)

        self.grid.addWidget(self.si2,3,0)
        self.grid.addWidget(self.no2,3,1)

        self.grid.addWidget(self.si3,5,0)
        self.grid.addWidget(self.no3,5,1)

        self.grid.addWidget(self.si4,7,0)
        self.grid.addWidget(self.no4,7,1)

        self.grid.addWidget(self.si5,9,0)
        self.grid.addWidget(self.no5,9,1)

        self.grid.addWidget(self.si6,11,0)
        self.grid.addWidget(self.no6,11,1)

        self.grid.addWidget(self.si7,13,0)
        self.grid.addWidget(self.no7,13,1)

        self.grid.addWidget(self.si8,15,0)
        self.grid.addWidget(self.no8,15,1)

        self.grid.addWidget(self.si9,17,0)
        self.grid.addWidget(self.no9,17,1)

        self.grid.addWidget(self.si10,19,0)
        self.grid.addWidget(self.no10,19,1)

        self.grid.addWidget(self.respuesta,21,0)

        self.grid.addWidget(self.salir,21,2)

        self.grid.addWidget(QtWidgets.QLabel("Le duele la cabeza?"),0,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene dolor de espalda?"),2,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene ojos cansados regularmente?"),4,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene fiebre?"),6,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene dolor de garganta?"),8,0)
        self.grid.addWidget(QtWidgets.QLabel("Se siente cansado regularmente?"),10,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene dolor de pansa?"),12,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene dolor de pecho?"),14,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene tos?"),16,0)
        self.grid.addWidget(QtWidgets.QLabel("Tiene desmayos constantes?"),18,0)
                
        self.grid.addWidget(QtWidgets.QLabel("Enfermedad"),20,0)
        
        #Preguntas
        self.grid.addWidget(QtWidgets.QLabel("¿Le duele la cabeza?"),0,3)

        self.si.clicked.connect(self.activar2)
        self.si.clicked.connect(self.sipresionado)
        
        self.si2.clicked.connect(self.activar2)
        
        self.si3.clicked.connect(self.terminar1)
        self.si3.clicked.connect(self.si3presionado)
        
        self.si4.clicked.connect(self.activar4)
        self.si4.clicked.connect(self.si4presionado)
        
        self.si5.clicked.connect(self.terminar2)
        self.si5.clicked.connect(self.si5presionado)
        
        self.si6.clicked.connect(self.activar7)
        self.si6.clicked.connect(self.si6presionado)
        
        self.si7.clicked.connect(self.activar7)
        
    
        self.si8.clicked.connect(self.activar4)
        self.si8.clicked.connect(self.si8presionado)
        
        self.si9.clicked.connect(self.terminar4)
        self.si9.clicked.connect(self.si9presionado)
        
        self.si10.clicked.connect(self.terminar5)
        self.si10.clicked.connect(self.si10presionado)

        self.no.clicked.connect(self.activar5)
        self.no.clicked.connect(self.nopresionado)
        
        self.no2.clicked.connect(self.activar2)
        
        self.no3.clicked.connect(self.activar3)
        self.no3.clicked.connect(self.no3presionado)
        
        self.no4.clicked.connect(self.terminar3)
        self.no4.clicked.connect(self.no4presionado)
        
        self.no5.clicked.connect(self.activar8)
        self.no5.clicked.connect(self.no5presionado)
        
        self.no6.clicked.connect(self.activar4)
        self.no6.clicked.connect(self.no6presionado)
        
        self.no7.clicked.connect(self.activar7)
        
        self.no8.clicked.connect(self.activar9)
        
        self.no9.clicked.connect(self.activar9)
        self.no9.clicked.connect(self.no9presionado)
        
        self.no10.clicked.connect(self.terminar3)
        self.no10.clicked.connect(self.no10presionado)
        

        self.salir.clicked.connect(self.cerrar)

        self.show()
        
        
            #widget = QtWidgets.QLabel("Probablemente Alzhaimer")
            #self.grid.addWidget(widget,1,4)
      

    def activar1(self):
        self.si2.setEnabled(True)
        self.no2.setEnabled(True)
        

    def activar2(self):#tiene ojos cansados regularmente
        self.si3.setEnabled(True)
        self.no3.setEnabled(True)
  
    def activar3(self): #Tienes fiebre?
        self.si4.setEnabled(True)
        self.no4.setEnabled(True)


    def activar4(self): #Tienes dolor de garganta?
        self.si5.setEnabled(True)
        self.no5.setEnabled(True)
        


    def activar5(self): #Se siente cansado regularmente?
        self.si6.setEnabled(True)
        self.no6.setEnabled(True)
        


    def activar6(self):
        self.si7.setEnabled(True)
        self.no7.setEnabled(True)
  
    def activar7(self): #Tienes dolor de pecho?
        self.si8.setEnabled(True)
        self.no8.setEnabled(True)


    def activar8(self):
        self.si9.setEnabled(True)
        self.no9.setEnabled(True)
        self.respuesta.setText("Probablemente Alzhaimer")

    def activar9(self):#Tienes tos
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
    
    

        
    #metodos para decisiones Si
    def sipresionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Tienes ojos cansados?")
        self.grid.addWidget(widget,1,2)
        self.grid.addWidget(widget1,2,2)
        
    def si3presionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Probablemente epilepsia")
        self.grid.addWidget(widget,3,2)
        self.grid.addWidget(widget1,4,2)
        
    def si4presionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Tienes dolor de garganta?")
        self.grid.addWidget(widget,5,2)
        self.grid.addWidget(widget1,6,2)
        
    def si5presionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Sinusitis o hipotermia")
        self.grid.addWidget(widget,7,2)
        self.grid.addWidget(widget1,8,2)
    
    def si6presionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Tiene dolor de pecho?")
        self.grid.addWidget(widget,3,4)
        self.grid.addWidget(widget1,4,4)
        
    def si8presionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Tiene dolor de garganta?")
        global contador
        contador = 1
        self.grid.addWidget(widget,5,4)
        self.grid.addWidget(widget1,6,4)
        
        
    def si9presionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Ictencia")
        self.grid.addWidget(widget,9,2)
        self.grid.addWidget(widget1,10,2)
    
    def si10presionado(self):
        widget = QtWidgets.QLabel("Si")
        widget1 = QtWidgets.QLabel("Golpe de calor o diabetes")
        self.grid.addWidget(widget,11,3)
        self.grid.addWidget(widget1,12,3)
        
    #metodos de No
    def nopresionado(self):
        widget = QtWidgets.QLabel("No")
        widget1 = QtWidgets.QLabel("Se siente cansado regularmente?")
        self.grid.addWidget(widget,1,4)
        self.grid.addWidget(widget1,2,4)
        
    def no3presionado(self):
        widget = QtWidgets.QLabel("No")
        widget1 = QtWidgets.QLabel("Tienes fiebre?")
        self.grid.addWidget(widget,3,3)
        self.grid.addWidget(widget1,4,3)
    
    def no4presionado(self):
        widget = QtWidgets.QLabel("No")
        widget1 = QtWidgets.QLabel("Probablemente Covid o Asma")
        self.grid.addWidget(widget,5,3)
        self.grid.addWidget(widget1,6,3)
        
    def no5presionado(self):
        widget = QtWidgets.QLabel("No")
        widget1 = QtWidgets.QLabel("Tienes tos?")
        self.grid.addWidget(widget,7,3)
        self.grid.addWidget(widget1,8,3)
    

    
    def no6presionado(self):
        widget = QtWidgets.QLabel("No")
        widget1 = QtWidgets.QLabel("Tienes dolor de garganta?")
        
        self.grid.addWidget(widget,3,6)
        self.grid.addWidget(widget1,4,6)
        
    def no9presionado(self):
        widget = QtWidgets.QLabel("No")
        widget1 = QtWidgets.QLabel("Tienes desmayos?")
        self.grid.addWidget(widget,9,4)
        self.grid.addWidget(widget1,10,4)
    
    def no10presionado(self):
        widget = QtWidgets.QLabel("No")
        widget1 = QtWidgets.QLabel("Problablemente Covid")
        self.grid.addWidget(widget,11,4)
        self.grid.addWidget(widget1,12,4)


    def cerrar(self):
         self.salir.clicked.connect(self.close)

calc = calculo()

sys.exit(app.exec_())