import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QMessageBox,QLabel

import hashlib
from bs4 import BeautifulSoup
import requests
import sqlite3

class IngresoUsuario(QMainWindow):
    def __init__(self):
        super(IngresoUsuario, self).__init__()
        loadUi("./interfaces/testDolar.ui", self)

        # Conecta el botón bt a la función calcularDivisa
        self.bt.clicked.connect(self.calcularDivisa)

    def calcularDivisa(self):
        url = 'https://www.bcv.org.ve'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        div_dolar = soup.find('div', id='dolar')

        divisa = div_dolar.find('strong').text

        # Eliminar espacios en blanco y comas
        divisa_limpia = divisa.replace(' ', '').replace(',', '.')

        # Convertir la cadena limpia en un número decimal
        valor_numerico = float(divisa_limpia)

        # Obtener la cantidad de dólares del QLineEdit en tu interfaz gráfica
        operacion = float(self.ln_bolivares.text())

        # Calcular la suma
        bolivares = operacion * valor_numerico

        # Formatear los valores con el formato "00,00"
        divisa_formateada = "{:.2f}".format(valor_numerico).replace(".", ",")
        suma_formateada = "{:.2f}".format(bolivares).replace(".", ",")

        # Mostrar los resultados en etiquetas o en otro lugar de tu interfaz gráfica
        self.label_3.setText("Valor de la divisa: " + divisa_formateada)
        self.label.setText("Costo en Bolívares: " + suma_formateada)
        print (suma_formateada)

    #     self.btn_login.clicked.connect(self.ingreso)
       
    #     self.bt_salir.clicked.connect(lambda : QApplication.quit())
        
        
   
    def cifrar_contrasenia(self, contrasenia):
        # Cifrar la contraseña usando un algoritmo de hash (SHA-256 en este caso)
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()
       
    def ingreso(self):
        nombre = self.txt_username.text()
        password = self.txt_password.text()

        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Users WHERE Username = ?", (nombre,))
        usuario = cursor.fetchone()

        if usuario:
            contrasenia_cifrada_ingresada = self.cifrar_contrasenia(password)
            contrasenia_cifrada_almacenada = usuario[1]  # Suponiendo que el hash se almacena en el segundo campo de la tabla
            if contrasenia_cifrada_ingresada == contrasenia_cifrada_almacenada:
            # Autenticación exitosa
                print("Inicio de sesión exitoso.")
            # Aquí puedes agregar código para abrir una nueva ventana o realizar acciones adicionales
            else:
            # Contraseña incorrecta
                print("Contraseña incorrecta.")
        else:
            print("Nombre de usuario no encontrado.")
    
        conexion.close()
        
   




app = QApplication(sys.argv)
IngresoUsuario = IngresoUsuario()
widget = QtWidgets.QStackedWidget()
widget.addWidget(IngresoUsuario)
widget.move(200, 80)
widget.setFixedHeight(500)
widget.setFixedWidth(800)
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()



try:
    sys.exit(app.exec_())
except:
    print("saliendo")