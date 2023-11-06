import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QStackedWidget,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
from PyQt5.QtWidgets import QDialog
import hashlib
import sqlite3
import os
import datetime
from bs4 import BeautifulSoup
import requests
from PyQt5.QtCore import Qt


class Ui_montos(QMainWindow):
    def __init__(self):
        super(Ui_montos, self).__init__()
        loadUi("./interfaces/montos.ui", self)
        self.setWindowTitle("Montos")
        self.btn_agg.clicked.connect(self.aggMontos)
        self.btn_clear.clicked.connect(self.clear)
        self.actionSalir.triggered.connect(self.salir)
        # self.actionVolver_al_menu_principal.triggered.connect(self.backM)
    def aggMontos(self):
     print("si")
       
    def salir(self):
        reply = QMessageBox.question(
            self,
             'Confirmación',
             '¿Desea Salir?',
             QMessageBox.Yes | QMessageBox.No,
             QMessageBox.Yes
         )
        if reply == QMessageBox.Yes:
             QApplication.quit()
            
    # def backM(self):
    #     conexion = sqlite3.connect('interfaces/database.db')
    #     cursor= conexion.cursor()
    #     cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
    #     resultado = cursor.fetchone()
    #     if resultado :
    #         nombre_usuario = resultado[0]
    #         horaActual = datetime.datetime.now().time()
            
    #         if datetime.time(5, 0, 0) <= horaActual < datetime.time(12, 0, 0):
    #             textForMenu = f"Buenos días {nombre_usuario}\n¿Qué deseas hacer hoy?"
    #         elif datetime.time(12, 0, 0) <= horaActual < datetime.time(18, 0, 0):
    #             textForMenu = f"Buenas tardes {nombre_usuario}\n¿Qué deseas hacer hoy?"
    #         elif datetime.time(18, 0, 0) <= horaActual or horaActual < datetime.time(5, 0, 0):
    #             textForMenu = f"Buenas noches {nombre_usuario}\n¿Qué deseas hacer hoy?"
    #         else:
    #             textForMenu = f"Hola {nombre_usuario}\n¿Qué deseas hacer hoy?"
    #         menu_principal = MenuPrincipal(self.id_user)
    #         menu_principal.lb_nombre.setText(textForMenu)

    #         # Establecer la ventana en modo de pantalla completa
    #         menu_principal.showMaximized()

    #         menu_principal.setWindowTitle("Menu Principal")

    #         # Asegúrate de añadir la ventana al widget después de establecerla en modo de pantalla completa
    #         widget.addWidget(menu_principal)
    #         widget.setCurrentIndex(widget.currentIndex() + 1)

    #         self.close()
            
    def clear(self):
        self.t_1.clear()
        self.t_2.clear()
        self.t_3.clear()
        self.t_4.clear()
        self.t_5.clear()
        self.t_6.clear()
        self.monto_1.clear()
        self.monto_2.clear()
        self.monto_3.clear()
        self.monto_4.clear()
        self.monto_5.clear()
        self.monto_6.clear()

if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("si")  # Establecer el nombre de la aplicación
    
    
    Montos=Ui_montos() 
    Montos.showFullScreen()   
    widget = QStackedWidget()
    widget.addWidget(Montos)
    widget.setGeometry(Montos.geometry())
 
    widget.show()
    sys.exit(app.exec_())
    
