import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
import hashlib
import sqlite3
import os
import datetime
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
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000)

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
            
                if (horaActual >= datetime.time(5, 0, 0)) and (horaActual <= datetime.time(12, 0, 0)):
                   
                   textForMenu = f"Buenos dias {nombre} \n¿Que deseas hacer hoy?"
    
                if (horaActual >= datetime.time(12, 0, 0)) and (horaActual <= datetime.time(18, 0, 0)):
                   
                   textForMenu = f"Buenas tardes {nombre} \n¿Que deseas hacer hoy?"
                   
                if (horaActual >= datetime.time(18, 0, 0)) and (horaActual <= datetime.time(5, 0, 0)):
                   
                   textForMenu = f"Buenas noches {nombre} \n¿Que deseas hacer hoy?"
                else :
                     textForMenu = f"Hola {nombre} \n¿Que deseas hacer hoy?"
                    
               
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
        super(Registro , self). __init__()
        loadUi("./interfaces/register.ui", self)
        self.bt_end.clicked.connect(self.close)
        self.bt_register.clicked.connect(self.registrarUsuario)
        self.bt_back.clicked.connect(self.ingresoLogin)
        
    
        
        
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
        conexion = sqlite3.connect('interfaces\database.db')
        nombre = self.txt_user.text()
        password = self.txt_password.text()
        passwordRepeat = self.txt_password_repeat.text()
        
        if len(nombre and password and passwordRepeat) <=0:
            QMessageBox.critical(self,"Error","Ningun campo ha sido llenado")
            return
        if len( password or passwordRepeat) <=0:
            QMessageBox.critical(self,"Error","Digite su contraseña")
            return
        else :
        
            
            if len(nombre) < 6:
                QMessageBox.critical(self, "Error", "El nombre de usuario debe tener minimo 6 caracteres.")
                return
        
            if len(password) < 6:
                QMessageBox.critical(self, "Error", "La contraseña debe tener minimo 6 caracteres.")
                return
            if len(passwordRepeat) < 6:
                QMessageBox.critical(self, "Error", "La contraseña debe minimo tener 6 caracteres.")
                return
        
         
        if password == passwordRepeat:
            if self.usuario_existe(nombre):
                QMessageBox.warning(self, "Error", "El nombre de usuario ya existe. \nIngrese uno distinto")
                return
            else:
                # Conectar a la base de datos
                contrasenia_cifrada = self.cifrar_contrasenia(password)
                conexion = sqlite3.connect('interfaces/database.db')

                # Crear un cursor
                cursor = conexion.cursor()

                # Insertar datos en la base de datos
                cursor.execute('INSERT INTO Users (Username, Password) VALUES (?, ?)', (nombre, contrasenia_cifrada))

                # Confirmar los cambios en la base de datos y cerrar la conexión
                conexion.commit()
                conexion.close()

                QMessageBox.information(self, "Éxito", "Registro exitoso")
        else:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
            self.txt_user.clear()
            self.txt_password.clear()
            self.txt_password_repeat.clear()
       

        
        
        
    def close(self):
       QApplication.quit()
        

class MenuPrincipal(QMainWindow):
    def __init__(self , id_user):
        super(MenuPrincipal , self). __init__()
        loadUi("./interfaces/menu.ui", self)
        self.frame_opciones.hide()
        self.id_user  = id_user
        self.bt_info.clicked.connect(self.passwordView)
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
            widget.setFixedWidth(900)
            self.hide()
    def passwordView(self):
        reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Deseas ir al formulario de cambio de contraseña?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
        if reply ==QMessageBox.Yes:
            contraseñaView = PasswordMenu(self.id_user)
            widget.addWidget(contraseñaView)
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
class CitasMenu(QMainWindow):
    def __init__(self,id_user):
        super(CitasMenu, self).__init__()
        self.id_user = id_user
        loadUi("interfaces\citas.ui", self)
        self.btn_citas.clicked.connect(self.mostrarCitas)
        self.btn_agg_cita.clicked.connect(self.mostrarFormularioAgendarCita)
        self.btn_borrar.clicked.connect(self.mostrarFormularioEliminarCita)
        self.btn_back.clicked.connect(self.volverAlMenu)
        self.btn_refresh.clicked.connect(self.buscarCitas)
        self.btn_buscar_2.clicked.connect(self.buscarPacienteParaCita)
        self.btn_edit.clicked.connect(self.editarCita)
        self.btn_agg.clicked.connect(self.agendarCita)
        self.btn_buscar_3.clicked.connect(self.buscarCitaParaEliminar)
        self.btn_delete.clicked.connect(self.eliminarCita)

    def mostrarCitas(self):
        self.stackedWidget.setCurrentWidget(self.tabla_citas)
        
 # Función para mostrar el formulario de agendar cita
    def mostrarFormularioAgendarCita(self):
        self.stackedWidget.setCurrentWidget(self.agg_cita)

    # Función para mostrar el formulario de eliminar cita
    def mostrarFormularioEliminarCita(self):
        self.stackedWidget.setCurrentWidget(self.delete_cita)

    # Función para volver al menú principal
    def volverAlMenu(self):
        print("Volviendo al menú principal")
        menu_principal = MenuPrincipal(self.id_user)
        conexion =sqlite3.connect('interfaces/database.db')
        cursor= conexion.cursor()
        cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
        resultado= cursor.fetchone()
        if resultado :
            nombre_usuario= resultado[0]
            horaActual = datetime.datetime.now().time()
            
            if (horaActual >= datetime.time(5, 0, 0)) and (horaActual <= datetime.time(12, 0, 0)):
                   
                textForMenu = f"Buenos dias {nombre_usuario} \n¿Que deseas hacer hoy?"
    
            if (horaActual >= datetime.time(12, 0, 0)) and (horaActual <= datetime.time(18, 0, 0)):
                   
                textForMenu = f"Buenas tardes {nombre_usuario} \n¿Que deseas hacer hoy?"
                   
            if (horaActual >= datetime.time(18, 0, 0)) and (horaActual <= datetime.time(5, 0, 0)):
                   
                textForMenu = f"Buenas noches {nombre_usuario} \n¿Que deseas hacer hoy?"
            else :
                    textForMenu = f"Hola {nombre_usuario} \n¿Que deseas hacer hoy?"
            menu_principal.lb_nombre.setText(textForMenu)
            menu_principal.show()
            self.hide()
        pass
 # Función para buscar citas
    def buscarCitas(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            idUser = self.id_user

            # Ejecuta una consulta para obtener los datos de los pacientes y ordenar por Fecha_Cita descendente
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Fecha_Cita, Hora_Cita FROM Pacientes WHERE ID_user = ? ORDER BY Fecha_Cita ASC, Hora_Cita ASC ", (idUser,))
            tabla_cita = cursor.fetchall()
            conexion.close()

            # Filtrar las filas que no contengan ningún valor 'None'
            filas_filtradas = [paciente for paciente in tabla_cita if None not in paciente]

            # Limpiar la tabla existente si es necesario
            self.tabla_cita.clearContents()

            # Establecer el número de filas y columnas en la tabla
            self.tabla_cita.setRowCount(len(filas_filtradas))
            self.tabla_cita.setColumnCount(len(filas_filtradas[0]))

            # Agregar los datos a la tabla
            for row, paciente in enumerate(filas_filtradas):
                for column, value in enumerate(paciente):
                    item = QTableWidgetItem(str(value))
                    self.tabla_cita.setItem(row, column, item)
        except:
            QMessageBox.critical(self, "Error", "No hay citas actualmente.")

    # Función para buscar paciente para asignar cita
    def buscarPacienteParaCita(self):
        idUser = self.id_user
        cedula =self.in_busqueda_2.text()
        if len(cedula) <=0:
            QMessageBox.warning(self,"Error","Ingrese una cedula")
        else:
            name = self.in_name.text()
            apellido = self.in_apell.text()
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

    # Función para editar una cita
    def editarCita(self):
        idUser = self.id_user
        cedula = self.in_busqueda_2.text()
        
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

    # Función para agendar una cita
    def agendarCita(self):
        idUser = self.id_user
        cedula = self.in_busqueda_2.text()
        
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
                QMessageBox.information(self, "Información", "Cita guardada con éxito.")
            else:
                # Si el paciente no existe, mostrar un mensaje de error
                QMessageBox.warning(self, "Advertencia", "No se encontró un paciente con la cédula proporcionada.")
            
            # Cerrar la conexión con la base de datos
            conexion.close()
            
        except sqlite3.Error as error:
            # En caso de error, mostrar un mensaje de error
            QMessageBox.critical(self, "Error", f"Error al guardar la cita: {str(error)}")
        
        

    # Función para buscar una cita para eliminar
    def buscarCitaParaEliminar(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            idUser = self.id_user
            cedula = self.in_busqueda_3.text()
            # Ejecuta una consulta para obtener los datos de los pacientes
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion , Sexo, Fecha_Cita, Hora_Cita  FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (cedula , idUser) )
            
           
            tabla_citas_delete = cursor.fetchall()
            conexion.close()

            # Limpiar la tabla existente si es necesario
            self.tabla_citas_delete.clearContents()

            # Establecer el número de filas y columnas en la tabla
            self.tabla_citas_delete.setRowCount(len(tabla_citas_delete))
            self.tabla_citas_delete.setColumnCount(len(tabla_citas_delete[0]))

            # Agregar los datos a la tabla
            for row, paciente in enumerate(tabla_citas_delete):
                for column, value in enumerate(paciente):
                    item = QTableWidgetItem(str(value))
                    self.tabla_citas_delete.setItem(row, column, item)
        except:
            QMessageBox.critical(self, "Error", "No hay ningún paciente con esa cedula.")

    # Función para eliminar una cita
    def eliminarCita(self):
        try:
            cedula = self.in_busqueda_3.text()
    
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
                self.tabla_citas_delete.clearContents()
                self.in_busqueda_3.clear()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al eliminar la cita  de la base de datos: " + str(e))
        pass

        
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
        conexion = sqlite3.connect('interfaces/database.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT Username From Users WHERE ID =? ", (self.id_user,))
        resultado = cursor.fetchone()
        nombre = resultado[0]
        textForMenu = f"¿Que deseas hacer {nombre}?"
        menu_principal = MenuPrincipal(self.id_user)
        menu_principal.show()
        menu_principal.lb_nombre.setText(textForMenu)
        
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
        filenames, _ = QFileDialog.getOpenFileNames(self, "Seleccionar imágenes", "", "Archivos de imagen (*.png *.jpg *.bmp)")
        
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
            
            if (horaActual >= datetime.time(5, 0, 0)) and (horaActual <= datetime.time(12, 0, 0)):
                   
                textForMenu = f"Buenos dias {nombre_usuario} \n¿Que deseas hacer hoy?"
    
            if (horaActual >= datetime.time(13, 0, 0)) and (horaActual <= datetime.time(18, 0, 0)):
                   
                textForMenu = f"Buenas tardes {nombre_usuario} \n¿Que deseas hacer hoy?"
                   
            if (horaActual >= datetime.time(18, 0, 0)) and (horaActual <= datetime.time(5, 0, 0)):
                   
                textForMenu = f"Buenas noches {nombre_usuario} \n¿Que deseas hacer hoy?"
                
            else :
                textForMenu = f"Hola {nombre_usuario} \n¿Que deseas hacer hoy?"
            menu_principal.lb_nombre.setText(textForMenu)
            menu_principal.show()
            self.hide()
        
        
        
       
class historiaMenu(QMainWindow):
    def __init__(self ,id_user):
        super(historiaMenu, self).__init__()
        loadUi("interfaces\History.ui", self)
        self.id_user = id_user
        self.btn_buscar.clicked.connect(self.Searchdata)
    #     self.btn_back.clicked.connect(self.back_menu)
    #     self.btn_refresh.clicked.connect(self.cargarDatosPacientes)
    #     self.btn_registrar.clicked.connect(self.addPacients)
    #     self.btn_buscar_2.clicked.connect(self.searchDataForDelete)
    #     self.btn_borrar.clicked.connect(self.DeletaData)
    #     self.btn_buscar.clicked.connect(self.SearchDataForUpdate)
    #     self.btn_act.clicked.connect(self.UpdateData)
       
    def Searchdata(self):
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()  
            idUser = self.id_user
            busqueda = self.in_busqueda.text()
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion , Sexo  FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (busqueda , idUser) )
            resultado = cursor.fetchone()
            if resultado:
                Cedula , Nombre , Apellido , Edad, Direccion , Sexo = resultado
                self.in_cedula.setText(Cedula)
                self.in_name.setText(Nombre)
                self.in_apell.setText(Apellido)
                self.in_age.setText(Edad)
                self.in_dir.setText(Direccion)
                self.in_number.setText(Sexo) #Prueba##
            else:
                QMessageBox.warning(self,"Advertencia","No se ha encontrado algun registro")
               
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e)) 
    # def UpdateData(self):
    #     try:
    #         cedula = self.txt_id_2.text()
    #         nombre = self.txt_name_2.text()
    #         apellido = self.txt_apell_2.text()
    #         edad = self.txt_age_2.text()
    #         direccion = self.txt_dir_2.text()
    #         sexo = self.txt_gen_2.text()

    #         conexion = sqlite3.connect('interfaces/database.db')
    #         cursor = conexion.cursor()
    
    #     # Actualizar los registros en la base de datos
    #         cursor.execute("UPDATE Pacientes SET Nombre=?, Apellido=?, Edad=?, Direccion=?, Sexo=? WHERE Cedula=?", (nombre, apellido, edad, direccion, sexo, cedula))
    #         conexion.commit()
            
    #         QMessageBox.information(self, "Información", "Los datos se actualizaron correctamente")

    #         conexion.close()
    #     except sqlite3.Error as e:
    #         QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))
    # def SearchDataForUpdate(self):
    #     try:
    #         idUser = self.id_user
    #         cedula = self.in_busqueda_edit.text()
    #         conexion = sqlite3.connect('interfaces/database.db')
    #         cursor=conexion.cursor()
    #         cursor.execute("SELECT Cedula ,Nombre, Apellido , Edad , Direccion , Sexo FROM Pacientes WHERE Cedula = ? AND ID_user = ? ", (cedula,idUser))
    #         resultado = cursor.fetchone()
    #         if resultado :
    #             Cedula ,Nombre , Apellido , Edad , Direccion , Sexo = resultado
    #             self.txt_id_2.setReadOnly(True)
    #             self.txt_id_2.setText(Cedula)
    #             self.txt_name_2.setText(Nombre)
    #             self.txt_apell_2.setText(Apellido)
    #             self.txt_age_2.setText(Edad)
    #             self.txt_dir_2.setText(Direccion)
    #             self.txt_gen_2.setText(Sexo)
    #         else:
    #             QMessageBox.warning(self,"Advertencia","No se encontraron registros con esa cedula")            
    #         conexion.close()
    #     except sqlite3.Error as e:
    #         QMessageBox.critical(self, "Error", "Error al consultar la base de datos: " + str(e))
    # def searchDataForDelete(self):
    #     try:
    #         conexion = sqlite3.connect('interfaces/database.db')
    #         cursor = conexion.cursor()
    #         idUser = self.id_user
    #         cedula = self.in_busqueda_delete.text()
    #         # Ejecuta una consulta para obtener los datos de los pacientes
    #         cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion , Sexo  FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (cedula , idUser) )
            
           
    #         tabla_pacientes = cursor.fetchall()
    #         conexion.close()

    #         # Limpiar la tabla existente si es necesario
    #         self.tabla_borrar.clearContents()

    #         # Establecer el número de filas y columnas en la tabla
    #         self.tabla_borrar.setRowCount(len(tabla_pacientes))
    #         self.tabla_borrar.setColumnCount(len(tabla_pacientes[0]))

    #         # Agregar los datos a la tabla
    #         for row, paciente in enumerate(tabla_pacientes):
    #             for column, value in enumerate(paciente):
    #                 item = QTableWidgetItem(str(value))
    #                 self.tabla_borrar.setItem(row, column, item)
    #     except:
    #          QMessageBox.critical(self, "Error", "No hay ningún paciente con esa cedula.")
    # def DeletaData(self):
        
    #     try:
    #         cedula = self.in_busqueda_delete.text()
    
    #         if len(cedula) == 0:
    #             QMessageBox.critical(self, "Error", "Ingrese una cédula")
    #         else:
    #             conexion = sqlite3.connect('interfaces/database.db')
    #             cursor = conexion.cursor()
    #             cursor.execute("DELETE FROM Pacientes WHERE Cedula = ?", (cedula,))
    #             conexion.commit()
    #             conexion.close()
        
    #     # Eliminación exitosa, muestra un mensaje y realiza otras acciones si es necesario
    #             QMessageBox.information(self, "Realizado", "Los datos han sido eliminados correctamente")
    #             self.tabla_borrar.clearContents()
    #             self.in_busqueda_delete.clear()
    #     except sqlite3.Error as e:
    #         QMessageBox.critical(self, "Error", "Error al eliminar los datos de la base de datos: " + str(e))
    
    # def addPacients(self):
    #     idUser = self.id_user
    #     cedula = self.txt_cedula.text()
    #     nombre = self.txt_name.text()
    #     apellido = self.txt_apellido.text()
    #     edad = self.txt_age.text()
    #     sexo = self.txt_sex.text()
    #     direccion = self.txt_dir.text()
        

    #     if not cedula or not nombre or not apellido or not edad or not sexo or not direccion:
    #         QMessageBox.critical(self, "Error", "Por favor, complete todos los campos.")
    #         return

    #     try:
    #         conexion = sqlite3.connect('interfaces/database.db')
    #         cursor = conexion.cursor()

    #         # Verificar si ya existe un paciente con la misma cédula
    #         cursor.execute("SELECT COUNT(*) FROM Pacientes WHERE Cedula = ?", (cedula,))
    #         existe_paciente = cursor.fetchone()[0]

    #         if existe_paciente > 0:
    #             QMessageBox.critical(self, "Error", "Ya existe un paciente con la misma cédula.")
                
    #             #limpia los campos luego de denegar el ingreso
    #             self.txt_cedula.clear()
    #             self.txt_name.clear()
    #             self.txt_apellido.clear()
    #             self.txt_age.clear()
    #             self.txt_sex.clear()
    #             self.txt_dir.clear()
    #             return

    #         # Si no existe un paciente con la misma cédula, ejecutar la consulta de inserción
    #         cursor.execute("INSERT INTO Pacientes (Cedula, Nombre, Apellido, Edad, Sexo ,Direccion , ID_user) VALUES (?, ?, ?, ?, ?, ?, ?)",
    #                     (cedula, nombre, apellido, edad, sexo , direccion , idUser))

    #         # Confirmar los cambios en la base de datos
    #         conexion.commit()

    #         QMessageBox.information(self, "Éxito", "Paciente registrado correctamente.")

    #         # Limpia los campos después de agregar el paciente
    #         self.txt_cedula.clear()
    #         self.txt_name.clear()
    #         self.txt_apellido.clear()
    #         self.txt_age.clear()
    #         self.txt_sex.clear()
    #         self.txt_dir.clear()
    #         # Cierra la conexión con la base de datos
    #         conexion.close()

    #     except sqlite3.Error as error:
    #         QMessageBox.critical(self, "Error", f"Error al registrar el paciente: {str(error)}")

    
    # def cargarDatosPacientes(self):
    #     try:
    #         conexion = sqlite3.connect('interfaces/database.db')
    #         cursor = conexion.cursor()
    #         idUser = self.id_user

    #         # Ejecuta una consulta para obtener los datos de los pacientes
    #         cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo FROM Pacientes WHERE ID_user = ?", (idUser,))
    #         tabla_pacientes = cursor.fetchall()

    #         # Cerrar la conexión con la base de datos
    #         conexion.close()

    #         # Limpiar la tabla existente si es necesario
    #         self.tabla_pacientes.clearContents()

    #         if tabla_pacientes:
    #             # Establecer el número de filas y columnas en la tabla
    #             self.tabla_pacientes.setRowCount(len(tabla_pacientes))
    #             self.tabla_pacientes.setColumnCount(len(tabla_pacientes[0]))

    #             # Agregar los datos a la tabla
    #             for row, paciente in enumerate(tabla_pacientes):
    #                 for column, value in enumerate(paciente):
    #                     item = QTableWidgetItem(str(value))
    #                     self.tabla_pacientes.setItem(row, column, item)
    #         else:
    #             # Si no hay datos, puedes mostrar un mensaje o realizar otra acción apropiada
    #             QMessageBox.information(self, "Información", "No se encontraron datos de pacientes.")

    #     except sqlite3.Error as error:
    #         QMessageBox.critical(self, "Error", f"Error al cargar los datos de pacientes: {str(error)}")
            
        
        
        
    # def back_menu(self):
    #     menu_principal = MenuPrincipal(self.id_user)
    #     conexion = sqlite3.connect('interfaces/database.db')
    #     cursor= conexion.cursor()
    #     cursor.execute("SELECT Username FROM Users WHERE ID = ?", (self.id_user,))
        
    #     resultado = cursor.fetchone()
    #     if resultado :
    #         nombre_usuario = resultado[0]
    #         horaActual = datetime.datetime.now().time()
            
    #         if (horaActual >= datetime.time(5, 0, 0)) and (horaActual <= datetime.time(12, 0, 0)):
                   
    #             textForMenu = f"Buenos dias {nombre_usuario} \n¿Que deseas hacer hoy?"
    
    #         if (horaActual >= datetime.time(13, 0, 0)) and (horaActual <= datetime.time(18, 0, 0)):
                   
    #             textForMenu = f"Buenas tardes {nombre_usuario} \n¿Que deseas hacer hoy?"
                   
    #         if (horaActual >= datetime.time(18, 0, 0)) and (horaActual <= datetime.time(5, 0, 0)):
                   
    #             textForMenu = f"Buenas noches {nombre_usuario} \n¿Que deseas hacer hoy?"
                
    #         else :
    #                 textForMenu = f"Hola {nombre_usuario} \n¿Que deseas hacer hoy?"
    #         menu_principal.lb_nombre.setText(textForMenu)
    #         menu_principal.show()
    #         self.hide()
       
            

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