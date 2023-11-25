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
import time
import json

class historiaMenu(QMainWindow):
    def __init__(self):
        super(historiaMenu, self).__init__()
        loadUi("interfaces/History.ui", self)
        self.btn_buscar.clicked.connect(self.Searchdata)
        self.btn_agg.clicked.connect(self.AddPacient)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.btn_edit.clicked.connect(self.UpdateData)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_agg_2.clicked.connect(self.addInformation)
        self.btn_clear_2.clicked.connect(self.clearData)
        self.btn_agg_3.clicked.connect(self.addDiagnostico)
        self.btn_edit_2.clicked.connect(self.addInformation)
        self.btn_edit_3.clicked.connect(self.addDiagnostico)
        self.btn_clear_3.clicked.connect(self.clearDiag)
        self.btn_clear_4.clicked.connect(self.clearTrata)
        self.fecha_hora_actualizadas = False
        self.fecha_actualizadas = False
        self.tabWidget.currentChanged.connect(self.actualizar_fecha_hora_diagnostico)
        self.tabWidget.currentChanged.connect(self.actualizar_fecha_trata)
        self.btn_agg_4.clicked.connect(self.aggTrata)
        self.btn_edit_4.clicked.connect(self.editTratA)
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
            
    def actualizar_fecha_trata(self):
        # Solo actualiza los campos de fecha y hora si no se han actualizado previamente
        if not self.fecha_actualizadas:
            fecha_actual = QDate.currentDate()

            self.fecha_2.setDate(fecha_actual)

            # Marca que los campos se han actualizado
            self.fecha_actualizadas = True

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
        
    def editTratA(self):
        cedula = self.in_busqueda.text()
        fecha_tratamiento = self.fecha_2.date().toString('yyyy-MM-dd')
        if not cedula:
            QMessageBox.warning(self, "Error", "Por favor ingrese la cédula en el menú de registro ")
            return
        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()
            # Verificar si ya existe un registro para el paciente
            cursor.execute("SELECT ID_Trata FROM PTrata WHERE Cedula = ?", (cedula,))
            row = cursor.fetchone()
            
            if not row:
                QMessageBox.information(self,"No existe","No existe tratamientos para este paciente,por favor presiona el botón guardar")
            if row:
                cursor.execute("SELECT ID_Trata FROM PTrata WHERE Cedula=?",(cedula,))
                datos = cursor.fetchone()
                id_trata = datos[0]
                for i in range(6):
                    honorario = self.combo_honorario[i].currentText()
                    tratamiento = self.combo_tratamiento[i].currentText()

                    # Verificar si se seleccionó un tratamiento
                    if honorario != "Seleccione el tipo de honorario" and tratamiento:
                        # Crear los nombres de las columnas según el tipo de tratamiento
                        tipo_trata_column = f"Tipo_Trata{i + 1}"
                        trata_column = f"Tratamiento{i + 1}"
                        fecha_trata_column = "Fecha_Trata"

                        # Verificar si ya existe un tratamiento para esa columna
                        cursor.execute(f"SELECT {tipo_trata_column}, {trata_column} FROM PTrata WHERE ID_Trata = ?", (id_trata,))
                        existing_data = cursor.fetchone()

                        if existing_data:
                            # Si ya existe, actualizar los datos existentes
                            cursor.execute(f"""
                                UPDATE PTrata
                                SET {tipo_trata_column} = ?, {trata_column} = ?, {fecha_trata_column} = ?
                                WHERE ID_Trata = ?
                            """, (honorario, tratamiento, fecha_tratamiento, id_trata))
                        # Confirmar los cambios en la base de datos
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Tratamientos actualizados correctamente.")

            # Cierra la conexión con la base de datos
            conexion.close()

        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar los tratamientos: {str(error)}")
    def aggTrata(self):
        # Obtener información del paciente
        cedula = self.in_busqueda.text()
        fecha_tratamiento = self.fecha_2.date().toString('yyyy-MM-dd')

        # Verificar si la cédula está presente
        if not cedula:
            QMessageBox.warning(self, "Error", "Por favor ingrese la cédula en el menú de registro ")
            return

        try:
            conexion = sqlite3.connect('interfaces/database.db')
            cursor = conexion.cursor()

            # Verificar si ya existe un registro para el paciente
            cursor.execute("SELECT ID_Trata FROM PTrata WHERE Cedula = ?", (cedula,))
            row = cursor.fetchone()

            if row:
               QMessageBox.information(self,"Registro de Tratamientos","Ya existe tratamientos registrados para este paciente,\nPor favor presiona el boton editar")
               return
            else:
                # Si no existe, insertar un nuevo registro y obtener el ID asignado
                cursor.execute("INSERT INTO PTrata (Cedula) VALUES (?)", (cedula,))
                id_trata = cursor.lastrowid

            # Recorrer las combobox y obtener los tratamientos
            for i in range(6):
                honorario = self.combo_honorario[i].currentText()
                tratamiento = self.combo_tratamiento[i].currentText()

                # Verificar si se seleccionó un tratamiento
                if honorario != "Seleccione el tipo de honorario" and tratamiento:
                    # Crear los nombres de las columnas según el tipo de tratamiento
                    tipo_trata_column = f"Tipo_Trata{i + 1}"
                    trata_column = f"Tratamiento{i + 1}"
                    fecha_trata_column = "Fecha_Trata"

                    # Verificar si ya existe un tratamiento para esa columna
                    cursor.execute(f"SELECT {tipo_trata_column}, {trata_column} FROM PTrata WHERE ID_Trata = ?", (id_trata,))
                    existing_data = cursor.fetchone()

                    if existing_data:
                        # Si ya existe, actualizar los datos existentes
                        cursor.execute(f"""
                            UPDATE PTrata
                            SET {tipo_trata_column} = ?, {trata_column} = ?, {fecha_trata_column} = ?
                            WHERE ID_Trata = ?
                        """, (honorario, tratamiento, fecha_tratamiento, id_trata))
                    else:
                        # Si no existe, insertar un nuevo registro
                        cursor.execute(f"""
                            UPDATE PTrata
                            SET {tipo_trata_column} = ?, {trata_column} = ?, {fecha_trata_column} = ?
                            WHERE ID_Trata = ?
                        """, (honorario, tratamiento, fecha_tratamiento, id_trata))

            # Confirmar los cambios en la base de datos
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Tratamientos registrados correctamente.")

            # Cierra la conexión con la base de datos
            conexion.close()

        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar los tratamientos: {str(error)}")



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

    def AddPacient(self):
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
            QMessageBox.critical(self, "Error", "Por favor seleccione su sexo")
            return

        if not cedula or not nombre or not apellido or not edad or not valor_sexo or not mail or not telefono or not direccion or not contexto:
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
                cursor.execute(
                    "INSERT INTO Pacientes (Cedula, Nombre, Apellido, Edad, Sexo ,Direccion ,Telefono, Mail ,Context) VALUES (?, ?, ?, ?, ?, ?, ? , ? ,? , ?)",
                    (cedula, nombre, apellido, edad, valor_sexo, direccion, telefono, mail, contexto))

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
            busqueda = self.in_busqueda.text()
            cursor.execute(
                "SELECT Cedula, Nombre, Apellido, Edad, Direccion, Sexo, Telefono, Mail, Context, Hipertension, Diabates, Coagualcion, Otros, Alergias, Diabate_Data, Hipertension_Data, Coagualcion_Data, Diagnotico, Fecha_Diagnotico, Hora_Diagnostico FROM Pacientes WHERE Cedula = ?",
                (busqueda,))
            resultado = cursor.fetchone()

            if resultado:
                (Cedula, Nombre, Apellido, Edad, Direccion, Sexo,
                Telefono, Mail, Context, Hipertension, Diabates, Coagualcion, Otros, Alergias,
                Diabate_Data, Hipertension_Data, Coagualcion_Data, Diagnotico, Fecha_Diagnotico,
                Hora_Diagnostico) = resultado

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
                if Diabates == "Si":
                    self.btn_si_4.setChecked(True)
                else:
                    self.btn_no_4.setChecked(True)
                if Coagualcion == "Si":
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
        if not busqueda:
            QMessageBox.warning(self, "Error", "Introduzca su cedula")
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
            cursor.execute(
                "UPDATE Pacientes SET Nombre=?, Apellido=?, Edad=?, Direccion=?, Sexo=? ,Telefono=? ,Mail =? , Context=? WHERE Cedula=?",
                (nombre, apellido, edad, direccion, valor_sexo, telefono, mail, context, cedula))
            conexion.commit()

            QMessageBox.information(self, "Información", "Los datos se actualizaron correctamente")

            conexion.close()
            self.Searchdata()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", "Error al actualizar los datos en la base de datos: " + str(e))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")
    Vista_P = historiaMenu()
    Vista_P.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(Vista_P)
    widget.setGeometry(Vista_P.geometry())
    widget.show()
    sys.exit(app.exec_())
