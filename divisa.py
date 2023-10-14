from bs4 import BeautifulSoup
import requests

url = 'https://www.bcv.org.ve'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

div_dolar = soup.find('div', id='dolar')

divisa = div_dolar.find('strong').text

divisa_limpia = divisa.replace(' ', '').replace(',', '.')
valor_numerico = float(divisa_limpia)

operacion = float(input("Ingrese sus dólares: "))

bolivares = operacion * valor_numerico

divisa_formateada = "{:.2f}".format(valor_numerico).replace(".", ",")
suma_formateada = "{:.2f}".format(bolivares).replace(".", ",")

print("Valor de la divisa:", divisa_formateada)
print("Costo en Bolivares:", suma_formateada)
