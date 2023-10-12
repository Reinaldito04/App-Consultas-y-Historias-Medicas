from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication ,QMainWindow
from PyQt5.QtWidgets import QMessageBox,QTableWidgetItem
import sqlite3
import datetime

class historiaMenu(QMainWindow):
    def __init__(self, id_user):
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
        self.btn_edit_2.clicked.connect(self.addInformation)
        #     self.btn_back.clicked.connect(self.back_menu)
        #     self.btn_refresh.clicked.connect(self.cargarDatosPacientes)
        #     self.btn_registrar.clicked.connect(self.addPacients)
        #     self.btn_buscar_2.clicked.connect(self.searchDataForDelete)
        #     self.btn_borrar.clicked.connect(self.DeletaData)
        #     self.btn_buscar.clicked.connect(self.SearchDataForUpdate)
        #     self.btn_act.clicked.connect(self.UpdateData)
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
            cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail,Context,Hipertension,Diabates,Coagualcion,Otros,Alergias,diabate_Data,hipertension_Data,Coagualcion_Data FROM Pacientes WHERE Cedula = ? AND ID_user = ?", (busqueda, idUser))
            resultado = cursor.fetchone()
            
            if resultado:
                Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail, Context ,Hipertension, Diabates, Coagualcion,Otros,Alergias, diabate_Data , hipertension_Data ,Coagualcion_Data = resultado
                
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
       
       

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    historias = historiaMenu()
    historias.show()
    sys.exit(app.exec_())
