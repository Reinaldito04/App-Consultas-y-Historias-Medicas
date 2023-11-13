import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sqlite3

class Ui_SI(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_SI, self).__init__()
        loadUi("./interfaces/SI.ui", self)
        self.setWindowTitle("SI")

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

        for combo in self.combo_honorario:
            combo.addItem("Seleccione el tipo de honorario")
            combo.addItems(list(self.tratamientos.keys()))
            combo.currentTextChanged.connect(self.loadTratamientos)

        for i, combo in enumerate(self.combo_tratamiento):
            combo.currentTextChanged.connect(lambda _, index=i: self.update_monto(index))

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

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("si")

    SI = Ui_SI()
    SI.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(SI)
    widget.setGeometry(SI.geometry())

    widget.show()
    sys.exit(app.exec_())
