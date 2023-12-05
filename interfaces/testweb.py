import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.uic import loadUi
from bs4 import BeautifulSoup
import requests
from urllib3.exceptions import InsecureRequestWarning  # Modificación en la importación
import sqlite3

class WorkerThread(QThread):
    result_signal = pyqtSignal(tuple)

    def __init__(self, dolar):
        super().__init__()
        self.dolar = dolar

    def run(self):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        url = 'https://www.bcv.org.ve'
        response = requests.get(url, verify=False)

        soup = BeautifulSoup(response.text, 'html.parser')

        div_dolar = soup.find('div', id='dolar')

        divisa = div_dolar.find('strong').text

        divisa_limpia = divisa.replace(' ', '').replace(',', '.')
        valor_numerico = float(divisa_limpia)
        operacion = float(self.dolar)

        bolivares = operacion * valor_numerico
        suma_formateada = "{:.2f}".format(bolivares).replace(".", ",")

        self.result_signal.emit((suma_formateada, operacion))

class HistoriaMenu(QMainWindow):
    def __init__(self, id_user):
        super(HistoriaMenu, self).__init__()
       
        self.id_user = id_user

        # Crear elementos de la interfaz
        self.dolar_input = QLineEdit(self)
        self.dolar_input.setGeometry(30, 40, 113, 22)

        self.calcular_divisa_button = QPushButton('Calcular Divisa', self)
        self.calcular_divisa_button.setGeometry(30, 80, 111, 32)
        self.calcular_divisa_button.clicked.connect(self.start_divisa_thread)

        self.resultado_label = QLabel('', self)
        self.resultado_label.setGeometry(30, 130, 341, 61)

    def start_divisa_thread(self):
        # Obtener el valor del QLineEdit
        dolar_value = self.dolar_input.text()

        # Crea y ejecuta el hilo de trabajo
        self.worker_thread = WorkerThread(dolar_value)
        self.worker_thread.result_signal.connect(self.on_divisa_finished)
        self.worker_thread.start()

    def on_divisa_finished(self, result):
        # Esta función se llama cuando la tarea en segundo plano está completa
        suma_formateada, operacion = result
        self.resultado_label.setText(f"Resultado: {suma_formateada}, Operación: {operacion}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HistoriaMenu(1)  # Reemplaza 1 con el id_user adecuado
    window.show()
    sys.exit(app.exec_())
