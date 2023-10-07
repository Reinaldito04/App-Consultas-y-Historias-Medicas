from bs4 import BeautifulSoup
import requests

url = 'https://www.bcv.org.ve'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

div_dolar = soup.find('div', id='dolar')

divisa = div_dolar.find('strong').text

# Eliminar espacios en blanco y comas
divisa_limpia = divisa.replace(' ', '').replace(',', '.')

# Convertir la cadena limpia en un número decimal
valor_numerico = float(divisa_limpia)

# Solicitar la cantidad de dólares al usuario
operacion = float(input("Ingrese sus dólares: "))

# Calcular la suma
bolivares = operacion * valor_numerico

# Formatear los valores con el formato "00,00"
divisa_formateada = "{:.2f}".format(valor_numerico).replace(".", ",")
suma_formateada = "{:.2f}".format(bolivares).replace(".", ",")

print("Valor de la divisa:", divisa_formateada)
print("Costo en Bolivares:", suma_formateada)
