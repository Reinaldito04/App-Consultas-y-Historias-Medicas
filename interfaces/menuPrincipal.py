import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QPropertyAnimation , QEasingCurve
from PyQt5.QtWidgets import QHeaderView, QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QMessageBox,QLabel

class MenuPrincipal(QMainWindow):
    def __init__(self):
        super(MenuPrincipal , self). __init__()
        loadUi("./interfaces/menu.ui", self)
        self.frame_opciones.hide()
        
        self.bt_menu.clicked.connect(self.toggle_sidebar)
        self.bt_salir.clicked.connect(self.close)
        self.bt_home.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_home) )
        self.bt_registro.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_registro) )
        self.bt_paciente.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_pacientes) )
        self.bt_consulta.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_consulta) )
        self.bt_historial.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_historial) )
    
    def toggle_sidebar(self):
        if self.frame_opciones.isHidden():
            self.frame_opciones.show()
        else:
            self.frame_opciones.hide()
   
    def close(self):
       QApplication.quit()

app = QApplication(sys.argv)
MenuPrincipal = MenuPrincipal()
widget = QtWidgets.QStackedWidget()
widget.addWidget(MenuPrincipal)
widget.move(200, 80)
widget.setFixedHeight(600)
widget.setFixedWidth(900)
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()



try:
    sys.exit(app.exec_())
except:
    print("saliendo")