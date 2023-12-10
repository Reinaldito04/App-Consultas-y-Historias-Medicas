from weasyprint import HTML
import os
import base64
import sqlite3
from datetime import datetime


def recuperar_datos_bd(cedula):
    conexion = sqlite3.connect("interfaces/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT Nombre, Apellido, Direccion, Telefono, context,Hipertension,Diabates,Coagualcion,Alergias,Otros,hipertension_Data,diabate_Data,Diagnotico FROM Pacientes WHERE Cedula=?", (cedula,))
    datos_base = cursor.fetchall()
    cursor.close()
    return datos_base
    
    
def obtener_codigo_base64(ruta_imagen):
    with open(ruta_imagen, "rb") as image_file:
        codigo_base64 = base64.b64encode(image_file.read()).decode("utf-8")
    return codigo_base64
def crear_pdf( ruta_salida,cedula,tratamientos,precioTotal,cursoTratamiento):
   
    rutaImagen = "interfaces/ELEMENTOS GRAFICOS/logo.png"
    codigo_base64 = obtener_codigo_base64(rutaImagen)
    imagenDoctor = "interfaces/ELEMENTOS GRAFICOS/OCLUSAL.jpg"
    
    codigo_base64Doctor = obtener_codigo_base64(imagenDoctor)
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    print("Fecha actual:", fecha_formateada)
    if fecha_formateada:
        conexion = sqlite3.connect("interfaces/database.db")
        cursor = conexion.cursor()
        cursor.execute ("SELECT Tratamiento1,Tratamiento2,Tratamiento3,Tratamiento4,Tratamiento5,Tratamiento6 FROM PTrata WHERE Cedula =?",(cedula,))
        
        resultado_tratamientos = cursor.fetchall()
        cursor.execute("SELECT Fecha_Trata FROM PTrata WHERE Cedula=?",(cedula,))
        fecha_tratamiento = cursor.fetchone()
        TotalPrecio = precioTotal
        datos_base = recuperar_datos_bd(cedula)       
        for dato in datos_base :
          nombre = dato[0]
          apellido = dato[1]
          direccion = dato[2]
          telefono = dato[3]
          contexto = dato[4]
          hipertension = dato[5]
          diabetes = dato[6]
          coalguacion = dato[7]
          alergias = dato[8]
          otros = dato[9]
          hiperetensiondata = dato[10]
          diabetedata= dato[11]
          diagnostico =dato[12]
          
          if diabetes =="Si":
            valordiabetes = "Si"
          elif diabetes =="No":
            valordiabetes="No"
            
          if coalguacion =="Si":
            valorCoalgu ="Si"
          elif coalguacion =="No":
            valorCoalgu="No"
          if hipertension=="Si":
            valorHiperetnion = "Si"
          elif hipertension =="No":
            valorHiperetnion ="No"

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
        text-align:center;
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
        font-size: 10px;
      }}
      .img-logo{{
        width:80px;
        height:80px;
      }}
      .container-img{{
        display:flex;
        justify-content:center;
        align-items: center;
       
        
      }}
      .doctor-img{{
        width:500px;

      }}
    </style>
    </head>
    <body>
    <img src="data:image/png;base64,{codigo_base64}" class="img-logo">
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
    <p> Cedula : <strong>{cedula} </strong></p>
      <p class="name">Nombres y Apellidos :<strong>{nombre} {apellido} </strong>
      
      </p>

      <p>Direccion: <strong>{direccion} </strong></p>

      <div class="container-telefonoOcupacion">
        <p>Telefono :<strong>{telefono} </strong>  </p>
        
       
      </div>
     

      <p>MOTIVO DE CONSULTA: <strong>{contexto} </strong> </p>

      <p class="estado-salud">ESTADO DE SALUD GENERAL.</p>

      <div class="container-hipertenso">
        <p>Hipertenso :</p>
        <p class="si-hipertenso">{valorHiperetnion}</p>
     
        <p class="controlado">
          Controlado : {hiperetensiondata}
        </p>
      </div>
      <div class="container-trastornos">
        <p>Trastornos de Coagulación :</p>
        <p class="si-trastorno">{valorCoalgu}</p>
      
      </div>
      <div class="container-diabetes">
        <p>Diabetes :</p>
        <p class="si-diabetes">{valordiabetes}</p>
        
        <p class="controlado">Controlado : {diabetedata}</p>
      </div>
      
      <p class="alergias">Alergías y Habitos</p>
<style>

.alergias,.diag,.otros{{
  text-decoration:underline;
   font-weight: bolder;
   text-align:center;
}}
.plan{{
  text-decoration:underline;
   font-weight: bolder;
   text-align:center;
}}
</style>
  
      <p>
        {alergias}
      </p>
     <p class="otros">Otros :</p>
      <p>{otros}</p>
      <p class="diag">Diagnostico</p>
      <p>
       {diagnostico}
      </p>

     <div class="container-img">
        <img src="data:image/png;base64,{codigo_base64Doctor}" class="doctor-img">
     </div>
     <style>
      .container-tratamiento{{
         border: 2px solid black;
        margin-bottom: 10px; 
        width: 550px;
       text-align:center;
        
    }}
     .container-precio {{
        display: flex;
        flex-direction: column; /* Muestra los elementos en columna */
        align-items: flex-start; 
        
        }}
     </style>
      <p class="plan">Plan de Tratamiento y Costo</p>
      <table>
      <tr>
        <th>Tratamiento</th>
        <th>Valor </th>
      </tr>
       """

    if tratamientos:
      
        for trato in tratamientos:
          for clave, valor in trato.items():
              html += f"""
              <tr>
                  <td>{clave}</td>
                  <td>{valor}</td>
              </tr>
              """

    html += f"""
      </table>
      <div class="container-total">
        <div class="div-strong">
          <p class="total">TOTAL</p>
        </div>
   
    <p class="totalBs">Bs : {TotalPrecio} </p>
      </div>
      <div class="container-firma">
        <p class="firma">______________</p>
        <p class="firma">Firma Paciente</p>
      </div>
      <div class="container-tabla">
        <h4>CURSO DE TRATAMIENTO</h4>

        <table>
          <tr>
            <th>Numero</th>
             <th>Fecha</th>
            <th>Tratamiento Realizado</th>
          </tr>
         """

    if cursoTratamiento:
      for indice, tratamiento in enumerate(cursoTratamiento, start=1):
          fecha = tratamiento.get('fecha', '')
          valor = tratamiento.get('tratamiento', '')
          if fecha and valor:
            html += f"""
                <tr>
                    <td>{indice}</td>
                    <td>{fecha_formateada}</td>
                    <td>{valor}</td>
                </tr>
            """

    html += """
        </table>
      </div>

   

      <footer>
      
        <p class="footer"> 
            Av 5 de Julio Edif.Virgen Del Valle Piso-3,Puerto La Cruz,Estado Anzoategui Telef 0281-9961504
        </p>
      </footer>
    </div>
    </body>
    </html>
    
    """

    HTML(string=html).write_pdf(ruta_salida)

if __name__ == "__main__":
    # Obtén tus datos desde la base de datos
    tratamientos = [{"Tratamiento 1" : "precio 1",
                      "Tratamiento 2" : "precio 2",
                      "Tratamiento 3" : "precio 3",
                      "Tratamiento 4" : "precio 4"
                         
                        }
                        ]
    # Llamada a la función con tus datos y ruta de salida
    ruta_salida = '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/waos.pdf'
    cedula = '31112639'
    crear_pdf( ruta_salida=ruta_salida,cedula=cedula,tratamientos=tratamientos,precioTotal=20)
