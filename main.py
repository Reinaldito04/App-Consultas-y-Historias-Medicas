import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QIODevice , QUrl
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
from urllib3.exceptions import InsecureRequestWarning
from PyQt5.QtCore import Qt
import re
class IngresoUsuario(QMainWindow):
    def __init__(self):
        super(IngresoUsuario, self).__init__()
        loadUi("./interfaces/loggin.ui", self)
        self.setWindowTitle("Login")
        self.btn_login.clicked.connect(self.ingreso)
        self.btn_adduser.clicked.connect(self.ingresoRegistro)
        self.bt_salir.clicked.connect(self.salida)
        
        

    def salida(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea Salir?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()
            
    def ingresoRegistro(self):
        registroview = Registro()
        widget.addWidget(registroview)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        registroview.show()
        self.hide()

    def cifrar_contrasenia(self, contrasenia):
        # Cifrar la contraseña usando un algoritmo de hash (SHA-256 en este caso)
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()

    def get_greeting_message(self, nombre):
        hora_actual = datetime.datetime.now().time()
        if datetime.time(5, 0, 0) <= hora_actual < datetime.time(12, 0, 0):
            return f"Buenos días {nombre}\n¿Qué deseas hacer hoy?"
        elif datetime.time(12, 0, 0) <= hora_actual < datetime.time(18, 0, 0):
            return f"Buenas tardes {nombre}\n¿Qué deseas hacer hoy?"
        elif datetime.time(18, 0, 0) <= hora_actual or hora_actual < datetime.time(5, 0, 0):
            return f"Buenas noches {nombre}\n¿Qué deseas hacer hoy?"
        else:
            return f"Hola {nombre}\n¿Qué deseas hacer hoy?"

    def authenticate_user(self, username, password):
        if not username or not password:
            QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña.")
            return

        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Users WHERE Username = ?", (username,))
        usuario = cursor.fetchone()
        conexion.close()

        if usuario:
            contrasenia_cifrada_ingresada = self.cifrar_contrasenia(password)
            contrasenia_cifrada_almacenada = usuario[1]  # Suponiendo que el hash se almacena en el segundo campo de la tabla
            if contrasenia_cifrada_ingresada == contrasenia_cifrada_almacenada:
                text_for_menu = self.get_greeting_message(username)
                id_user = usuario[2]
                self.open_menu_principal(text_for_menu, id_user)
            else:
                QMessageBox.warning(self, "Error", "Contraseña Incorrecta.")
        else:
            QMessageBox.warning(self, "Error", "Nombre de usuario no encontrado.")

    def open_menu_principal(self, text_for_menu, id_user):
        menu_principal = MenuPrincipal(id_user)
        menu_principal.lb_nombre.setText(text_for_menu)
        
        # Establecer la ventana en modo de pantalla completa
        menu_principal.showMaximized()
       
        menu_principal.setWindowTitle("Menu Principal")

     
        # Asegúrate de añadir la ventana al widget después de establecerla en modo de pantalla completa
        widget.addWidget(menu_principal)
       
        widget.setCurrentIndex(widget.currentIndex() + 1)

        self.close()

    def ingreso(self):
        nombre = self.txt_username.text()
        password = self.txt_password.text()
        self.authenticate_user(nombre, password)
    
   
class Registro(QMainWindow):
    def __init__(self):
        super(Registro, self).__init__()
        loadUi("interfaces/dogtores.ui", self)
        self.btn_agg.clicked.connect(self.registrarUsuario)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.actionLogin.triggered.connect(self.login)
        self.actionSalir.triggered.connect(self.close)
        self.bt_photo.clicked.connect(self.addPhoto)
        self.in_cedula.textChanged.connect(self.verificar_existencia_cedula)
        self.in_mail.editingFinished.connect(self.mostrar_mensaje_mail)
        self.in_number.textChanged.connect(self.mostrar_mensaje_telefono)
        self.in_user.textChanged.connect(lambda: self.usuario_existe(nombre=self.in_user.text()))
    def login(self):
        ingreso_usuario.show()
        self.hide()
    def addPhoto(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, "Seleccionar imágenes", "", "Archivos de imagen (*.png *.jpg *.bmp)")
        
        if len(filenames) >= 1:
            pixmap1 = QPixmap(filenames[0])
            self.foto.setPixmap(pixmap1)
            
        else:
            QMessageBox.information(self,"Imagenes","Por favor,Selecciona una imagen") 
            
    def validar_correo_electronico(self, correo):
        patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(patron, correo) is not None    
    
    
    def mostrar_mensaje_mail(self):
        correo = self.in_mail.text()
        if self.validar_correo_electronico(correo):
           self.btn_agg.setEnabled(True) 
            
        else:
            QMessageBox.warning(self,"Correo invalido","Por favor introduzca un correo valido")
            self.btn_agg.setEnabled(False) 
            return
    def validar_numeros(self,cadena):
        
        patron = r'^[0-9]+$'
        return re.match(patron, cadena) is not None
    
    def mostrar_mensaje_telefono(self):
        numero = self.in_number.text()
        if self.validar_numeros(numero):
            self.btn_agg.setEnabled(True) 
        else:
            QMessageBox.information(self,"Solo numeros","Número inválido")
            self.btn_agg.setEnabled(False) 
            return
         
    def clearInputs(self):
        self.in_cedula.clear()
        self.in_name.clear()
        self.in_apell.clear()
        self.in_age.clear()
        self.in_mail.clear()
        self.in_number.clear()
        self.in_dir.clear()
        self.btn_m.setChecked(False)
        self.btn_f.setChecked(False)
        self.in_espec.clear()
        
        self.in_user.clear()
        self.in_password.clear()
        self.in_password_2.clear()    
        self.foto.clear()
    def cifrar_contrasenia(self, contrasenia):
        # Cifrar la contraseña usando un algoritmo de hash (SHA-256 en este caso)
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()
    
    def usuario_existe(self, nombre):
        # Conectar a la base de datos
        
        conexion = sqlite3.connect('interfaces/database.db')

        # Crear un cursor
        cursor = conexion.cursor()

        # Consultar si el usuario ya existe
        cursor.execute('SELECT COUNT(*) FROM Users WHERE Username = ?', (nombre,))
        resultado = cursor.fetchone()[0]

        # Cerrar la conexión
        conexion.close()

        # Si resultado es mayor que 0, significa que el usuario ya existe
        
        if resultado >0:
            QMessageBox.warning(self,"Error","El nombre de usuario ya existe. \nIngrese uno distinto")
            self.btn_agg.setEnabled(False)
            return
        else:
            self.btn_agg.setEnabled(True)
        
        

    
    def verificar_existencia_cedula(self):
        cedula = self.in_cedula.text()

        if not cedula:
            return

        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()

        # Consultar si ya existe alguien con la misma cédula
        cursor.execute('SELECT * FROM Users WHERE Cedula = ?', (cedula,))
        existe_cedula = cursor.fetchone() is not None

        conexion.close()

        if existe_cedula:
            QMessageBox.warning(self, "Error", "Ya existe alguien con la misma cédula.")
            self.btn_agg.setEnabled(False)
            return
        else:
            self.btn_agg.setEnabled(True)

    def registrarUsuario(self):
        cedula = self.in_cedula.text()
        nombre = self.in_name.text()
        apellido = self.in_apell.text()
        edad = self.in_age.text()
        mail = self.in_mail.text()
        valor_sexo = ""
        foto = self.foto.pixmap()
        if self.btn_m.isChecked():
            valor_sexo = "Masculino"
        elif self.btn_f.isChecked():
            valor_sexo = "Femenino"
        conexion = sqlite3.connect('interfaces/database.db')
        username = self.in_user.text()
        password = self.in_password.text()
        passwordRepeat = self.in_password_2.text()
        telefono = self.in_number.text()
        direccion = self.in_dir.text()
        especialidad = self.in_espec.text()
        if not cedula or not username or not nombre or not apellido or not edad or not valor_sexo or not mail or not telefono or not direccion or not especialidad:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos.")
            return
        if len( password or passwordRepeat) <=0:
            QMessageBox.critical(self,"Error","Digite su contraseña")
            return
        if foto is None :
            QMessageBox.warning(self,"Advertencia","Debes importar una imagen antes de guardar")
            return
        else :
           
            if len(username) < 6:
                QMessageBox.critical(self, "Error", "El nombre de usuario debe tener minimo 6 caracteres.")
                return
        
            if len(password) < 8:
                QMessageBox.critical(self, "Error", "La contraseña debe tener minimo 8 caracteres.")
                return
            if len(passwordRepeat) < 8:
                QMessageBox.critical(self, "Error", "La contraseña debe minimo tener 8 caracteres.")
                return
        
         
        if password == passwordRepeat:
            if self.usuario_existe(username):
                QMessageBox.warning(self, "Error", "El nombre de usuario ya existe. \nIngrese uno distinto")
                return
            else:
                foto_image = foto.toImage()  
                foto_bytes = QByteArray()
                buffer = QBuffer(foto_bytes)  
                buffer.open(QIODevice.WriteOnly)
                foto_image.save(buffer, "PNG")
                foto_bytes = buffer.data()
                buffer.close()
                # Conectar a la base de datos
                contrasenia_cifrada = self.cifrar_contrasenia(password)
                conexion = sqlite3.connect('interfaces/database.db')

                # Crear un cursor
                cursor = conexion.cursor()

                # Insertar datos en la base de datos
                cursor.execute('INSERT INTO Users (Username, Password ,Cedula ,Nombres, Apellidos, Sexo , Edad , Direccion , Telefono , Mail , Especialidad , Imagen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? , ?)', 
                               (username , contrasenia_cifrada , cedula ,nombre, apellido , valor_sexo , edad , direccion ,telefono , mail ,especialidad , foto_bytes ))

                # Confirmar los cambios en la base de datos y cerrar la conexión
                conexion.commit()
                conexion.close()

                QMessageBox.information(self, "Éxito", "Registro exitoso")
        else:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
            self.clearInputs()
            
    def close(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea Salir?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()

class MenuPrincipal(QMainWindow):
    def __init__(self, id_user):
        super(MenuPrincipal, self).__init__()
        loadUi("./interfaces/menu.ui", self)

        self.id_user = id_user
        self.setWindowTitle("MenuPrincipal")
        self.showMaximized()
        
        self.setupUi()
    
    def setupUi(self):
        self.frame_opciones.hide()
        self.bt_info.clicked.connect(self.informacionView)
        self.bt_menu.clicked.connect(self.toggle_sidebar)
        self.bt_salir.clicked.connect(self.close)
        self.bt_home.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.principal_tab))
        self.bt_registro.clicked.connect(self.Historyviews)
        self.bt_paciente.clicked.connect(self.PlacasView)
        self.bt_citas.clicked.connect(self.CitasView)
        self.bt_help.clicked.connect(self.ayuda)
        self.bt_act.clicked.connect(self.act_T)
        self.bt_buscar.clicked.connect(self.buscar)
        self.cargarCitas()
        self.filtro = self.findChild(QtWidgets.QComboBox, "filtro")
        self.filtro.addItem("Seleccione una opción para filtrar")
        self.filtro.addItems(["Dentista", "Cedula", "Nombre","Apellido", "Fecha_Cita", "Hora_Cita", "Estatus_Cita"])
        self.in_buscar.textChanged.connect(self.buscar)

    def act_T(self):
        self.cargarCitas()

    def cargarCitas(self, filtro=None, valor=None):
        self.tabla_cita.setRowCount(0)  # Limpiar la tabla actual
        headers = ["Cedula", "Nombre", "Apellido", "Fecha de la  cita", "Hora de la cita", "Estatus de la cita"]

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            if filtro and valor:
                cursor.execute("""
                SELECT 
                    Pacientes.Cedula, 
                    Pacientes.Nombre, 
                    Pacientes.Apellido, 
                    Cita.Fecha_Cita, 
                    Cita.Hora_Cita, 
                    Cita.Estatus_Cita
                FROM 
                    Pacientes
                INNER JOIN 
                    Cita ON Pacientes.Cedula = Cita.Cedula
                WHERE 
                    {} LIKE ? AND Pacientes.ID_user = ? 
                ORDER BY 
                    Cita.Fecha_Cita ASC
                """.format(filtro), ('%' + valor + '%', self.id_user))
            else:
                cursor.execute("""
                SELECT 
                    Pacientes.Cedula, 
                    Pacientes.Nombre, 
                    Pacientes.Apellido, 
                    Cita.Fecha_Cita, 
                    Cita.Hora_Cita, 
                    Cita.Estatus_Cita
                FROM 
                    Pacientes
                INNER JOIN 
                    Cita ON Pacientes.Cedula = Cita.Cedula
                WHERE 
                    Pacientes.ID_user = ? 
                ORDER BY 
                    Cita.Fecha_Cita ASC
                """, (self.id_user,))
            citas = cursor.fetchall() 

            self.tabla_cita.setColumnCount(len(headers))
            self.tabla_cita.setHorizontalHeaderLabels(headers)

            for row, cita in enumerate(citas):
                self.tabla_cita.insertRow(row)
                for column, value in enumerate(cita):
                    item = QtWidgets.QTableWidgetItem(str(value))
                    self.tabla_cita.setItem(row, column, item)

            conexion.close()
        except sqlite3.Error as e:
            QtWidgets.QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))

    def buscar(self):
        filtro = self.filtro.currentText()
        valor = self.in_buscar.text()
        if filtro == "Seleccione una opción para filtrar":
            QtWidgets.QMessageBox.warning(self, "Error", "Debe seleccionar un filtro para buscar")
        elif len(valor) == 0:
            self.act_T()
        elif not valor:
            QtWidgets.QMessageBox.warning(self, "Por favor", "Ingrese alguna especificación de la cita para realizar la búsqueda")
        elif self.tabla_cita.rowCount() == 0:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "No se ha encontrado ningún resultado")
            self.in_buscar.clear()
            self.act_T()
        else:
            self.cargarCitas(filtro, valor)

    
    def PlacasView(self):
        reply = self.showConfirmation("¿Deseas ir al formulario de placas?")
        if reply == QMessageBox.Yes:
            placa_view = Ui_placas(self.id_user)
            widget.addWidget(placa_view)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            placa_view.show()
            self.hide()
            
    def ayuda(self):
        dialog = helpView()
        dialog.exec_()
    def CitasView(self):
        reply = self.showConfirmation("¿Deseas ir al formulario de citas?")
        if reply == QMessageBox.Yes:
            citas = Ui_CitasMenu(self.id_user)
            widget.addWidget(citas)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            citas.show()
            self.hide()

    def informacionView(self):
        reply = self.showConfirmation("¿Deseas ir al formulario de cambiar data?")
        if reply == QMessageBox.Yes:
            doctorView = EditDoctor(self.id_user)
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT Cedula, Especialidad, Nombres, Apellidos, Sexo, Edad, Direccion, Telefono, Mail, Imagen FROM Users WHERE ID = ?", (self.id_user,))
            resultado = cursor.fetchone()
            if resultado:
                self.populateDoctorView(doctorView, resultado)
                widget.addWidget(doctorView)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                self.hide()

    def populateDoctorView(self, doctorView, data):
        doctorView.in_cedula_2.setText(data[0])
        doctorView.in_espec_2.setText(data[1])
        doctorView.in_name_2.setText(data[2])
        doctorView.in_apell_2.setText(data[3])
        doctorView.in_age_2.setText(data[5])
        doctorView.in_dir_2.setText(data[6])
        doctorView.in_number_2.setText(data[7])
        doctorView.in_mail_2.setText(data[8])
        if data[4] == "Masculino":
            doctorView.btn_m_2.setChecked(True)
        elif data[4] == "Femenino":
            doctorView.btn_f_2.setChecked(True)
        pixmap1 = QPixmap()
        pixmap1.loadFromData(data[9])
        doctorView.foto_2.setPixmap(pixmap1)

    def Historyviews(self):
        reply = self.showConfirmation("¿Desea ir al formulario de registro de pacientes?")
        if reply == QMessageBox.Yes:
            historia = historiaMenu(self.id_user)
            widget.addWidget(historia)
            widget.setCurrentIndex(widget.currentIndex() + 1)
            historia.show()
            self.hide()

    def showConfirmation(self, message):
        return QMessageBox.question(self, 'Confirmación', message, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

    def toggle_sidebar(self):
        self.frame_opciones.setHidden(not self.frame_opciones.isHidden())

    def close(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea Salir?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()
            
class helpView(QDialog):
    def __init__(self):
        super(helpView,self).__init__()
        loadUi('interfaces/help.ui', self)
        self.setWindowTitle('Información')
       
        self.click.setText('<a href="https://github.com/Reinaldito04/App-Consultas-y-Historias-Medicas">Haz Click aqui</a>')
        self.click.setOpenExternalLinks(True)
        self.click.linkActivated.connect(self.open_github_link)
        self.click.setStyleSheet("QLabel { text-decoration: none; }")

    def open_github_link(self):
        QDesktopServices.openUrl(QUrl('https://github.com/Reinaldito04/App-Consultas-y-Historias-Medicas'))

class EditDoctor(QMainWindow):
    def __init__(self,id_user):
        super(EditDoctor, self).__init__()
        self.id_user = id_user
        loadUi("interfaces/edicion.ui", self)
        self.btn_passwordChange.clicked.connect(self.PasswordView)
        self.bt_delete.clicked.connect(self.eliminarInfo)
        self.btn_save.clicked.connect(self.modifyInfo)
        self.btn_back.clicked.connect(self.back_menu)

     
    def back_menu(self):
        
        conexion = sqlite3.connect('interfaces/database.db')
        cursor= conexion.cursor()
        cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
        resultado = cursor.fetchone()
        if resultado :
            nombre_usuario = resultado[0]
            horaActual = datetime.datetime.now().time()
            
            if datetime.time(5, 0, 0) <= horaActual < datetime.time(12, 0, 0):
                textForMenu = f"Buenos días {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(12, 0, 0) <= horaActual < datetime.time(18, 0, 0):
                textForMenu = f"Buenas tardes {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(18, 0, 0) <= horaActual or horaActual < datetime.time(5, 0, 0):
                textForMenu = f"Buenas noches {nombre_usuario}\n¿Qué deseas hacer hoy?"
            else:
                textForMenu = f"Hola {nombre_usuario}\n¿Qué deseas hacer hoy?"
            menu_principal = MenuPrincipal(self.id_user)
            menu_principal.lb_nombre.setText(textForMenu)
          
            # Establecer la ventana en modo de pantalla completa
            menu_principal.showMaximized()

            menu_principal.setWindowTitle("Menu Principal")
            
            # Asegúrate de añadir la ventana al widget después de establecerla en modo de pantalla completa
            widget.addWidget(menu_principal)
            widget.setCurrentIndex(widget.currentIndex() + 1)

            self.close()
    def modifyInfo(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            'Deseas cambiar tu información personal?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
            
        if self.btn_m_2.isChecked():
               sexo = "Masculino"
        if self.btn_f_2.isChecked():
                sexo = "Femenino"
        if reply == QMessageBox.Yes:
           conexion = sqlite3.connect('interfaces/database.db')
           cursor = conexion.cursor()
           cedula = self.in_cedula_2.text()
           especialidad = self.in_espec_2.text()
           nombre = self.in_name_2.text()
           apellido = self.in_apell_2.text()
           direccion = self.in_dir_2.text()
           telefono  = self.in_number_2.text()
           edad = self.in_age_2.text()
           mail = self.in_mail_2.text()
           
           
           cursor.execute("UPDATE Users SET Cedula = ?, Especialidad = ?, Nombres = ?, Apellidos = ?, Direccion = ?, Telefono = ?, Mail = ?, Sexo = ?, Edad = ? WHERE ID = ?", (cedula, especialidad, nombre, apellido, direccion, telefono, mail, sexo, edad, self.id_user))
           QMessageBox.information(self,"Realizado","Los cambios han sido guardados correctamente")
           conexion.commit()    
           conexion.close()
        
        
           
    def eliminarInfo(self):
        eliminarData = DeleteAllData(self.id_user)
        widget.addWidget(eliminarData)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        self.hide()
            
    def PasswordView(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Deseas cambiar tu contraseña?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply ==QMessageBox.Yes:
            passwordview = PasswordMenu(self.id_user)
           
            widget.addWidget(passwordview)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
            self.hide()
            
class DeleteAllData(QMainWindow):
    def __init__(self,id_user):
        super(DeleteAllData , self).__init__()
        self.id_user = id_user
        loadUi("interfaces/eliminarData.ui", self)
        self.bt_back.clicked.connect(self.back)
        self.bt_delete.clicked.connect(self.deleteData)
        
    def cifrar_contrasenia(self, contrasenia):
        # Cifrar la contraseña usando un algoritmo de hash (SHA-256 en este caso)
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()
    def deleteData(self):
        contraseniaaAntigua = self.ln_password.text()
        contraseniaRepeat = self.ln_repeatPassword.text()
        iduser=self.id_user
        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Estas seguro de eliminar tu información?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes :
            try:
                cursor.execute("SELECT Password, Username From Users WHERE ID =? ", (iduser,))
                resultado = cursor.fetchone()
                if resultado and resultado[0] ==  self.cifrar_contrasenia(contraseniaaAntigua):
                    if contraseniaaAntigua  == contraseniaRepeat :
                       
                        nombre = resultado[1]
                        cursor.execute('BEGIN TRANSACTION;')
                        cursor.execute("DELETE FROM Users WHERE ID =?",(self.id_user,))
                        cursor.execute('DELETE FROM Pacientes WHERE ID_user = ?', (self.id_user,))
                        conexion.commit()
                        QMessageBox.information(self,'Exito',f'Felicidades {nombre} tus datos han sido eliminado correctamente')
                        registro = Registro()
                        widget.addWidget(registro)
                        widget.setCurrentIndex(widget.currentIndex()+1)
                        
                    else:
                        QMessageBox.information(self,'Error','Las contraseñas no coinciden.')
                else:
                    QMessageBox.information(self,'Error','La contraseña es incorrecta.')
            except sqlite3.Error as e:
                print(f"Error de base de datos: {e}")
            finally:
                conexion.close()
         
    def back(self):
            doctorView = EditDoctor(self.id_user)
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT Cedula,Especialidad,Nombres,Apellidos,Sexo,Edad,Direccion,Telefono,Mail , Imagen FROM Users WHERE ID = ?", (self.id_user,))
            resultado = cursor.fetchone()
            if resultado :
                doctorView.in_cedula_2.setText(resultado[0])
                doctorView.in_espec_2.setText(resultado[1])
                doctorView.in_name_2.setText(resultado[2])
                doctorView.in_apell_2.setText(resultado[3])
                doctorView.in_age_2.setText(resultado[5])
                doctorView.in_dir_2.setText(resultado[6])
                doctorView.in_number_2.setText(resultado[7])
                doctorView.in_mail_2.setText(resultado[8])
                sexo = resultado[4]
                if sexo == "Masculino":
                    doctorView.btn_m_2.setChecked(True)
                if sexo == "Femenino":
                    doctorView.btn_f_2.setChecked(True)
                pixmap1 = QPixmap()
                pixmap1.loadFromData(resultado[9])
                doctorView.foto_2.setPixmap(pixmap1)
            widget.addWidget(doctorView)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
            self.hide()
        
class Ui_CitasMenu(QMainWindow):
    def __init__(self,id_user):
        super(Ui_CitasMenu, self).__init__()
        self.id_user = id_user
        loadUi("interfaces/citas.ui", self)
        self.actionVolver_al_menu_principal.triggered.connect(self.back)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_buscar.clicked.connect(self.searchdata)
        self.btn_agg.clicked.connect(self.aggCite)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_edit.clicked.connect(self.editarCita)
        #self.btn_delete.clicked.connect(self.eliminarCita)
        self.setWindowTitle("Menu de Citas")
        self.showMaximized()
    def eliminarCita(self):
        try:
            cedula = self.in_busqueda.text()
    
            if len(cedula) == 0:
                QMessageBox.critical(self, "Error", "Ingrese una cédula")
            else:
              
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM Cita WHERE Cedula = ?", (cedula,))

                conexion.commit()
                conexion.close()
        
        # Eliminación exitosa, muestra un mensaje y realiza otras acciones si es necesario
                QMessageBox.information(self, "Realizado", "La cita ha sido eliminada correctamente")
                
                self.clear()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al eliminar la cita  de la base de datos: " + str(e))
       
    def clear(self):
        self.in_busqueda.clear()
        self.txt_name.clear()
        self.txt_apell.clear()
        self.tableWidget.setRowCount(0)
        
    def editarCita(self):
        idUser = self.id_user
        cedula = self.in_busqueda.text()
        
        fecha = self.fecha.selectedDate()
        fechaToString = fecha.toString('yyyy-MM-dd')
        statusCita = None
        if self.bt_act.isChecked():
            statusCita = 'Activa'
        if self.bt_cancel.isChecked():
            statusCita = 'Cancelada'
        hora = self.hora.time()
        horaToString = hora.toString('hh:mm:ss')
        
        try:
            if not cedula:
                QMessageBox.warning(self,"Introduzca una cedula","Debes introducir una cedula antes de editar")
                return
            reply = QMessageBox.question(
                self,
                'Confirmación',
                '¿Desea cambiar la fecha y hora de la cita?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
            
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                
                # Verificar si existe un paciente con la cédula proporcionada
                cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
                existe_paciente = cursor.fetchone()[0] > 0
                
                if existe_paciente:
                    # Si el paciente existe, proceder a actualizar la cita
                    cursor.execute("""
                        UPDATE Cita 
                        SET Fecha_Cita = ?, Hora_Cita = ?, Estatus_Cita = ?
                        WHERE Cedula = ? 
                    """, (fechaToString, horaToString, statusCita, cedula))
        
                    # Guardar los cambios en la base de datos
                    conexion.commit()
                    
                    # Mostrar un mensaje de éxito
                    QMessageBox.information(self, "Información", "Cita actualizada con éxito.")
                else:
                    # Si el paciente no existe, mostrar un mensaje de error
                    QMessageBox.warning(self, "Advertencia", "No se encontró un paciente con la cédula proporcionada.")
                
                # Cerrar la conexión con la base de datos
                conexion.close()
            
        except sqlite3.Error as error:
            # En caso de error, mostrar un mensaje de error
            QMessageBox.critical(self, "Error", f"Error al actualizar la cita: {str(error)}")

    def aggCite(self):
       
        cedula = self.in_busqueda.text()
        
        fecha = self.fecha.selectedDate()
        fechaToString = fecha.toString('yyyy-MM-dd')
        statusCita = None
        if self.bt_act.isChecked():
            statusCita = 'Activa'
        if self.bt_cancel.isChecked():
            statusCita = 'Cancelada'
        hora = self.hora.time()
        horaToString = hora.toString('hh:mm:ss')
        
        try:
            if not cedula:
                QMessageBox.warning(self,"Introduzca una cedula","Debes introducir una cedula antes de guardar")
                return
            reply = QMessageBox.question(
                self,
                'Confirmación',
                '¿Deseas agregar la cita?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes
            )
            if reply == QMessageBox.Yes:
            
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                
                # Verificar si existe un paciente con la cédula proporcionada
                cursor.execute("SELECT COUNT(*) FROM Cita WHERE Cedula = ?", (cedula,))
                existe_paciente = cursor.fetchone()[0] > 0
                
                if existe_paciente:
                    QMessageBox.information(self,"Cita","Ya el paciente tiene una cita registrada")
                    return
                elif not existe_paciente:
                    # Si el paciente existe, proceder a actualizar la cita
                    cursor.execute("""
                                    INSERT INTO Cita (Cedula, Fecha_Cita, Hora_Cita, Estatus_Cita)
                                    VALUES (?, ?, ?, ?)
                                """, (cedula, fechaToString, horaToString, statusCita))
                    
                    # Guardar los cambios en la base de datos
                    conexion.commit()
                    
                    # Mostrar un mensaje de éxito
                    QMessageBox.information(self, "Información", "Cita agregada con éxito.")
                else:
                    # Si el paciente no existe, mostrar un mensaje de error
                    QMessageBox.warning(self, "Advertencia", "No se encontró un paciente con la cédula proporcionada.")
                
                # Cerrar la conexión con la base de datos
                conexion.close()
            
        except sqlite3.Error as error:
            # En caso de error, mostrar un mensaje de error
            QMessageBox.critical(self, "Error", f"Error al actualizar la cita: {str(error)}")

    def searchdata(self):
        idUser = self.id_user
        cedula = self.in_busqueda.text()
        
        if len(cedula) <= 0:
            QMessageBox.warning(self, "Error", "Ingrese una cedula")
            return  # Salir de la función si no hay cédula

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            cursor.execute("""
                            SELECT 
                            Pacientes.Cedula, 
                            Pacientes.Nombre, 
                            Pacientes.Apellido, 
                            Cita.Fecha_Cita, 
                            Cita.Hora_Cita, 
                            Cita.Estatus_Cita
                        FROM 
                            Pacientes
                        INNER JOIN 
                            Cita ON Pacientes.Cedula = Cita.Cedula
                        WHERE 
                            Pacientes.Cedula = ? AND Pacientes.ID_user = ?"""
                           
                           , (cedula, idUser))
            tabla_cita = cursor.fetchall()

            # Filtrar los resultados para eliminar las filas con None
        
            if tabla_cita:
                for cita in tabla_cita:
                  
                    cedula = cita[0]
                    nombre = cita[1]
                    apellido = cita[2]
                    fecha = cita[3]
                    hora = cita[4]
                    estatus = cita[5]
                    # Limpiar la tabla existente si es necesario
                    self.tableWidget.clearContents()

                    # Establecer el número de filas y columnas en la tabla
                    self.tableWidget.setRowCount(len(tabla_cita))
                    self.tableWidget.setColumnCount(len(tabla_cita[0]))

                    # Agregar los datos a la tabla
                    for row, paciente in enumerate(tabla_cita):
                        for column, value in enumerate(paciente):
                            item = QTableWidgetItem(str(value))
                            self.tableWidget.setItem(row, column, item)

                    self.txt_name.setText(nombre)
                    self.txt_apell.setText(apellido)
                    fecha_cita = fecha
                  
                    self.fecha.setSelectedDate(QDate.fromString(fecha_cita, 'yyyy-MM-dd'))
                    hora_cita = QTime.fromString(hora, 'hh:mm:ss')
                    
                    if estatus =='Activa':
                        self.bt_act.setChecked(True)
                    if estatus == 'Cancelada':
                        self.bt_cancel.setChecked(True)
                    
                    self.hora.setTime(hora_cita)
                    
            else:
                    # Manejar el caso en el que no se encontraron resultados, por ejemplo, mostrar un mensaje de error
                QMessageBox.warning(self, "Sin resultados", "El paciente no tiene citas actualmente")

                    # Si deseas mostrar el nombre y apellido incluso si no hay cita, puedes hacerlo aquí
                cursor.execute("SELECT Nombre, Apellido FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (cedula, idUser))
                datos_paciente = cursor.fetchone()
                    
                if datos_paciente:
                    nombre_paciente, apellido_paciente = datos_paciente
                    self.txt_name.setText(nombre_paciente)
                    self.txt_apell.setText(apellido_paciente)
                else:
                    QMessageBox.warning(self, "Sin resultados", "No se encontró al paciente")
        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al buscar paciente: {str(error)}")
        finally:
            conexion.close()

    def back(self):
        
        conexion = sqlite3.connect('interfaces/database.db')
        cursor= conexion.cursor()
        cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
        resultado = cursor.fetchone()
        if resultado :
            nombre_usuario = resultado[0]
            horaActual = datetime.datetime.now().time()
            
            if datetime.time(5, 0, 0) <= horaActual < datetime.time(12, 0, 0):
                textForMenu = f"Buenos días {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(12, 0, 0) <= horaActual < datetime.time(18, 0, 0):
                textForMenu = f"Buenas tardes {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(18, 0, 0) <= horaActual or horaActual < datetime.time(5, 0, 0):
                textForMenu = f"Buenas noches {nombre_usuario}\n¿Qué deseas hacer hoy?"
            else:
                textForMenu = f"Hola {nombre_usuario}\n¿Qué deseas hacer hoy?"
            menu_principal = MenuPrincipal(self.id_user)
            menu_principal.lb_nombre.setText(textForMenu)

            # Establecer la ventana en modo de pantalla completa
            menu_principal.showMaximized()

            menu_principal.setWindowTitle("Menu Principal")

            # Asegúrate de añadir la ventana al widget después de establecerla en modo de pantalla completa
            widget.addWidget(menu_principal)
            widget.setCurrentIndex(widget.currentIndex() + 1)

            self.close()
            
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
class PasswordMenu(QMainWindow):
    def __init__(self,id_user ):
        super(PasswordMenu, self).__init__()
        self.id_user = id_user
        loadUi("interfaces/password.ui", self)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_menu.clicked.connect(self.returnMenu)
        self.bt_passwordChange.clicked.connect(self.cambiarPassword)
    
    def cifrar_contrasenia(self, contrasenia):
        # Cifrar la contraseña usando un algoritmo de hash (SHA-256 en este caso)
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()
    
    def cambiarPassword(self):
        contraseniaaAntigua = self.txt_passwordOld.text()
        contraseniaNew = self.txt_passwordNew.text()
        contraseniaRepeat = self.txt_passowrdRepeat.text()
        iduser=self.id_user
        
        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Estas seguro de cambiar tu contraseña?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes :
            try:
                cursor.execute("SELECT Password , Username From Users WHERE ID =? ", (iduser,))
                resultado = cursor.fetchone()
                if resultado and resultado[0] ==  self.cifrar_contrasenia(contraseniaaAntigua):
                    if contraseniaNew  == contraseniaRepeat :
                        contraseniaCifrada = self.cifrar_contrasenia(contraseniaNew)
                        nombre = resultado[1]
                        cursor.execute("UPDATE Users SET Password= ? WHERE ID= ?", (contraseniaCifrada , iduser))
                        conexion.commit()
                        QMessageBox.information(self,'Exito',f'Felicidades {nombre} tu contraseña ha sido cambiada correctamente') 
                    else:
                        QMessageBox.information(self,'Error','Las contraseñas no coinciden.')
                else:
                    QMessageBox.information(self,'Error','La contraseña antigua no es valida.')       
            except sqlite3.Error as e:
                print(f"Error de base de datos: {e}")
            finally:
                conexion.close()
    def returnMenu(self):
            doctorView = EditDoctor(self.id_user)
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT Cedula,Especialidad,Nombres,Apellidos,Sexo,Edad,Direccion,Telefono,Mail , Imagen FROM Users WHERE ID = ?", (self.id_user,))
            resultado = cursor.fetchone()
            if resultado :
                doctorView.in_cedula_2.setText(resultado[0])
                doctorView.in_espec_2.setText(resultado[1])
                doctorView.in_name_2.setText(resultado[2])
                doctorView.in_apell_2.setText(resultado[3])
                doctorView.in_age_2.setText(resultado[5])
                doctorView.in_dir_2.setText(resultado[6])
                doctorView.in_number_2.setText(resultado[7])
                doctorView.in_mail_2.setText(resultado[8])
                sexo = resultado[4]
                if sexo == "Masculino":
                    doctorView.btn_m_2.setChecked(True)
                if sexo == "Femenino":
                    doctorView.btn_f_2.setChecked(True)
                pixmap1 = QPixmap()
                pixmap1.loadFromData(resultado[9])
                doctorView.foto_2.setPixmap(pixmap1)
            widget.addWidget(doctorView)
            widget.setCurrentIndex(widget.currentIndex()+1)
            
            self.hide()
        
 
class ImagePopup(QDialog):
    def __init__(self):
        super().__init__()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        self.setWindowTitle('Vista completa de la imagen')
        self.center()
        self.setFixedSize(600, 600)
        
    def show_image(self, pixmap):
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)
        self.exec_()  # Muestra la ventana emergente como modal

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Ui_placas(QMainWindow):
    def __init__(self,id_user):
        super(Ui_placas, self).__init__()
        loadUi("interfaces/placas.ui", self)
        self.id_user = id_user
        self.btn_agg.clicked.connect(self.addplacas)
        self.btn_edit.clicked.connect(self.editar)
        self.btn_buscar.clicked.connect(self.searchData)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.btn_clear_2.clicked.connect(self.clearInputs_2)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_import.clicked.connect(self.addPhoto)
        self.actionVolver_al_menu_principal.triggered.connect(self.back_menu)
        self.showMaximized()
        
        self.btn_buscar_2.clicked.connect(self.buscarDatos)
        self.img1.mousePressEvent = lambda event: self.show_image_popup(self.img1.pixmap())
        self.img2.mousePressEvent = lambda event: self.show_image_popup(self.img2.pixmap())
        self.img3.mousePressEvent = lambda event: self.show_image_popup(self.img3.pixmap())
        self.img4.mousePressEvent = lambda event: self.show_image_popup(self.img4.pixmap())
        self.img5.mousePressEvent = lambda event: self.show_image_popup(self.img5.pixmap())
        self.img6.mousePressEvent = lambda event: self.show_image_popup(self.img6.pixmap())
        
    def editar(self):
        cedula = self.in_busqueda.text()
        foto_pixmap1  =self.img1.pixmap()
        foto_pixmap2  =self.img2.pixmap()
        foto_pixmap3  =self.img3.pixmap()
        if foto_pixmap1 is None or foto_pixmap2 is None or foto_pixmap3 is None:
            QMessageBox.warning(self,"Advertencia","Debes importar 3 imagenes antes de guardar")
            return
        if len(cedula) <=0 :
             QMessageBox.warning(self,"Advertencia","Debes ingresar la cedula para almacenar las placas")
             return
        else:
            try:
                foto1_image = foto_pixmap1.toImage()
                foto2_image = foto_pixmap2.toImage()
                foto3_image = foto_pixmap3.toImage()

                # Convierte cada imagen a un formato de bytes (por ejemplo, PNG)
                foto1_bytes = QByteArray()
                buffer1 = QBuffer(foto1_bytes)
                buffer1.open(QIODevice.WriteOnly)
                foto1_image.save(buffer1, "PNG")
                foto1_byte = buffer1.data()
                buffer1.close()

                foto2_bytes = QByteArray()
                buffer2 = QBuffer(foto2_bytes)
                buffer2.open(QIODevice.WriteOnly)
                foto2_image.save(buffer2, "PNG")
                foto2_byte = buffer2.data()
                buffer2.close()

                foto3_bytes = QByteArray()
                buffer3 = QBuffer(foto3_bytes)
                buffer3.open(QIODevice.WriteOnly)
                foto3_image.save(buffer3, "PNG")
                foto3_byte = buffer3.data()
                buffer3.close()
                
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                reply = QMessageBox.question(
                    self,
                    'Confirmación',
                    '¿Desea editar las placas ya guardadas?',
                    QMessageBox.Yes | QMessageBox.No,
                    QMessageBox.Yes
                )
                if reply == QMessageBox.Yes:
                    cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
                    
                    cursor.execute("UPDATE Pacientes SET Placa1 = ?, Placa2 = ? ,Placa3 = ? WHERE Cedula = ?",
                    (foto1_byte, foto2_byte, foto3_byte ,cedula ))
                    QMessageBox.information(self, "Exito", "Datos Guardados Correctamente ")
                    conexion.commit()
                    conexion.close()
                    self.clearInputs()
                return
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))
    def back_menu(self):
        
        conexion = sqlite3.connect('interfaces/database.db')
        cursor= conexion.cursor()
        cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
        resultado = cursor.fetchone()
        if resultado :
            nombre_usuario = resultado[0]
            horaActual = datetime.datetime.now().time()
            
            if datetime.time(5, 0, 0) <= horaActual < datetime.time(12, 0, 0):
                textForMenu = f"Buenos días {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(12, 0, 0) <= horaActual < datetime.time(18, 0, 0):
                textForMenu = f"Buenas tardes {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(18, 0, 0) <= horaActual or horaActual < datetime.time(5, 0, 0):
                textForMenu = f"Buenas noches {nombre_usuario}\n¿Qué deseas hacer hoy?"
            else:
                textForMenu = f"Hola {nombre_usuario}\n¿Qué deseas hacer hoy?"
            menu_principal = MenuPrincipal(self.id_user)
            menu_principal.lb_nombre.setText(textForMenu)

            # Establecer la ventana en modo de pantalla completa
            menu_principal.showMaximized()

            menu_principal.setWindowTitle("Menu Principal")

            # Asegúrate de añadir la ventana al widget después de establecerla en modo de pantalla completa
            widget.addWidget(menu_principal)
            widget.setCurrentIndex(widget.currentIndex() + 1)

            self.close()

    def show_image_popup(self, pixmap):
        if pixmap:
            
            # Crea una nueva ventana emergente y muestra la imagen
            image_popup = ImagePopup()
            image_popup.show_image(pixmap)

            # Conecta la señal accepted de la ventana emergente para habilitar la ventana principal nuevamente
            image_popup.accepted.connect(self.enable_main_window)

    def enable_main_window(self):
        # Habilita la ventana principal cuando se cierra la ventana emergente
        self.setEnabled(True)
            
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
       
    def clearInputs(self):
        self.in_busqueda.clear()
        self.in_name.clear()
        self.in_apell.clear()
        self.img1.clear()
        self.img2.clear()
        self.img3.clear()
    
    def clearInputs_2(self):
        self.in_busqueda_2.clear()
        self.in_apell_2.clear()
        self.in_name_2.clear()
        self.img4.clear()
        self.img5.clear()
        self.img6.clear()
        
    def addplacas(self):
        cedula = self.in_busqueda.text()
        foto_pixmap1  =self.img1.pixmap()
        foto_pixmap2  =self.img2.pixmap()
        foto_pixmap3  =self.img3.pixmap()
        if foto_pixmap1 is None or foto_pixmap2 is None or foto_pixmap3 is None:
            QMessageBox.warning(self,"Advertencia","Debes importar 3 imagenes antes de guardar")
            return
        if len(cedula) <=0 :
             QMessageBox.warning(self,"Advertencia","Debes ingresar la cedula para almacenar las placas")
             return
        else:
            try:
                foto1_image = foto_pixmap1.toImage()
                foto2_image = foto_pixmap2.toImage()
                foto3_image = foto_pixmap3.toImage()

                # Convierte cada imagen a un formato de bytes (por ejemplo, PNG)
                foto1_bytes = QByteArray()
                buffer1 = QBuffer(foto1_bytes)
                buffer1.open(QIODevice.WriteOnly)
                foto1_image.save(buffer1, "PNG")
                foto1_byte = buffer1.data()
                buffer1.close()

                foto2_bytes = QByteArray()
                buffer2 = QBuffer(foto2_bytes)
                buffer2.open(QIODevice.WriteOnly)
                foto2_image.save(buffer2, "PNG")
                foto2_byte = buffer2.data()
                buffer2.close()

                foto3_bytes = QByteArray()
                buffer3 = QBuffer(foto3_bytes)
                buffer3.open(QIODevice.WriteOnly)
                foto3_image.save(buffer3, "PNG")
                foto3_byte = buffer3.data()
                buffer3.close()
                
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                
                cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
                existe_paciente = cursor.fetchone()[0]

                if existe_paciente > 0:
                    QMessageBox.critical(self, "Error", "El paciente ya tiene placas registradas.")
                    
                #limpia los campos luego de denegar el ingreso
                self.clearInputs()
                
                if existe_paciente < 0:
                    cursor.execute("UPDATE Pacientes SET Placa1 = ?, Placa2 = ? ,Placa3 = ? WHERE Cedula = ?",
                    (foto1_byte, foto2_byte, foto3_byte ,cedula ))
                    QMessageBox.information(self, "Exito", "Datos Guardados Correctamente ")
                conexion.commit()
                conexion.close()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))
        
    def searchData(self):
        idUser = self.id_user
        cedula =self.in_busqueda.text()
        if len(cedula) <=0:
            QMessageBox.warning(self,"Error","Ingrese una cedula")
        else:
            
            try:
                conexion = sqlite3.connect('./interfaces/database.db')
                cursor = conexion.cursor()
                cursor.execute("SELECT Nombre , Apellido FROM Pacientes WHERE Cedula = ? AND ID_user = ?",(cedula, idUser))
                resultado = cursor.fetchone()
                conexion.close()
                if resultado :
                    nombre_paciente ,apellido_paciente = resultado
                    self.in_name.setText(nombre_paciente)
                    self.in_apell.setText(apellido_paciente)
                else:
                    QMessageBox.critical(self,"Error","El paciente no fue encontrado")
            except sqlite3.Error as error:
                QMessageBox.critical(self, "Error", f"Error al buscar paciente: {str(error)}")

    def addPhoto(self):
            filenames, _ = QFileDialog.getOpenFileNames(self, "Seleccionar imágenes", "", "Archivos de imagen (*.png *.jpg *.bmp *.jpeg *.JFIF)")
                
            if len(filenames) >= 3:
                    pixmap1 = QPixmap(filenames[0])
                    pixmap2 = QPixmap(filenames[1])
                    pixmap3 = QPixmap(filenames[2])
                    
                    self.img1.setPixmap(pixmap1)    
                    self.img2.setPixmap(pixmap2)
                    self.img3.setPixmap(pixmap3)
            else:
                    QMessageBox.information(self,"Imagenes","Por favor,Selecciona una imagen")    
    
    def buscarDatos(self):
        cedula = self.in_busqueda_2.text()
        idUser = self.id_user
        if len(cedula)<= 0:
         QMessageBox.warning(self,"Advertencia","Ingrese una Cédula")
        else:
            try:
                conexion = sqlite3.connect('./interfaces/database.db')
                cursor =conexion.cursor()
                cursor.execute("SELECT Nombre , Apellido , Placa1, Placa2, Placa3 FROM Pacientes WHERE Cedula = ? AND ID_user = ?",(cedula, idUser))
                resultado = cursor.fetchone()
                if resultado:
                    nombre_paciente , apellido_paciente ,placa1 , placa2,placa3 = resultado
                    self.in_name_2.setText(nombre_paciente)
                    self.in_apell_2.setText(apellido_paciente)
                    pixmap1 = QPixmap()
                    pixmap1.loadFromData(placa1)
                    self.img4.setPixmap(pixmap1)
                    
                    pixmap2 = QPixmap()
                    pixmap2.loadFromData(placa2)
                    self.img5.setPixmap(pixmap2)
                    
                    pixmap3 = QPixmap()
                    pixmap3.loadFromData(placa3)
                    self.img6.setPixmap(pixmap3)
                else:
                    QMessageBox.information(self,"Eror","No se encuentra datos")
                    return
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))                   
    def searchAll(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            idUser = self.id_user

            # Ejecuta una consulta para obtener los datos de los pacientes y ordenar por Fecha_Cita descendente
            cursor.execute("SELECT Cedula, Nombre, Apellido, Placa1 , Placa2 , Placa3   FROM Pacientes WHERE ID_user = ? ", (idUser,))
            tabla_placas = cursor.fetchall()
            conexion.close()

            # Filtrar las filas que no contengan ningún valor 'None'
            filas_filtradas = [paciente for paciente in tabla_placas if None not in paciente]

            # Limpiar la tabla existente si es necesario
            self.tabla_placas.clearContents()

            # Establecer el número de filas y columnas en la tabla
            self.tabla_placas.setRowCount(len(filas_filtradas))
            self.tabla_placas.setColumnCount(len(filas_filtradas[0]))

            # Agregar los datos a la tabla
            for row, paciente in enumerate(filas_filtradas):
                for column, value in enumerate(paciente):
                    if column == 6:  
                        if value == 1:
                           
                            item = QTableWidgetItem("Imágenes disponibles")
                        else:
                               item = QTableWidgetItem("No hay imágenes")
                    elif column in [3, 4, 5]:  # Supongamos que las columnas 3, 4 y 5 contienen las rutas de las imágenes
                        if value is not None and os.path.exists(value):                           
                            pixmap = QPixmap(value)
                            if not pixmap.isNull():
                                item = QTableWidgetItem()
                                item.setData(Qt.DecorationRole, pixmap)
                            else:
                               
                                item = QTableWidgetItem("Imagen dañada")
                        else:
                        
                            item = QTableWidgetItem("Imagen faltante")
                    else:
                        item = QTableWidgetItem(str(value))
                    self.tabla_placas.setItem(row, column, item)
        except:
            QMessageBox.critical(self, "Error", "No hay pacientes con placas actualmente.")
            
    def searchForDelete(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            idUser = self.id_user
            cedula = self.in_busqueda_3.text()
            if len(cedula)<= 0:
                QMessageBox.critical(self,"Error","Ingrese la cedula primeramente")
                return
            else:
                
                # Ejecuta una consulta para obtener los datos de los pacientes y ordenar por Fecha_Cita descendente
                cursor.execute("SELECT Cedula, Nombre, Apellido, Placa1 , Placa2 , Placa3   FROM Pacientes WHERE ID_user = ? AND Cedula = ? ", (idUser,cedula ))
                tabla_placas = cursor.fetchall()
                conexion.close()

                # Filtrar las filas que no contengan ningún valor 'None'
                filas_filtradas = [paciente for paciente in tabla_placas if None not in paciente]

                # Limpiar la tabla existente si es necesario
                self.tabla_delete.clearContents()

                # Establecer el número de filas y columnas en la tabla
                self.tabla_delete.setRowCount(len(filas_filtradas))
                self.tabla_delete.setColumnCount(len(filas_filtradas[0]))

                # Agregar los datos a la tabla
                for row, paciente in enumerate(filas_filtradas):
                    for column, value in enumerate(paciente):
                        if column == 6:  # Supongamos que la columna 6 es "ImagenesDisponibles"
                            if value == 1:
                                # El paciente tiene imágenes, muestra un mensaje o icono personalizado
                                item = QTableWidgetItem("Imágenes disponibles")
                            else:
                                # El paciente no tiene imágenes, muestra un mensaje o icono personalizado
                                item = QTableWidgetItem("No hay imágenes")
                        elif column in [3, 4, 5]:  # Supongamos que las columnas 3, 4 y 5 contienen las rutas de las imágenes
                            if value is not None and os.path.exists(value):
                                pixmap = QPixmap(value)
                                if not pixmap.isNull():
                                    item = QTableWidgetItem()
                                    item.setData(Qt.DecorationRole, pixmap)
                                else:
                                    # La imagen está dañada
                                    # Mostrar un ícono de error en lugar de la imagen
                                    item = QTableWidgetItem("Imagen dañada")
                            else:
                                # La imagen está ausente
                                # Mostrar un ícono de imagen faltante en lugar de la imagen
                                item = QTableWidgetItem("Imagen faltante")
                        else:
                            item = QTableWidgetItem(str(value))
                        self.tabla_delete.setItem(row, column, item)
        except:
            QMessageBox.critical(self, "Error", "El paciente no tiene placas actualmente.")
            
    def DeletePlaca(self):
        try:
            cedula = self.in_busqueda.text()
    
            if len(cedula) == 0:
                QMessageBox.critical(self, "Error", "Ingrese una cédula")
            else:
                Placa1 = None
                Placa2 = None
                Placa3 = None
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                cursor.execute("UPDATE Pacientes SET Placa1 = ?, Placa2 = ? , Placa3= ? WHERE Cedula = ?",
                        (Placa1, Placa2, Placa3 , cedula))
                conexion.commit()
                conexion.close()
        
        # Eliminación exitosa, muestra un mensaje y realiza otras acciones si es necesario
                QMessageBox.information(self, "Realizado", "Las placas ha sido eliminada correctamente")
                self.tabla_delete.clearContents()
                self.in_busqueda_3.clear()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al eliminar las placas  de la base de datos: " + str(e))
        pass
    
       
class historiaMenu(QMainWindow):
    def __init__(self ,id_user):
        super(historiaMenu, self).__init__()
        loadUi("interfaces/History.ui", self)
        self.id_user = id_user
        self.btn_buscar.clicked.connect(self.Searchdata)
        self.btn_agg.clicked.connect(self.AddPacient)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.btn_edit.clicked.connect(self.UpdateData)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_delete.clicked.connect(self.DeletaData)
        self.actionVolver_al_menu_principal.triggered.connect(self.back_menu)
        self.btn_agg_2.clicked.connect(self.addInformation)
        self.btn_clear_2.clicked.connect(self.clearData)
        self.btn_agg_3.clicked.connect(self.addDiagnostico)
        self.btn_edit_2.clicked.connect(self.addInformation)
        self.btn_edit_3.clicked.connect(self.addDiagnostico)
        self.btn_clear_3.clicked.connect(self.clearDiag)
        self.btn_clear_4.clicked.connect(self.clearTrata)
        self.fecha_hora_actualizadas = False
        self.tabWidget.currentChanged.connect(self.actualizar_fecha_hora_diagnostico)
        self.showMaximized()

        
        self.tratamientos = {
            "Triaje": ["Seleccione el tipo de honorario", "Consulta e Historia Clínica sin informe", "Consulta e Historia Clínica con informe"],
            "Periodoncia": ["Tartectomía y pulido simple (1 sesión)", "Tartectomía y pulido simple (2-3 sesiones)","Aplicación tópica de fluór","Cirguia periodontal (por cuadrante)"],
            "Blanqueamiento": ["Blanqueamiento intrapulpar", "Blanquemaineto maxilar superior e inferior (2 sesiones de 20 min c/u)"],
            "Operatoria": ["Obturaciones provisionales","Obturaciones con Amalgama","Obturaciones con vidrio ionomerico pequeña","Obturaciones con vidrio ionomerico grande","Obturaciones con resina fotocurada"],
            "Endodoncia": ["Pulpotomías formocreasoladas","Emergencias Endodontica","Tratamiento endodontico monoradicular","Tratamiento endodontico biradicular","Tratamiento endodontico multiradicular","Desobturación conductos"],
            "Radiografias Periaciales": ["Adultos e infantes"],
            "Cirugias": ["Exodoncia simple","Exodoncia quirurgica","Exodoncia de dientes temporales","Exodoncia de corales erupcionadas/incluidas"],
            "Protesis": ["Coronas provisionales por unidad","Muñon artificial monoradicular","Muñon artificial multiradicular","Incrustacion resina/metálica","Unidad de corona meta-porcelana","Cementado de protesis fija"],
            "Protesis removibles metalicas y/o acrilicas": ["1 a 3 unidades","4 a 6 unidades","7 a 12 unidades","Unidadad adicional","Ganchos contorneados retentativas acrilicas c/u","Reparaciones protesis acrilicas y/oo agregar un diente a la protesis"],
            "Protesis totales": ["Dentadura superior o inferior (incluye controles post-inatalción) c/u"],
            "Implantes dentales": ["Honorarios cirujano por implante","Implante y aditamientos","Injertos óseos (1cc)","PRF (incluye bionalista y extraccion de sangre + centrifugado)","Corona metal porcelana sobre implante","DPR acrilica"],
        }

        self.combo_honorario = [self.findChild(QtWidgets.QComboBox, f"c_{i}") for i in range(6)]
        self.combo_tratamiento = [self.findChild(QtWidgets.QComboBox, f"t_{i}") for i in range(6)]
        self.monto_dola = [self.findChild(QtWidgets.QLineEdit, f"monto_dola_{i+1}") for i in range(6)]
        self.monto_bs = [self.findChild(QtWidgets.QLineEdit, f"monto_bs_{i+1}") for i in range(6)]
        for combo in self.combo_honorario:
            combo.addItem("Seleccione el tipo de honorario")
            combo.addItems(list(self.tratamientos.keys()))
            combo.currentTextChanged.connect(self.loadTratamientos)

        for i, combo in enumerate(self.combo_tratamiento):
            combo.currentTextChanged.connect(lambda _, index=i: self.update_monto(index))
    
    def actualizar_fecha_hora_diagnostico(self):
        # Solo actualiza los campos de fecha y hora si no se han actualizado previamente
        if not self.fecha_hora_actualizadas:
            fecha_actual = QDate.currentDate()
            hora_actual = QTime.currentTime()

            self.fecha.setDate(fecha_actual)
            self.hora.setTime(hora_actual)

            # Marca que los campos se han actualizado
            self.fecha_hora_actualizadas = True

    def clearTrata(self):
        self.in_name_4.clear()
        self.in_apell_4.clear()
        self.monto_dola_1.clear()
        self.monto_bs_1.clear()
        self.monto_dola_2.clear()
        self.monto_bs_2.clear()
        self.monto_dola_3.clear()
        self.monto_bs_3.clear()
        self.monto_dola_4.clear()
        self.monto_bs_4.clear()
        self.monto_dola_5.clear()
        self.monto_bs_5.clear()
        self.monto_dola_6.clear()
        self.monto_bs_6.clear()
        self.totalBs.clear()
        self.totaldola.clear()
    def calcularDivisa(self, dolar):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        url = 'https://www.bcv.org.ve'
        response = requests.get(url , verify=False)

        soup = BeautifulSoup(response.text, 'html.parser')

        div_dolar = soup.find('div', id='dolar')

        divisa = div_dolar.find('strong').text

        # Eliminar espacios en blanco y comas
        divisa_limpia = divisa.replace(' ', '').replace(',', '.')

        # Convertir la cadena limpia en un número decimal
        valor_numerico = float(divisa_limpia)

        # Obtener la cantidad de dólares del QLineEdit en tu interfaz gráfica
        operacion = float(dolar)

        # Calcular la suma
        bolivares = operacion * valor_numerico
        suma_formateada = "{:.2f}".format(bolivares).replace(".", ",")

        # Retorna el valor calculado
        return suma_formateada, operacion

    def loadTratamientos(self):
        sender = self.sender()
        selected_honorario = sender.currentText()

        if selected_honorario == "Seleccione el tipo de honorario":
            return

        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()

        index = self.combo_honorario.index(sender)

        tratamientos_honorario = self.tratamientos.get(selected_honorario, [])
        linked_combo = self.combo_tratamiento[index]
        linked_combo.clear()

        for tratamiento in tratamientos_honorario:
            cursor.execute("SELECT monto FROM Trata WHERE tipo_tratamiento = ? AND tratamiento = ?", (selected_honorario, tratamiento))
            monto = cursor.fetchone()
            if monto:
                linked_combo.addItem(tratamiento)

    def update_monto(self, index):
        selected_honorario = self.combo_honorario[index].currentText()
        selected_tratamiento = self.combo_tratamiento[index].currentText()

        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()

        cursor.execute("SELECT monto FROM Trata WHERE tipo_tratamiento = ? AND tratamiento = ?", (selected_honorario, selected_tratamiento))
        monto = cursor.fetchone()

        if monto:
            self.monto_dola[index].setText(str(monto[0]))
           
            dolares = monto[0]
            resultado_divisa = self.calcularDivisa(dolares)
            if resultado_divisa:
                bolivares, operacion = resultado_divisa
                self.monto_bs[index].setText(str(bolivares))
                self.totalPrecio()
            else:
                # Manejar el caso en el que no se pueda obtener la información de la divisa
                self.monto_bs[index].setText("Error al obtener la tasa de cambio")
        else:
            # Manejar el caso en el que no se encuentre el monto en la base de datos
            self.monto_bs[index].setText("Monto no encontrado en la base de datos")

           
    def totalPrecio(self):
        # Calcula el total sumando los valores flotantes de los QLineEdits
        totalBs = 0.0
        totalUsd= 0.0

        # Asegúrate de manejar las conversiones a flotante correctamente y verifica que las cadenas no estén vacías
        if self.monto_bs_1.text():
            totalBs += float(self.monto_bs_1.text().replace(',', '.'))

        if self.monto_bs_2.text():
            totalBs += float(self.monto_bs_2.text().replace(',', '.'))

        if self.monto_bs_3.text():
            totalBs += float(self.monto_bs_3.text().replace(',', '.'))
        if self.monto_bs_4.text():
            totalBs += float(self.monto_bs_4.text().replace(',', '.'))
        if self.monto_bs_5.text():
            totalBs += float(self.monto_bs_5.text().replace(',', '.'))
        if self.monto_bs_6.text():
            totalBs += float(self.monto_bs_6.text().replace(',', '.'))

        if self.monto_dola_1.text():
            totalUsd += float(self.monto_dola_1.text().replace(',', '.'))

        if self.monto_dola_2.text():
            totalUsd += float(self.monto_dola_2.text().replace(',', '.'))

        if self.monto_dola_3.text():
            totalUsd += float(self.monto_dola_3.text().replace(',', '.'))
        if self.monto_dola_4.text():
            totalUsd += float(self.monto_dola_4.text().replace(',', '.'))
        if self.monto_dola_5.text():
            totalUsd += float(self.monto_dola_5.text().replace(',', '.'))
        if self.monto_dola_6.text():
            totalUsd += float(self.monto_dola_6.text().replace(',', '.'))

        # Formatea el número con dos decimales
        totalBs_formateado = f'{totalBs:.2f}'
        totalUsd_formateado = f'{totalUsd:.2f}'
    
        # Asigna el valor formateado al QLineEdit
        self.totalBs.setText(totalBs_formateado)
        self.totaldola.setText(totalUsd_formateado)
    
        
    def clearDiag(self):
        self.in_name_3.clear()
        self.in_apell_3.clear()
        self.hora.clear()
        self.fecha.clear()
        self.diag.clear()
        
    def addDiagnostico(self):
        cedula = self.in_busqueda.text()
        diag = self.diag.toPlainText()
        fecha = self.fecha.date()
        hora = self.hora.time()
        fechaToString = fecha.toString('yyyy-MM-dd')
        horatoString = hora.toString('hh:mm:ss')
        print (fechaToString)
        print (horatoString)
        if not cedula :
            QMessageBox.warning(self,"Error","Por favor ingrese la cedula en el menu de registro ")
            return
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
                        # Verificar si ya existe un paciente con la misma cédula
            cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
            cursor.execute("UPDATE Pacientes SET Diagnotico=?, Fecha_Diagnotico=?, Hora_Diagnostico=?  WHERE Cedula=?", (
                diag,fechaToString,horatoString, cedula ))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Informacion registrada correctamente.")

            # Cierra la conexión con la base de datos
            conexion.close()
    
        # Actualizar los registros en la base de datos
        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar el paciente: {str(error)}")
    def clearData(self):
        self.hiper_control.clear()
        self.diabetes_control.clear()
        self.coagualcion_control.clear()
        self.ln_data.clear()
        self.btn_si.setChecked(False)
        self.btn_si_4.setChecked(False)
        self.btn_no_4.setChecked(False)
        self.btn_si_3.setChecked(False)
        self.btn_no_3.setChecked(False)
        self.btn_no.setChecked(False)
        self.ln_alergias.clear()
        
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

    def addInformation(self):
        hipertenso = None
        diabetes = None
        coagulacion = None
        cedula = self.in_busqueda.text()
        hipertenso_control = self.hiper_control.toPlainText()
        diabetes_control = self.diabetes_control.toPlainText()
        coagualcion_control= self.coagualcion_control.toPlainText()
        if self.btn_si.isChecked():
            hipertenso = "Si"
        if self.btn_no.isChecked():
            hipertenso = "No"
        
        if self.btn_si_4.isChecked():
            diabetes = "Si"
        if self.btn_no_4.isChecked():
            diabetes = "No"
            
        if self.btn_si_3.isChecked():
            coagulacion = "Si"
        if self.btn_no_3.isChecked():
            coagulacion = "No"
        Otros = self.ln_data.toPlainText()
        alergias = self.ln_alergias.toPlainText()
        if not cedula :
            QMessageBox.warning(self,"Error","Por favor ingrese la cedula en el menu de registro ")
            return
        if not Otros:
            Otros = None
        if not alergias:
            alergias =None
            
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
            cursor.execute("UPDATE Pacientes SET Hipertension=?, Diabates=?, Coagualcion=?, Otros=? ,Alergias=? , diabate_Data=?,hipertension_Data=?,Coagualcion_Data=?  WHERE Cedula=?", (
                hipertenso, diabetes, coagulacion, Otros, alergias,diabetes_control,hipertenso_control,coagualcion_control, cedula ))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Informacion registrada correctamente.")

            # Cierra la conexión con la base de datos
            conexion.close()
    
        # Actualizar los registros en la base de datos
        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar el paciente: {str(error)}")

    def clearInputs(self):
        self.in_cedula.clear()
        self.in_name.clear()
        self.in_apell.clear()
        self.in_age.clear()
        self.in_mail.clear()
        self.in_number.clear()
        self.in_dir.clear()
        self.btn_m.setChecked(False)
        self.btn_f.setChecked(False)
        self.motivo.clear()
    def  AddPacient(self): 
        idUser = self.id_user
        cedula = self.in_cedula.text()
        nombre = self.in_name.text()
        apellido = self.in_apell.text()
        edad = self.in_age.text()
        mail = self.in_mail.text()
        valor_sexo = None
        if self.btn_m.isChecked():
            valor_sexo = "Masculino"
        if self.btn_f.isChecked():
            valor_sexo = "Femenino"
        telefono = self.in_number.text()
        direccion = self.in_dir.text()
        contexto = self.motivo.toPlainText()
        
        if valor_sexo is None:
            QMessageBox.critical(self,"Error","Por favor seleccione su sexo")
            return

        if not cedula or not nombre or not apellido or not edad or not valor_sexo or not mail  or not telefono or not direccion or not contexto:
            QMessageBox.critical(self, "Error", "Por favor, complete todos los campos.")
            return

        telefono_pattern = re.compile(r'^\d{11}$')  # Asume que el número de teléfono debe tener 10 dígitos
        mail_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')  # Patrón para validar correo electrónico
        cedula_pattern = re.compile(r'^\d+$')  # Asume que la cédula debe contener solo dígitos
        
        if not cedula_pattern.match(cedula):
            QMessageBox.warning(self, "Error", "Ingrese una cédula válida (solo números).")
            return
        if not telefono_pattern.match(telefono):
            QMessageBox.warning(self, "Error", "Ingrese un número de teléfono válido (0000-0000-000).")
            return

        if not mail_pattern.match(mail):
            QMessageBox.warning(self, "Error", "Ingrese una dirección de correo electrónico válida.")
            return
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            # Verificar si ya existe un paciente con la misma cédula
            cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
            existe_paciente = cursor.fetchone()[0]
            if existe_paciente:
                QMessageBox.warning(self, "Advertencia", "Ya existe un paciente con la misma cédula.")
                return
            else:
                cursor.execute("INSERT INTO Pacientes (Cedula, Nombre, Apellido, Edad, Sexo ,Direccion , ID_user ,Telefono, Mail ,Context) VALUES (?, ?, ?, ?, ?, ?, ? , ? ,? , ?)",
                            (cedula, nombre, apellido, edad, valor_sexo , direccion , idUser ,telefono , mail , contexto))

                # Confirmar los cambios en la base de datos
                conexion.commit()

                QMessageBox.information(self, "Éxito", "Paciente registrado correctamente.")

                # Cierra la conexión con la base de datos
                conexion.close()

        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar el paciente: {str(error)}")
               
           
    def Searchdata(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            idUser = self.id_user
            busqueda = self.in_busqueda.text()
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail, Context, Hipertension, Diabates, Coagualcion, Otros, Alergias, Diabate_Data, Hipertension_Data, Coagualcion_Data, Diagnotico, Fecha_Diagnotico, Hora_Diagnostico FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (busqueda, idUser))
            resultado = cursor.fetchone()

            if resultado:
                (Cedula, Nombre, Apellido, Edad, Direccion, Sexo, 
                    Telefono, Mail, Context ,Hipertension, Diabates, Coagualcion, Otros, Alergias, 
                    Diabate_Data , Hipertension_Data , Coagualcion_Data, Diagnotico, Fecha_Diagnotico, Hora_Diagnostico) = resultado

                self.in_cedula.setText(Cedula)
                self.in_name.setText(Nombre)
                self.in_apell.setText(Apellido)
                self.in_age.setText(Edad)  
                self.in_mail.setText(Mail)  # Correo
                self.in_dir.setText(Direccion)
                self.in_number.setText(Telefono)  # Prueba##
                self.motivo.setText(Context)
                self.hiper_control.setText(Hipertension_Data)
                self.diabetes_control.setText(Diabate_Data)
                self.coagualcion_control.setText(Coagualcion_Data)
                self.ln_data.setText(Otros)
                self.ln_alergias.setText(Alergias)
                self.in_name_3.setText(Nombre)
                self.in_apell_3.setText(Apellido)
                self.diag.setText(Diagnotico)
                self.in_name_4.setText(Nombre)
                self.in_apell_4.setText(Apellido)
                
                if Hipertension == "Si":
                    self.btn_si.setChecked(True)
                else:
                    self.btn_no.setChecked(True)
                if Diabates =="Si":
                    self.btn_si_4.setChecked(True)
                else:
                    self.btn_no_4.setChecked(True)
                if Coagualcion =="Si":
                    self.btn_si_3.setChecked(True)
                else:
                    self.btn_no_3.setChecked(True)

                # Manejar los botones de radio según el valor de Sexo
                if Sexo == "Masculino":
                    self.btn_m.setChecked(True)
                if Sexo == "Femenino":
                    self.btn_f.setChecked(True)

                # Obtener la fecha y hora de la base de datos
                if Fecha_Diagnotico is not None:
                    fecha_cita = QDate.fromString(Fecha_Diagnotico, 'yyyy-MM-dd')
                    self.fecha.setDate(fecha_cita)
                if Hora_Diagnostico is not None:
                    hora_cita = QTime.fromString(Hora_Diagnostico, 'hh:mm:ss')
                    self.hora.setTime(hora_cita)
                
                self.tabla_pacientes.clearContents()
                self.tabla_pacientes.setRowCount(1)
                self.tabla_pacientes.setColumnCount(8)
                data = [Cedula, Nombre, Apellido, Edad, Sexo, Direccion, Telefono, Mail]
                for column, value in enumerate(data):
                    item = QTableWidgetItem(value)
                    self.tabla_pacientes.setItem(0, column, item)
            else:
                # Limpiar la tabla existente si no se encuentra ningún registro
                self.tabla_pacientes.clearContents()
                QMessageBox.warning(self, "Advertencia", "No se ha encontrado ningún registro")

            conexion.close()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))

    def UpdateData(self):
        busqueda = self.in_busqueda.text()
        if not busqueda :
            QMessageBox.warning(self,"Error","Introduzca su cedula")
            return
        try:
            cedula = self.in_cedula.text()
            nombre = self.in_name.text()
            apellido = self.in_apell.text()
            edad = self.in_age.text()
            direccion = self.in_dir.text()
            telefono = self.in_number.text()
            mail = self.in_mail.text()
            valor_sexo = None
            if self.btn_m.isChecked():
                valor_sexo = "Masculino"
            if self.btn_f.isChecked():
                valor_sexo = "Femenino"
            context = self.motivo.toPlainText()


            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
    
        # Actualizar los registros en la base de datos
            cursor.execute("UPDATE Pacientes SET Nombre=?, Apellido=?, Edad=?, Direccion=?, Sexo=? ,Telefono=? ,Mail =? , Context=? WHERE Cedula=?", (nombre, apellido, edad, direccion, valor_sexo, telefono ,mail,  context, cedula))
            conexion.commit()
            
            QMessageBox.information(self, "Información", "Los datos se actualizaron correctamente")
           
            conexion.close()
            self.Searchdata()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))
    def searchDataForDelete(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            idUser = self.id_user
            cedula = self.in_busqueda_delete.text()
            # Ejecuta una consulta para obtener los datos de los pacientes
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion , Sexo  FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (cedula , idUser) )
            
           
            tabla_pacientes = cursor.fetchall()
            conexion.close()

            # Limpiar la tabla existente si es necesario
            self.tabla_pacientes.clearContents()

            # Establecer el número de filas y columnas en la tabla
            self.tabla_pacientes.setRowCount(len(tabla_pacientes))
            self.tabla_pacientes.setColumnCount(len(tabla_pacientes[0]))

            # Agregar los datos a la tabla
            for row, paciente in enumerate(tabla_pacientes):
                for column, value in enumerate(paciente):
                    item = QTableWidgetItem(str(value))
                    self.tabla_pacientes.setItem(row, column, item)
        except:
             QMessageBox.critical(self, "Error", "No hay ningún paciente con esa cedula.")
    def DeletaData(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea eliminar al paciente del sistema?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            try:
                cedula = self.in_busqueda.text()
        
                if len(cedula) == 0:
                    QMessageBox.critical(self, "Error", "Ingrese una cédula")
                else:
                    conexion = sqlite3.connect('interfaces/database.db')
                    cursor = conexion.cursor()
                    cursor.execute("DELETE FROM Pacientes WHERE Cedula = ?", (cedula,))
                    conexion.commit()
                    conexion.close()
            
            # Eliminación exitosa, muestra un mensaje y realiza otras acciones si es necesario
                    QMessageBox.information(self, "Realizado", "Los datos han sido eliminados correctamente")
                    self.clearInputs()
                    self.clearData()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", "Error al eliminar los datos de la base de datos: " + str(e))
        
        
        
    def back_menu(self):
        
        conexion = sqlite3.connect('interfaces/database.db')
        cursor= conexion.cursor()
        cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
        resultado = cursor.fetchone()
        if resultado :
            nombre_usuario = resultado[0]
            horaActual = datetime.datetime.now().time()
            
            if datetime.time(5, 0, 0) <= horaActual < datetime.time(12, 0, 0):
                textForMenu = f"Buenos días {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(12, 0, 0) <= horaActual < datetime.time(18, 0, 0):
                textForMenu = f"Buenas tardes {nombre_usuario}\n¿Qué deseas hacer hoy?"
            elif datetime.time(18, 0, 0) <= horaActual or horaActual < datetime.time(5, 0, 0):
                textForMenu = f"Buenas noches {nombre_usuario}\n¿Qué deseas hacer hoy?"
            else:
                textForMenu = f"Hola {nombre_usuario}\n¿Qué deseas hacer hoy?"
            menu_principal = MenuPrincipal(self.id_user)
            menu_principal.lb_nombre.setText(textForMenu)

            # Establecer la ventana en modo de pantalla completa
            menu_principal.showMaximized()

            menu_principal.setWindowTitle("Menu Principal")

            # Asegúrate de añadir la ventana al widget después de establecerla en modo de pantalla completa
            widget.addWidget(menu_principal)
            widget.setCurrentIndex(widget.currentIndex() + 1)

            self.close()
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Clinica")  # Establecer el nombre de la aplicación

    ingreso_usuario = IngresoUsuario()
    ingreso_usuario.showFullScreen()  # Muestra la ventana en pantalla completa

    widget = QStackedWidget()
    widget.addWidget(ingreso_usuario)
    widget.setGeometry(ingreso_usuario.geometry())
    widget.show()
    icon = QIcon("./interfaces/ELEMENTOS GRAFICOS/odontology-outline.png")
    ingreso_usuario.setWindowIcon(icon)
    sys.exit(app.exec_())