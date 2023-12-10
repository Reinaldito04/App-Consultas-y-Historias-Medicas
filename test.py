import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QCompleter

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Crear el widget QLineEdit
        self.busqueda = QLineEdit(self)
        layout.addWidget(self.busqueda)

        # Lista de sugerencias (puedes obtener esto de tu fuente de datos)
        sugerencias = ["123456", "234567", "345678", "456789", "567890"]

        # Crear un modelo de autocompletado con las sugerencias
        modelo_completer = QCompleter(sugerencias, self)
        modelo_completer.setCaseSensitivity(0)  # No distingue entre mayúsculas y minúsculas

        # Configurar el autocompletado para el QLineEdit
        self.busqueda.setCompleter(modelo_completer)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Autocompletado en PyQt5')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
