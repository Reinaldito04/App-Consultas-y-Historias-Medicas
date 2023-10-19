from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem

import sqlite3


class Ui_placas(QMainWindow):
    def __init__(self, id_user):
        super(Ui_placas, self).__init__()
        loadUi("interfaces\placas(nueva).ui", self)
        self.id_user= id_user
        self.btn_agg.clicked.connect(self.addplacas)
        self.btn_buscar.clicked.connect(self.searchData)
        self.btn_clear.clicked.connect(self.clearInputs)
        self.actionSalir.triggered.connect(self.salir)
        self.btn_import.clicked.connect(self.addPhoto)

        self.btn_buscar_2.clicked.connect(self.buscarDatos)
        
    def salir(self):
       QApplication.quit()
       
    def clearInputs(self):
        self.in_busqueda.clear()
        self.in_busqueda_2.clear()
        self.in_name.clear()
        self.in_apell.clear()
        self.in_name2.clear()
        self.in_apell2.clear()
        
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

    def addPhoto(self):
            filenames, _ = QFileDialog.getOpenFileNames(self, "Seleccionar imágenes", "", "Archivos de imagen (*.png *.jpg *.bmp)")
                
            if len(filenames) >= 3:
                    pixmap1 = QPixmap(filenames[0])
                    pixmap2 = QPixmap(filenames[1])
                    pixmap3 = QPixmap(filenames[2])
                        
                    self.foto.setPixmap(pixmap2)
                    self.foto.setPixmap(pixmap3)
                    self.foto.setPixmap(pixmap1)
            else:
                    QMessageBox.information(self,"Imagenes","Por favor,Selecciona una imagen")    
    
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    placa = Ui_placas()
    placa.show()
    sys.exit(app.exec_())