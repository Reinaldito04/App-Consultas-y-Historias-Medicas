from weasyprint import HTML
import os
import base64
import sqlite3
from datetime import datetime


def recuperar_datos_bd(cedula):
    conexion = sqlite3.connect("interfaces/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT Nombre, Apellido, Direccion, Telefono, context FROM Pacientes WHERE Cedula=?", (cedula,))
    datos_base = cursor.fetchall()
    cursor.close()
    return datos_base
    
    
def crear_pdf( ruta_salida,cedula):
  
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    print("Fecha actual:", fecha_formateada)
    if fecha_formateada:
       
        datos_base = recuperar_datos_bd(cedula)       
        for dato in datos_base :
          nombre = dato[0]
          apellido = dato[1]
          direccion = dato[2]
          telefono = dato[3]
          contexto = dato[4]
        
        
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
      h2 {{
        text-align: center;
        line-height: 0.4;
      }}
      .container-fecha {{
        width: 90%;
        margin-left:20px;
      }}
      .fecha {{
        margin-left:20px;
        text-align: end;
        font-size: 18px;
      }}
      .titulo {{
        text-align: center;
        line-height: 0.4;
      }}
      .container-historia-clinica {{
        width: 90%;
      }}
      .history-clinic {{
        text-align: end;
      }}
      .container {{
        margin-left: 10%;
      }}
      .container-telefonoOcupacion {{
        display: flex;
        margin: 0 auto;
      }}
      .estado-salud {{
        text-decoration: underline;
        font-weight: bolder;
      }}
      .container-hipertenso {{
        display: flex;
      }}
      .si-hipertenso,
      .si-trastorno,
      .si-diabetes {{
        margin-left: 10px;
      }}
      .controlado {{
        margin-left: 50px;
      }}
      .no-hipertenso,
      .no-trastorno,
      .no-diabetes {{
        margin-left: 10px;
      }}
      .container-trastornos,
      .container-diabetes {{
        display: flex;
      }}
      .container-precio,
      .container-total {{
        display: flex;
      }}
      .container-total {{
        width: 70%;
      }}
      .totalBs {{
        margin-left: 86%;
        font-weight: bolder;
      }}
      .total {{
        margin-left: 500%;
        font-weight: bolder;
      }}
      .firma {{
        line-height: 0.5;
        margin-left: 28%;
      }}
      .container-tabla {{
        max-width: 800px;
        margin: 0 auto;
        margin-left: -20px;
        padding: 20px;

        border-radius: 8px;
      }}

      table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
      }}

      th,
      td {{
        border: 1px solid #ddd;
        padding: 8px;
        text-align: left;
      }}
      .footer{{
        text-decoration: overline;
        font-size: 15px;
      }}
    </style>
    </head>
    <body>
      <h2>Od.José R. Fernández R.</h2>
    <h2>Odontología General e Infantil</h2>
    <div class="container-fecha">
      <p class="fecha">Fecha :{fecha_formateada} </p>
    </div>

    <p class="titulo">Prótesis Fijas, Totales y Removibles,</p>
    <p class="titulo">Tratamientos de Conductos, Cirugías,</p>
    <p class="titulo">Restauraciones Estéticas y Rx.</p>
    <div class="container-historia-clinica">
      <p class="history-clinic">HISTORIA CLINICA :</p>
    </div>

    <div class="container">
      <p class="name">Nombres y Apellidos :<strong>{nombre} {apellido} </strong>
      
      </p>

      <p>Direccion: <strong>{direccion} </strong></p>

      <div class="container-telefonoOcupacion">
        <p>Telefono :<strong>{telefono} </strong>  </p>
        
       
      </div>
      <div class="container-telefonoOcupacion">
       <p>Ocupacion:___________________________</p>
      </div>

      <p>MOTIVO DE CONSULTA: <strong>{contexto} </strong> </p>

      <p class="estado-salud">ESTADO DE SALUD GENERAL.</p>

      <div class="container-hipertenso">
        <p>Hipertenso :</p>
        <p class="si-hipertenso">Si ____</p>
        <p class="no-hipertenso">No ____</p>
        <p class="controlado">
          Controlado :____________________________________
        </p>
      </div>
      <div class="container-trastornos">
        <p>Trastornos de Coagulación :</p>
        <p class="si-trastorno">Si_______</p>
        <p class="no-trastorno">No______</p>
      </div>
      <div class="container-diabetes">
        <p>Diabetes :</p>
        <p class="si-diabetes">Si_______</p>
        <p class="no-diabetes">No______</p>
        <p class="controlado">Controlado_________</p>
      </div>
      <p>Otros : ________________________________________</p>
      <p>Alergías y Habitos</p>

      <p>
        ________________________________________________________________________________________
      </p>
      <p>
        ________________________________________________________________________________________
      </p>
      <p>
        ________________________________________________________________________________________
      </p>

      <p>Diagnostico</p>
      <p>
        ________________________________________________________________________________________
      </p>

      <p>
        ________________________________________________________________________________________
      </p>
      <p>Plan de Tratamiento y Costo</p>
      <div class="container-precio">
        <p>
          ____________________________________________________________________________________
        </p>
        <p>Bs ____</p>
      </div>
      <div class="container-precio">
        <p>
          ____________________________________________________________________________________
        </p>
        <p>Bs ____</p>
      </div>
      <div class="container-precio">
        <p>
          ____________________________________________________________________________________
        </p>
        <p>Bs ____</p>
      </div>
      <div class="container-total">
        <div class="div-strong">
          <p class="total">TOTAL</p>
        </div>

        <p class="totalBs">Bs________</p>
      </div>
      <div class="container-firma">
        <p class="firma">______________</p>
        <p class="firma">Firma Paciente</p>
      </div>
      <div class="container-tabla">
        <h4>CURSO DE TRATAMIENTO</h4>

        <table>
          <tr>
            <th>Fecha</th>
            <th>Tratamientos Realizados</th>
          </tr>
          <tr>
            <td>2023-11-18</td>
            <td>Tratamiento A</td>
          </tr>
          <tr>
            <td>2023-11-19</td>
            <td>Tratamiento B</td>
          </tr>
          <!-- Agrega más filas según sea necesario -->
        </table>
      </div>

      <div class="container-tabla">
        <h4>ESTADO DE CUENTA</h4>

        <table>
          <tr>
            <th>Fecha</th>
            <th>Tratamientos Realizados</th>
            <th>Abono</th>
            <th>Saldo</th>
          </tr>
          <tr>
            <td>2023-11-18</td>
            <td>Tratamiento A</td>
            <td>20$</td>
            <td>10$</td>
          </tr>
          <tr>
            <td>2023-11-19</td>
            <td>Tratamiento B</td>
            <td>20$</td>
            <td>50$</td>
          </tr>
          <!-- Agrega más filas según sea necesario -->
        </table>
      </div>

      <footer>
        <p class="footer"> 
            Av 5 de Julio Edif.Don Gregorio Piso1 Consultorio 1-3,Puerto La Cruz,Estado Anzoategui Telef 0281-9961504
        </p>
      </footer>
    </div>
    </body>
    </html>
    
    """

    HTML(string=html).write_pdf(ruta_salida)

if __name__ == "__main__":
    # Obtén tus datos desde la base de datos
   
    # Llamada a la función con tus datos y ruta de salida
    ruta_salida = '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/waos.pdf'
    cedula = '31112639'
    crear_pdf( ruta_salida=ruta_salida,cedula=cedula)
