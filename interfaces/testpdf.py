import sqlite3
from PyQt5.QtGui import QIcon, QFont, QTextDocument
from PyQt5.QtCore import Qt, QFileInfo, QTextCodec, QByteArray, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import (QApplication, QTreeWidget, QTreeWidgetItem, QDialog, QPushButton, QFileDialog,
                             QMessageBox, QToolBar)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QStackedWidget,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout



class IngresoUsuario(QMainWindow):
    def __init__(self):
        super(IngresoUsuario,self).__init__()
        loadUi("interfaces/pdfui.ui",self)
        self.bt_buscar.clicked.connect(self.cargarDatos)
        self.bt_preview.clicked.connect(self.previewpdf)
        self.documento = QTextDocument()
        
    def previewpdf(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)
            
            vista = QPrintPreviewDialog(impresion, self)
            vista.setWindowTitle("Vista previa")
            vista.setWindowFlags(Qt.Window)
            vista.resize(800, 600)

            exportarPDF = vista.findChildren(QToolBar)
            exportarPDF[0].addAction(QIcon("exportarPDF.png"), "Exportar a PDF", self.exportarPDF)
            
            vista.paintRequested.connect(self.vistaPreviaImpresion)
            vista.exec_()
        else:
            QMessageBox.critical(self, "Vista previa", "No hay datos para visualizar.   ",
                                 QMessageBox.Ok)


    def exportarPDF(self):
        if not self.documento.isEmpty():
            nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Listado de usuarios",
                                                           "Archivos PDF (*.pdf);;All Files (*)",
                                                           options=QFileDialog.Options())

            if nombreArchivo:
                # if QFileInfo(nombreArchivo).suffix():
                #     nombreArchivo += ".pdf"

                impresion = QPrinter(QPrinter.HighResolution)
                impresion.setOutputFormat(QPrinter.PdfFormat)
                impresion.setOutputFileName(nombreArchivo)
                self.documento.print_(impresion)

                QMessageBox.information(self, "Exportar a PDF", "Datos exportados con éxito.   ",
                                        QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Exportar a PDF", "No hay datos para exportar.   ",
                                 QMessageBox.Ok)
    def vistaPreviaImpresion(self, impresion):
        self.documento.print_(impresion)

    def Imprimir(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)
            
            dlg = QPrintDialog(impresion, self)
            dlg.setWindowTitle("Imprimir documento")

            if dlg.exec_() == QPrintDialog.Accepted:
                self.documento.print_(impresion)

            del dlg
        else:
            QMessageBox.critical(self, "Imprimir", "No hay datos para imprimir.   ",
                                 QMessageBox.Ok)

    def cargarDatos(self):
        conexionDB = sqlite3.connect("interfaces/database.db")
        cursor = conexionDB.cursor()

        cursor.execute("SELECT Cedula, Nombre, Apellido, Edad, Sexo FROM Pacientes")
        datosDB = cursor.fetchall()

        conexionDB.close()

        if datosDB:
            self.documento.clear()
            self.treeWidget.clear()

            datos = ""
            item_widget = []
            for dato in datosDB:
                datos += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %dato
                item_widget.append(QTreeWidgetItem((str(dato[0]), dato[1], dato[2], dato[3],dato[4])))

            reporteHtml = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
h3 {
    font-family: Helvetica-Bold;
    text-align: center;
   }

table {
       font-family: arial, sans-serif;
       border-collapse: collapse;
       width: 100%;
      }

td {
    text-align: left;
    padding-top: 4px;
    padding-right: 6px;
    padding-bottom: 2px;
    padding-left: 6px;
   }

th {
    text-align: left;
    padding: 4px;
    background-color: black;
    color: white;
   }

tr:nth-child(even) {
                    background-color: #dddddd;
                   }
</style>
</head>
<body>

<h3>Pacientes Registrados en la clinica<br/></h3>

<table align="left" width="100%" cellspacing="0">
  <tr>
    <th>Cedula</th>
    <th>NOMBRE</th>
    <th>APELLIDO</th>
    <th>Edad</th>
    <th>Sexo</th>
  </tr>
  [DATOS]
</table>

</body>
</html>
""".replace("[DATOS]", datos)

            datos = QByteArray()
            datos.append(str(reporteHtml))
            codec = QTextCodec.codecForHtml(datos)
            unistr = codec.toUnicode(datos)

            if Qt.mightBeRichText(unistr):
                self.documento.setHtml(unistr)
            else:
                self.documento.setPlainText(unistr)

            self.treeWidget.addTopLevelItems(item_widget)
        else:
            QMessageBox.information(self, "Buscar usuarios", "No se encontraron resultados.      ",
                                    QMessageBox.Ok)

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