from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
import sqlite3
from bs4 import BeautifulSoup
import requests
import datetime

class historiaMenu(QMainWindow):
    
    def __init__(self ):
        super(historiaMenu, self).__init__()
        loadUi("interfaces\History.ui", self)
        self.btn_buscar.clicked.connect(self.Searchdata)
        self.btn_agg.clicked.connect(self.AddPacient)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.btn_edit.clicked.connect(self.UpdateData)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_delete.clicked.connect(self.DeletaData)
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
    
        
        
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    historias = historiaMenu()
    historias.show()
    sys.exit(app.exec_())
