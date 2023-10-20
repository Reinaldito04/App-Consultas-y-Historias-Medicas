import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
import hashlib
import sqlite3
import os
import datetime
from bs4 import BeautifulSoup
import requests
from PyQt5.QtCore import Qt
class IngresoUsuario(QMainWindow):
    def __init__(self):
        super(IngresoUsuario , self). __init__()
        loadUi("./interfaces/loggin.ui", self)
        self.btn_login.clicked.connect(self.ingreso)
        self.btn_adduser.clicked.connect(self.ingresoRegistro)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        

        
    def ingresoRegistro(self):
        registro = Registro()
        widget.addWidget(registro)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(578)
        widget.setFixedWidth(879)

    def cifrar_contrasenia(self, contrasenia):
        # Cifrar la contraseña usando un algoritmo de hash (SHA-256 en este caso)
        cifrado = hashlib.sha256()
        cifrado.update(contrasenia.encode('utf-8'))
        return cifrado.hexdigest()
    
    def MenuPrincipalacceso(self):
        MenuPrincipal = MenuPrincipal()
        widget.addWidget(MenuPrincipal)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000)   
    def ingreso(self):
        nombre = self.txt_username.text()
        password = self.txt_password.text()

        if not  nombre or not password:
            QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña.")
            return
        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Users WHERE Username = ?", (nombre,))
        usuario = cursor.fetchone()

        if usuario:
            contrasenia_cifrada_ingresada = self.cifrar_contrasenia(password)
            contrasenia_cifrada_almacenada = usuario[1]  # Suponiendo que el hash se almacena en el segundo campo de la tabla
            if contrasenia_cifrada_ingresada == contrasenia_cifrada_almacenada:         
                horaActual = datetime.datetime.now().time()
            
                if datetime.time(5, 0, 0) <= horaActual < datetime.time(12, 0, 0):
                    textForMenu = f"Buenos días {nombre}\n¿Qué deseas hacer hoy?"
                elif datetime.time(12, 0, 0) <= horaActual < datetime.time(18, 0, 0):
                    textForMenu = f"Buenas tardes {nombre}\n¿Qué deseas hacer hoy?"
                elif datetime.time(18, 0, 0) <= horaActual or horaActual < datetime.time(5, 0, 0):
                    textForMenu = f"Buenas noches {nombre}\n¿Qué deseas hacer hoy?"
                else:
                    textForMenu = f"Hola {nombre}\n¿Qué deseas hacer hoy?"
                    
               
                id_user = usuario[2]
                menu_principal = MenuPrincipal(id_user)
                menu_principal.lb_nombre.setText(textForMenu)
                self.close()
                menu_principal.show()
                print("Inicio de sesión exitoso.")
                
            
            else:
          
                 QMessageBox.warning(self, "Error", "Contraseña Incorrecta.")
        else:
             QMessageBox.warning(self, "Error", "Nombre de usuario no encontrado.")
    
        conexion.close()
    
   
class Registro(QMainWindow):
    def __init__(self):
        super(Registro, self).__init__()
        loadUi("interfaces\dogtores.ui", self)
        self.btn_agg.clicked.connect(self.registrarUsuario)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.actionLogin.triggered.connect(self.ingresoLogin)
        self.actionSalir.triggered.connect(self.close)
        self.bt_photo.clicked.connect(self.addPhoto)
        
    
    def addPhoto(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, "Seleccionar imágenes", "", "Archivos de imagen (*.png *.jpg *.bmp)")
        
        if len(filenames) >= 1:
            pixmap1 = QPixmap(filenames[0])
            self.foto.setPixmap(pixmap1)
            
        else:
            QMessageBox.information(self,"Imagenes","Por favor,Selecciona una imagen")      
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
        return resultado > 0
    
    def ingresoLogin(self):
        self.hide()
        IngresoUsuario.show()
        
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
        conexion = sqlite3.connect('interfaces\database.db')
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
        
            if len(password) < 6:
                QMessageBox.critical(self, "Error", "La contraseña debe tener minimo 6 caracteres.")
                return
            if len(passwordRepeat) < 6:
                QMessageBox.critical(self, "Error", "La contraseña debe minimo tener 6 caracteres.")
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
       QApplication.quit()
        

class MenuPrincipal(QMainWindow):
    def __init__(self , id_user):
        super(MenuPrincipal , self). __init__()
        loadUi("./interfaces/menu.ui", self)
        self.frame_opciones.hide()
        self.id_user  = id_user
        self.bt_info.clicked.connect(self.informacionView)
        self.bt_menu.clicked.connect(self.toggle_sidebar)
        self.bt_salir.clicked.connect(self.close)
        self.bt_home.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_home) )
        self.bt_registro.clicked.connect(self.Historyviews)
        self.bt_paciente.clicked.connect(self.PlacasView )
        self.bt_citas.clicked.connect(self.CitasView)
        self.bt_historial.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_historial) )
    
    def PlacasView(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Deseas ir al formulario de placas?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply ==QMessageBox.Yes:
            placa_view = placasMenu(self.id_user) 
            widget.addWidget(placa_view)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.setFixedHeight(700)
            widget.setFixedWidth(900)
            self.hide()
            
            
    def CitasView(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Deseas ir al formulario de citas?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply ==QMessageBox.Yes:
            CitasView = CitasMenu(self.id_user)
           
            widget.addWidget(CitasView)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.setFixedHeight(700)
            widget.setFixedWidth(1100)
            self.hide()
    def informacionView(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Deseas ir al formulario de cambiar data?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply ==QMessageBox.Yes:
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
            widget.setFixedHeight(620)
            widget.setFixedWidth(800)
            self.hide()
        
        
         
    def Historyviews(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Desea ir al formulario de registro de pacientes?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply == QMessageBox.Yes:
            histori = historiaMenu(self.id_user)
            widget.addWidget(histori)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.setFixedHeight(700)
            widget.setFixedWidth(1050)
            histori.show()
            self.hide()
            # widget.addWidget(histori)
            # widget.setCurrentIndex(widget.currentIndex()+1)
            # widget.setFixedHeight(620)
            # widget.setFixedWidth(800)
            # self.hide()+
         

        

        
    def toggle_sidebar(self):
        if self.frame_opciones.isHidden():
            self.frame_opciones.show()
        else:
            self.frame_opciones.hide()
   
    def close(self):
       QApplication.quit()
       
class EditDoctor(QMainWindow):
    def __init__(self,id_user):
        super(EditDoctor, self).__init__()
        self.id_user = id_user
        loadUi("interfaces\edicion.ui", self)
        self.btn_passwordChange.clicked.connect(self.PasswordView)
        self.bt_delete.clicked.connect(self.eliminarInfo)
        self.btn_save.clicked.connect(self.modifyInfo)
        self.btn_back.clicked.connect(self.backMenu)
     
    def backMenu(self):   
        menu_principal = MenuPrincipal(self.id_user)
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
            menu_principal.lb_nombre.setText(textForMenu)
            menu_principal.show()
            self.hide()
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
        widget.setFixedHeight(500)
        widget.setFixedWidth(500)
        self.hide()
        
        # reply = QMessageBox.question(
        #     self,
        #     'Confirmación',
        #     '¿Deseas eliminar toda tu informacion?\n (Pacientes y datos de acceso)',
        #     QMessageBox.Yes | QMessageBox.No,
        #     QMessageBox.Yes
        # )
        # if reply == QMessageBox.Yes:
        #     conexion = sqlite3.connect('interfaces/database.db')
        #     cursor = conexion.cursor()
        #     cursor.execute('BEGIN TRANSACTION;')
        #     cursor.execute("DELETE FROM Users WHERE ID =?",(self.id_user,))
        #     cursor.execute('DELETE FROM Pacientes WHERE ID_user = ?', (self.id_user,))
        #     conexion.commit()
        #     QMessageBox.information(self,"Finalizado","Tus datos han sido borrados exitosamente")
        #     conexion.close()
        #     registro = Registro()
        #     widget.addWidget(registro)
        #     widget.setCurrentIndex(widget.currentIndex()+1)
        #     widget.setFixedHeight(578)
        #     widget.setFixedWidth(879)
     
            
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
            widget.setFixedHeight(700)
            widget.setFixedWidth(1100)
            self.hide()
            
class DeleteAllData(QMainWindow):
    def __init__(self,id_user):
        super(DeleteAllData , self).__init__()
        self.id_user = id_user
        loadUi("interfaces\eliminarData.ui", self)
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
                        widget.setFixedHeight(578)
                        widget.setFixedWidth(879) 
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
            widget.setFixedHeight(620)
            widget.setFixedWidth(800)
            self.hide()
        
class CitasMenu(QMainWindow):
    def __init__(self,id_user):
        super(CitasMenu, self).__init__()
        self.id_user = id_user
        loadUi("interfaces\citas(nuevo).ui", self)
        self.actionVolver_al_menu_principal.triggered.connect(self.back)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_buscar.clicked.connect(self.searchdata)
        self.btn_agg.clicked.connect(self.aggCite)
        self.btn_clear.clicked.connect(self.clear)
        self.btn_edit.clicked.connect(self.editarCita)
        self.btn_delete.clicked.connect(self.eliminarCita)
    def eliminarCita(self):
        try:
            cedula = self.in_busqueda.text()
    
            if len(cedula) == 0:
                QMessageBox.critical(self, "Error", "Ingrese una cédula")
            else:
                citaNull = None
                horaNull = None
                conexion = sqlite3.connect('interfaces/database.db')
                cursor = conexion.cursor()
                cursor.execute("UPDATE Pacientes SET Fecha_Cita = ?, Hora_Cita = ? WHERE Cedula = ?",
                        (citaNull, horaNull, cedula))
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
            
        hora = self.hora.time()
        horaToString = hora.toString('hh:mmm:ss')
        
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            
            # Verificar si existe un paciente con la cédula proporcionada
            cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
            existe_paciente = cursor.fetchone()[0] > 0
            
            if existe_paciente:
                # Si el paciente existe, proceder a actualizar la cita
                cursor.execute("UPDATE Pacientes SET Fecha_Cita = ?, Hora_Cita = ? WHERE Cedula = ?",
                            (fechaToString, horaToString, cedula))
                
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
        idUser = self.id_user
        cedula = self.in_busqueda.text()
        
        fecha = self.fecha.selectedDate()
        fechaToString = fecha.toString('yyyy-MM-dd')
            
        hora = self.hora.time()
        horaToString = hora.toString('hh:mmm:ss')
        nombre = self.txt_name.text()
        apellido = self.txt_apell.text()
        if len(nombre) <= 0:
            QMessageBox.warning(self,"error","Ingrese el nombre del paciente ")
            return
        if len(apellido) <= 0:
            QMessageBox.warning(self,"error","Ingrese el apellido del paciente ")
            return
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            
            # Verificar si existe un paciente con la cédula proporcionada
            cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
            existe_paciente = cursor.fetchone()[0] > 0
            
            if existe_paciente:
                # Si el paciente existe, proceder a actualizar la cita
                cursor.execute("UPDATE Pacientes SET Fecha_Cita = ?, Hora_Cita = ? WHERE Cedula = ?",
                            (fechaToString, horaToString, cedula))
                
                # Guardar los cambios en la base de datos
                conexion.commit()
                
                # Mostrar un mensaje de éxito
                QMessageBox.information(self, "Información", "Cita guardada con éxito.")
            else:
                # Si el paciente no existe, mostrar un mensaje de error
                QMessageBox.warning(self, "Advertencia", "No se encontró un paciente con la cédula proporcionada.")
            
            # Cerrar la conexión con la base de datos
            conexion.close()
            
        except sqlite3.Error as error:
            # En caso de error, mostrar un mensaje de error
            QMessageBox.critical(self, "Error", f"Error al guardar la cita: {str(error)}")    
    def searchdata(self):
        idUser = self.id_user
        cedula = self.in_busqueda.text()
        
        if len(cedula) <= 0:
            QMessageBox.warning(self, "Error", "Ingrese una cedula")
            return  # Salir de la función si no hay cédula

        try:
            conexion = sqlite3.connect('interfaces\database.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT Cedula,Nombre, Apellido, Fecha_Cita, Hora_Cita  FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (cedula, idUser))
            tabla_cita = cursor.fetchall()

            # Filtrar los resultados para eliminar las filas con None
            resultados_filtrados = [resultado for resultado in tabla_cita if None not in resultado]

            if resultados_filtrados:
                # Limpiar la tabla existente si es necesario
                self.tableWidget.clearContents()

                # Establecer el número de filas y columnas en la tabla
                self.tableWidget.setRowCount(len(resultados_filtrados))
                self.tableWidget.setColumnCount(len(resultados_filtrados[0]))

                # Agregar los datos a la tabla
                for row, paciente in enumerate(resultados_filtrados):
                    for column, value in enumerate(paciente):
                        item = QTableWidgetItem(str(value))
                        self.tableWidget.setItem(row, column, item)

                # Mostrar el primer resultado en los campos de texto
                primer_resultado = resultados_filtrados[0]
                nombre_paciente, apellido_paciente, fechaCita, horaCita, cedula = primer_resultado
                self.txt_name.setText(nombre_paciente)
                self.txt_apell.setText(apellido_paciente)
                fecha_cita = fechaCita
                print("Hora obtenida de la base de datos:", horaCita)
                self.fecha.setSelectedDate(QDate.fromString(fecha_cita, 'yyyy-MM-dd'))
                hora_cita = QTime.fromString(horaCita, 'hh:mm:ss')
                self.hora.setTime(hora_cita)
            else:
                # Manejar el caso en el que no se encontraron resultados, por ejemplo, mostrar un mensaje de error
                QMessageBox.warning(self, "Sin resultados", "El paciente no tiene citas actualmente")

                # Si deseas mostrar el nombre en pantalla, puedes hacerlo aquí
                self.txt_name.clear()  # Limpiar el campo de nombre
                self.txt_apell.clear()  # Limpiar el campo de apellido
        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al buscar paciente: {str(error)}")
        finally:
            conexion.close()



    def back(self):
        menu_principal = MenuPrincipal(self.id_user)
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
            menu_principal.lb_nombre.setText(textForMenu)
            menu_principal.show()
            self.hide()
    def salir(self):
        QApplication.quit()
#         self.btn_citas.clicked.connect(self.mostrarCitas)
#         self.btn_agg_cita.clicked.connect(self.mostrarFormularioAgendarCita)
#         self.btn_borrar.clicked.connect(self.mostrarFormularioEliminarCita)
#         self.btn_back.clicked.connect(self.volverAlMenu)
#         self.btn_refresh.clicked.connect(self.buscarCitas)
#         self.btn_buscar_2.clicked.connect(self.buscarPacienteParaCita)
#         self.btn_edit.clicked.connect(self.editarCita)
#         self.btn_agg.clicked.connect(self.agendarCita)
#         self.btn_buscar_3.clicked.connect(self.buscarCitaParaEliminar)
#         self.btn_delete.clicked.connect(self.eliminarCita)

#     def mostrarCitas(self):
#         self.stackedWidget.setCurrentWidget(self.tabla_citas)
        
#  # Función para mostrar el formulario de agendar cita
#     def mostrarFormularioAgendarCita(self):
#         self.stackedWidget.setCurrentWidget(self.agg_cita)

#     # Función para mostrar el formulario de eliminar cita
#     def mostrarFormularioEliminarCita(self):
#         self.stackedWidget.setCurrentWidget(self.delete_cita)

#     # Función para volver al menú principal
#     def volverAlMenu(self):
#         print("Volviendo al menú principal")
#         menu_principal = MenuPrincipal(self.id_user)
#         conexion =sqlite3.connect('interfaces/database.db')
#         cursor= conexion.cursor()
#         cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
#         resultado= cursor.fetchone()
#         if resultado :
#             nombre_usuario= resultado[0]
#             horaActual = datetime.datetime.now().time()
            
#             if (horaActual >= datetime.time(5, 0, 0)) and (horaActual <= datetime.time(12, 0, 0)):
                   
#                 textForMenu = f"Buenos dias {nombre_usuario} \n¿Que deseas hacer hoy?"
    
#             if (horaActual >= datetime.time(12, 0, 0)) and (horaActual <= datetime.time(18, 0, 0)):
                   
#                 textForMenu = f"Buenas tardes {nombre_usuario} \n¿Que deseas hacer hoy?"
                   
#             if (horaActual >= datetime.time(18, 0, 0)) and (horaActual <= datetime.time(5, 0, 0)):
                   
#                 textForMenu = f"Buenas noches {nombre_usuario} \n¿Que deseas hacer hoy?"
#             else :
#                     textForMenu = f"Hola {nombre_usuario} \n¿Que deseas hacer hoy?"
#             menu_principal.lb_nombre.setText(textForMenu)
#             menu_principal.show()
#             self.hide()
#         pass
#  # Función para buscar citas
#     def buscarCitas(self):
#         try:
#             conexion = sqlite3.connect('interfaces/database.db')
#             cursor = conexion.cursor()
#             idUser = self.id_user

#             # Ejecuta una consulta para obtener los datos de los pacientes y ordenar por Fecha_Cita descendente
#             cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Fecha_Cita, Hora_Cita FROM Pacientes WHERE ID_user = ? ORDER BY Fecha_Cita ASC, Hora_Cita ASC ", (idUser,))
#             tabla_cita = cursor.fetchall()
#             conexion.close()

#             # Filtrar las filas que no contengan ningún valor 'None'
#             filas_filtradas = [paciente for paciente in tabla_cita if None not in paciente]

#             # Limpiar la tabla existente si es necesario
#             self.tabla_cita.clearContents()

#             # Establecer el número de filas y columnas en la tabla
#             self.tabla_cita.setRowCount(len(filas_filtradas))
#             self.tabla_cita.setColumnCount(len(filas_filtradas[0]))

#             # Agregar los datos a la tabla
#             for row, paciente in enumerate(filas_filtradas):
#                 for column, value in enumerate(paciente):
#                     item = QTableWidgetItem(str(value))
#                     self.tabla_cita.setItem(row, column, item)
#         except:
#             QMessageBox.critical(self, "Error", "No hay citas actualmente.")

#     # Función para buscar paciente para asignar cita
#     def buscarPacienteParaCita(self):
#         idUser = self.id_user
#         cedula =self.in_busqueda_2.text()
#         if len(cedula) <=0:
#             QMessageBox.warning(self,"Error","Ingrese una cedula")
#         else:
#             name = self.in_name.text()
#             apellido = self.in_apell.text()
#             try:
#                 conexion = sqlite3.connect('interfaces\database.db')
#                 cursor = conexion.cursor()
#                 cursor.execute("SELECT Nombre , Apellido FROM Pacientes WHERE Cedula = ? AND ID_user = ?",(cedula, idUser))
#                 resultado = cursor.fetchone()
#                 conexion.close()
#                 if resultado :
#                     nombre_paciente ,apellido_paciente = resultado
#                     self.in_name.setText(nombre_paciente)
#                     self.in_apell.setText(apellido_paciente)
#                 else:
#                     QMessageBox.critical(self,"Error","El paciente no fue encontrado")
#             except sqlite3.Error as error:
#                 QMessageBox.critical(self, "Error", f"Error al buscar paciente: {str(error)}")

#     # Función para editar una cita
#     def editarCita(self):
#         idUser = self.id_user
#         cedula = self.in_busqueda_2.text()
        
#         fecha = self.fecha.selectedDate()
#         fechaToString = fecha.toString('yyyy-MM-dd')
            
#         hora = self.hora.time()
#         horaToString = hora.toString('hh:mmm:ss')
        
#         try:
#             conexion = sqlite3.connect('interfaces/database.db')
#             cursor = conexion.cursor()
            
#             # Verificar si existe un paciente con la cédula proporcionada
#             cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
#             existe_paciente = cursor.fetchone()[0] > 0
            
#             if existe_paciente:
#                 # Si el paciente existe, proceder a actualizar la cita
#                 cursor.execute("UPDATE Pacientes SET Fecha_Cita = ?, Hora_Cita = ? WHERE Cedula = ?",
#                             (fechaToString, horaToString, cedula))
                
#                 # Guardar los cambios en la base de datos
#                 conexion.commit()
                
#                 # Mostrar un mensaje de éxito
#                 QMessageBox.information(self, "Información", "Cita actualizada con éxito.")
#             else:
#                 # Si el paciente no existe, mostrar un mensaje de error
#                 QMessageBox.warning(self, "Advertencia", "No se encontró un paciente con la cédula proporcionada.")
            
#             # Cerrar la conexión con la base de datos
#             conexion.close()
            
#         except sqlite3.Error as error:
#             # En caso de error, mostrar un mensaje de error
#             QMessageBox.critical(self, "Error", f"Error al actualizar la cita: {str(error)}")

#     # Función para agendar una cita
#     def agendarCita(self):
#         idUser = self.id_user
#         cedula = self.in_busqueda_2.text()
        
#         fecha = self.fecha.selectedDate()
#         fechaToString = fecha.toString('yyyy-MM-dd')
            
#         hora = self.hora.time()
#         horaToString = hora.toString('hh:mmm:ss')
        
#         try:
#             conexion = sqlite3.connect('interfaces/database.db')
#             cursor = conexion.cursor()
            
#             # Verificar si existe un paciente con la cédula proporcionada
#             cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
#             existe_paciente = cursor.fetchone()[0] > 0
            
#             if existe_paciente:
#                 # Si el paciente existe, proceder a actualizar la cita
#                 cursor.execute("UPDATE Pacientes SET Fecha_Cita = ?, Hora_Cita = ? WHERE Cedula = ?",
#                             (fechaToString, horaToString, cedula))
                
#                 # Guardar los cambios en la base de datos
#                 conexion.commit()
                
#                 # Mostrar un mensaje de éxito
#                 QMessageBox.information(self, "Información", "Cita guardada con éxito.")
#             else:
#                 # Si el paciente no existe, mostrar un mensaje de error
#                 QMessageBox.warning(self, "Advertencia", "No se encontró un paciente con la cédula proporcionada.")
            
#             # Cerrar la conexión con la base de datos
#             conexion.close()
            
#         except sqlite3.Error as error:
#             # En caso de error, mostrar un mensaje de error
#             QMessageBox.critical(self, "Error", f"Error al guardar la cita: {str(error)}")
        
        

    # # Función para buscar una cita para eliminar
    # def buscarCitaParaEliminar(self):
    #     try:
    #         conexion = sqlite3.connect('interfaces/database.db')
    #         cursor = conexion.cursor()
    #         idUser = self.id_user
    #         cedula = self.in_busqueda_3.text()
    #         # Ejecuta una consulta para obtener los datos de los pacientes
    #         cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion , Sexo, Fecha_Cita, Hora_Cita  FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (cedula , idUser) )
            
           
    #         tabla_citas_delete = cursor.fetchall()
    #         conexion.close()

    #         # Limpiar la tabla existente si es necesario
    #         self.tabla_citas_delete.clearContents()

    #         # Establecer el número de filas y columnas en la tabla
    #         self.tabla_citas_delete.setRowCount(len(tabla_citas_delete))
    #         self.tabla_citas_delete.setColumnCount(len(tabla_citas_delete[0]))

    #         # Agregar los datos a la tabla
    #         for row, paciente in enumerate(tabla_citas_delete):
    #             for column, value in enumerate(paciente):
    #                 item = QTableWidgetItem(str(value))
    #                 self.tabla_citas_delete.setItem(row, column, item)
    #     except:
    #         QMessageBox.critical(self, "Error", "No hay ningún paciente con esa cedula.")

    # # Función para eliminar una cita
    # def eliminarCita(self):
    #     try:
    #         cedula = self.in_busqueda_3.text()
    
    #         if len(cedula) == 0:
    #             QMessageBox.critical(self, "Error", "Ingrese una cédula")
    #         else:
    #             citaNull = None
    #             horaNull = None
    #             conexion = sqlite3.connect('interfaces/database.db')
    #             cursor = conexion.cursor()
    #             cursor.execute("UPDATE Pacientes SET Fecha_Cita = ?, Hora_Cita = ? WHERE Cedula = ?",
    #                     (citaNull, horaNull, cedula))
    #             conexion.commit()
    #             conexion.close()
        
    #     # Eliminación exitosa, muestra un mensaje y realiza otras acciones si es necesario
    #             QMessageBox.information(self, "Realizado", "La cita ha sido eliminada correctamente")
    #             self.tabla_citas_delete.clearContents()
    #             self.in_busqueda_3.clear()
    #     except sqlite3.Error as e:
    #         QMessageBox.critical(self, "Error", "Error al eliminar la cita  de la base de datos: " + str(e))
    #     pass

        
class PasswordMenu(QMainWindow):
    def __init__(self,id_user ):
        super(PasswordMenu, self).__init__()
        self.id_user = id_user
        loadUi("interfaces\password.ui", self)
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
            widget.setFixedHeight(620)
            widget.setFixedWidth(800)
            self.hide()
        
 
class placasMenu(QMainWindow):
    def __init__(self , id_user):
        super(placasMenu , self).__init__()
        loadUi("interfaces\placas.ui", self)       
        self.id_user = id_user
        self.btn_bdd.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_bdd))
        self.btn_page_import.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_import))
        self.btn_page_view.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_view))
        self.btn_page_delete.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_delete))
        self.btn_back.clicked.connect(self.backMenu)
        self.btn_import.clicked.connect(self.addPhotos)
        self.btn_guardar.clicked.connect(self.AddData)
        self.btn_buscar.clicked.connect(self.searchData)
        
        self.btn_buscar_2.clicked.connect(self.buscarDatos)
        self.btn_buscar_4.clicked.connect(self.searchAll)
        self.btn_buscar_3.clicked.connect(self.searchForDelete)
        self.btn_delete.clicked.connect(self.DeletePlaca)
    
    def DeletePlaca(self):
        try:
            cedula = self.in_busqueda_3.text()
    
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

    def buscarDatos(self):
        cedula = self.in_busqueda_2.text()
        idUser = self.id_user
        if len(cedula)<= 0:
         QMessageBox.warning(self,"Advertencia","Ingrese una Cédula")
        else:
            try:
                conexion = sqlite3.connect('interfaces\database.db')
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
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))
    def AddData(self):
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
                conexion = sqlite3.connect('interfaces\database.db')
                cursor = conexion.cursor()
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
                conexion = sqlite3.connect('interfaces\database.db')
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
    def addPhotos(self):
        filenames, _ = QFileDialog.getOpenFileNames(self, "Seleccionar imágenes", "", "Archivos de imagen (*.png *.jpg *.bmp *.jpeg *.JFIF)")
        
        if len(filenames) >= 3:
            pixmap1 = QPixmap(filenames[0])
            pixmap2 = QPixmap(filenames[1])
            pixmap3 = QPixmap(filenames[2])
            
            self.img1.setPixmap(pixmap1)
            self.img2.setPixmap(pixmap2)
            self.img3.setPixmap(pixmap3)
        else:
            QMessageBox.information(self,"Imagenes","Por favor, seleccione al menos tres imágenes.")
    def backMenu(self):
        menu_principal = MenuPrincipal(self.id_user)
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
            menu_principal.lb_nombre.setText(textForMenu)
            menu_principal.show()
            self.hide()
        
        
        
       
class historiaMenu(QMainWindow):
    def __init__(self ,id_user):
        super(historiaMenu, self).__init__()
        loadUi("interfaces\History.ui", self)
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
        
        
        self.t0 = self.findChild(QtWidgets.QComboBox, "t0")
        self.t0.addItem("Seleccione el tipo de honorario")
        self.t0.addItems(["Triaje", "Periodoncia", "Blanqueamiento", "Operatoria", "Endodoncia", "Radiografias Periaciales", "Cirugias", "Protesis", "Protesis removibles metalicas y/o acrilicas", "Protesis totales", "Implantes dentales"])
        self.t0.currentIndexChanged.connect(self.actualizar_cb_tratamiento)

        self.t1 = self.findChild(QtWidgets.QComboBox, "t1")
        self.t2 = self.findChild(QtWidgets.QComboBox, "t2")
        self.t3 = self.findChild(QtWidgets.QComboBox, "t3")
        self.t1.currentIndexChanged.connect(self.actualizar_costo_t1)
        self.t2.currentIndexChanged.connect(self.actualizar_costo_t2)
        self.t3.currentIndexChanged.connect(self.actualizar_costo_t3)
        
        
        # Define el diccionario de tratamientos
        self.tratamientos = {
            "Triaje": ["Consulta e Historia Clinica sin informe", "Consulta e Historia Clinica con informe"],
            "Periodoncia": ["Tartectomia y pulido simple (1 sesión)", "Tartectomia y pulido simple (2-3 sesiones)","Aplicación tópica de fluór","Cirguia periodontal (por cuadrante)"],
            "Blanqueamiento": ["Blanqueamiento intrapulpar", "Blanquemaineto maxilar superior e inferioir (2 sesiones de 20 min c/u)"],
            "Operatoria": ["Obturaciones provisionales","Obturaciones con Amalgama","Obturaciones con vidrio ionomerico pequeña","Obturaciones con vidrio ionomerico grande","Obturaciones con resina fotocurada"],
            "Endodoncia": ["Pulpotomías formocreasoladas","Emergencias Endodontica","Tratamiento endodontico monoradicular","Tratamiento endodontico biradicular","Tratamiento endodontico multiradicular","Desobturación conductos"],
            "Radiografias Periaciales": ["Adultos e infantes"],
            "Cirugias": ["Exodoncia simple","Exodoncia quirurgica","Exodoncia de dientes temporales","Exodoncia de corales erupcionadas/incluidas"],
            "Protesis": ["Coronas provisionales por unidad","Muñon artificial monoradicular","Muñon artificial multiradicular","Incrustacion resina/metálica","Unidad de corona meta-porcelana","Cementado de protesis fija"],
            "Protesis removibles metalicas y/o acrilicas": ["1 a 3 unidades","4 a 6 unidades","7 a 12 unidades","Unidadad adicional","Ganchos contorneados retentativas acrilicas c/u","Reparaciones protesis acrilicas y/oo agregar un diente a la protesis"],
            "Protesis totales": ["Dentadura superior o inferior (incluye controles post-inatalción) c/u"],
            "Implantes dentales": ["Honorarios cirujano por implante","Implante y aditamientos","Injertos óseos (1cc)","PRF (incluye bionalista y extraccion de sangre + centrifugado)","Corona metal porcelana sobre implante","DPR acrilica"],
        }
        self.valores_monto = {
            "Consulta e Historia Clinica sin informe" : 20,
            "Consulta e Historia Clinica con informe" : 25,
            "Tartectomia y pulido simple (1 sesión)":40,
            "Tartectomia y pulido simple (2-3 sesiones)":60,
            "Aplicación tópica de fluór":30,
            "Cirguia periodontal (por cuadrante)":60,
            "Blanqueamiento intrapulpar":110,
            "Blanqueamiento maxilar superior e inferioir (2 sesiones de 20 min c/u)":180,
            "Obturaciones provisionales":30,
            "Obturaciones con Amalgama":40,
            "Obturaciones con vidrio ionomerico pequeña":40,
            "Obturaciones con vidrio ionomerico grande":50,
            "Obturaciones con resina fotocurada":50,
            "Pulpotomías formocreasoladas":50,
            "Emergencias Endodontica":60,
            "Tratamiento endodontico monoradicular":130,
            "Tratamiento endodontico biradicular":160,
            "Tratamiento endodontico multiradicular":200,
            "Desobturación conductos":60,
            "Adultos e infantes":15,
            "Exodoncia simple":40,
            "Exodoncia quirurgica":60,
            "Exodoncia de dientes temporales":25,
            "Exodoncia de corales erupcionadas/incluidas":70,
            "Coronas provisionales por unidad":80,
            "Muñon artificial monoradicular":120,
            "Muñon artificial multiradicular":160,
            "Incrustacion resina/metálica":200,
            "Unidad de corona meta-porcelana":400,
            "Cementado de protesis fija":30,
            "1 a 3 unidades":250,
            "4 a 6 unidades":300,
            "7 a 12 unidades":350,
            "Unidadad adicional":20,
            "Ganchos contorneados retentativas acrilicas c/u":15,
            "Reparaciones protesis acrilicas y/oo agregar un diente a la protesis":35,
            "Dentadura superior o inferior (incluye controles post-inatalción) c/u":300,
            "Honorarios cirujano por implante":350,
            "Implante y aditamientos":350,
            "Injertos óseos (1cc)":200,
            "PRF (incluye bionalista y extraccion de sangre + centrifugado)":100,
            "Corona metal porcelana sobre implante":500,
            "DPR acrilica":120,
        }
    #     self.btn_back.clicked.connect(self.back_menu)
    #     self.btn_refresh.clicked.connect(self.cargarDatosPacientes)
    #     self.btn_registrar.clicked.connect(self.addPacients)
    #     self.btn_buscar_2.clicked.connect(self.searchDataForDelete)
    #     self.btn_borrar.clicked.connect(self.DeletaData)
    #     self.btn_buscar.clicked.connect(self.SearchDataForUpdate)
    #     self.btn_act.clicked.connect(self.UpdateData)
    def calcularDivisa(self, dolar):
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
        operacion = float(dolar)

        # Calcular la suma
        bolivares = operacion * valor_numerico
        suma_formateada = "{:.2f}".format(bolivares).replace(".", ",")

        # Retorna el valor calculado
        return suma_formateada, operacion

    def actualizar_costo_t1(self):
        seleccion_t1 = self.t1.currentText()

        # Define un diccionario para asignar los valores de monto a cada selección
       

        if seleccion_t1 in self.valores_monto:
            monto = self.valores_monto[seleccion_t1]
            bolivares, operacion = self.calcularDivisa(monto)  # Captura los valores retornados
            self.montobs_t1.setText(str(bolivares))  # Convierte a cadena y establece en el QLineEdit
            self.montodola_t1.setText(str(monto))
            print(f"Seleccionaste {seleccion_t1}")
            self.totalPrecio()
    def actualizar_costo_t2(self):
        seleccion_t1 = self.t2.currentText()

        # Define un diccionario para asignar los valores de monto a cada selección
       

        if seleccion_t1 in self.valores_monto:
            monto = self.valores_monto[seleccion_t1]
            bolivares, operacion = self.calcularDivisa(monto)  # Captura los valores retornados
            self.montobs_t2.setText(str(bolivares))  # Convierte a cadena y establece en el QLineEdit
            self.montodola_t2.setText(str(monto))
            print(f"Seleccionaste {seleccion_t1}")
            self.totalPrecio()
    def actualizar_costo_t3(self):
        seleccion_t1 = self.t3.currentText()

        # Define un diccionario para asignar los valores de monto a cada selección
       

        if seleccion_t1 in self.valores_monto:
            monto = self.valores_monto[seleccion_t1]
            bolivares, operacion = self.calcularDivisa(monto)  # Captura los valores retornados
            self.montobs_t3.setText(str(bolivares))  # Convierte a cadena y establece en el QLineEdit
            self.montodola_t3.setText(str(monto))
            print(f"Seleccionaste {seleccion_t1}")
            self.totalPrecio()
           
    def totalPrecio(self):
        # Calcula el total sumando los valores flotantes de los QLineEdits
        totalBs = 0.0
        totalUsd= 0.0

        # Asegúrate de manejar las conversiones a flotante correctamente y verifica que las cadenas no estén vacías
        if self.montobs_t1.text():
            totalBs += float(self.montobs_t1.text().replace(',', '.'))

        if self.montobs_t2.text():
            totalBs += float(self.montobs_t2.text().replace(',', '.'))

        if self.montobs_t3.text():
            totalBs += float(self.montobs_t3.text().replace(',', '.'))

        if self.montodola_t1.text():
            totalUsd += float(self.montodola_t1.text().replace(',', '.'))

        if self.montodola_t2.text():
            totalUsd += float(self.montodola_t2.text().replace(',', '.'))

        if self.montodola_t3.text():
            totalUsd += float(self.montodola_t3.text().replace(',', '.'))

        # Formatea el número con dos decimales
        totalBs_formateado = f'{totalBs:.2f}'
        totalUsd_formateado = f'{totalUsd:.2f}'
        

        # Asigna el valor formateado al QLineEdit
        self.totalBs.setText(totalBs_formateado)
        self.totaldola.setText(totalUsd_formateado)
    def actualizar_cb_tratamiento(self):
        # Obtiene la selección en t0
        seleccion_t0 = self.t0.currentText()
         
        # Limpia las ComboBox t1, t2, t3
        self.t1.clear()
        self.t2.clear()
        self.t3.clear()
       
        # Obtiene las opciones de tratamiento según la selección en t0
        opciones_tratamiento = self.tratamientos.get(seleccion_t0, [])

        # Agrega las opciones a las ComboBox correspondientes
        self.t1.addItems(opciones_tratamiento)
        self.t2.addItems(opciones_tratamiento)
        self.t3.addItems(opciones_tratamiento)

        

    def clearDiag(self):
        self.in_name_3.clear()
        self.in_apell_3.clear()
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

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            # Verificar si ya existe un paciente con la misma cédula
            cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
            existe_paciente = cursor.fetchone()[0]

            if existe_paciente > 0:
                QMessageBox.critical(self, "Error", "Ya existe un paciente con la misma cédula.")
                
                #limpia los campos luego de denegar el ingreso
                self.clearInputs()
                self.clearData()
                return

            # Si no existe un paciente con la misma cédula, ejecutar la consulta de inserción
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
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail,Context,Hipertension,Diabates,Coagualcion,Otros,Alergias,diabate_Data,hipertension_Data,Coagualcion_Data,Diagnotico FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (busqueda, idUser))
            resultado = cursor.fetchone()
            
            if resultado:
                (Cedula, Nombre, Apellido, Edad, Direccion, Sexo, 
                    Telefono, Mail, Context ,Hipertension, Diabates, Coagualcion,Otros,Alergias, 
                    diabate_Data , hipertension_Data ,Coagualcion_Data,Diagnotico ) = resultado
                
                self.in_cedula.setText(Cedula)
                self.in_name.setText(Nombre)
                self.in_apell.setText(Apellido)
                self.in_age.setText(Edad)  
                self.in_mail.setText(Mail)  # Correo
                self.in_dir.setText(Direccion)
                self.in_number.setText(Telefono)  # Prueba##
                self.motivo.setText(Context)
                self.hiper_control.setText(hipertension_Data)
                self.diabetes_control.setText(diabate_Data)
                self.coagualcion_control.setText(Coagualcion_Data)
                self.ln_data.setText(Otros)
                self.ln_alergias.setText(Alergias)
                self.in_name_3.setText(Nombre)
                self.in_apell_3.setText(Apellido)
                self.diag.setText(Diagnotico)
                self.in_name_4.setText(Nombre)
                self.in_apell_4.setText(Apellido)
                # horaDb = Hora_Diagnostico
                # fechaDb = Fecha_Diagnotico
                # self.fecha.setDateTime(fechaDb)
                # self.hora.setTime(horaDb) Para despues 
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
        try:
            cedula = self.in_cedula.text()
            nombre = self.in_name.text()
            apellido = self.in_apell.text()
            edad = self.in_age.text()
            direccion = self.in_dir.text()
            telefono = self.in_number.text()
            mail = self.in_mail.text()
            if self.btn_m.isChecked():
                valor_sexo = "Masculino"
            if self.btn_f.isChecked():
                valor_sexo = "Femenino"
            context = self.motivo.text()

            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
    
        # Actualizar los registros en la base de datos
            cursor.execute("UPDATE Pacientes SET Nombre=?, Apellido=?, Edad=?, Direccion=?, Sexo=? ,Telefono=? ,Mail =? , Context=? WHERE Cedula=?", (nombre, apellido, edad, direccion, valor_sexo, telefono ,mail, cedula , context))
            conexion.commit()
            
            QMessageBox.information(self, "Información", "Los datos se actualizaron correctamente")

            conexion.close()
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
        menu_principal = MenuPrincipal(self.id_user)
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
            menu_principal.lb_nombre.setText(textForMenu)
            menu_principal.show()
            self.hide()
       
            

app = QApplication(sys.argv)
IngresoUsuario = IngresoUsuario()
widget = QtWidgets.QStackedWidget()
widget.addWidget(IngresoUsuario)
widget.move(200, 80)
widget.setFixedHeight(580)
widget.setFixedWidth(750)
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()



try:
    sys.exit(app.exec_())
except:
    print("saliendo")