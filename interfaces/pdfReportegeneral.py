from weasyprint import HTML
import os
import base64
import sqlite3
from datetime import datetime


def recuperardatos_Doctor(id_user):
    conexion = sqlite3.connect("interfaces/database.db")
    cursor = conexion.cursor()
    cursor.execute("""
                            SELECT 
          
                                  Users.Nombres as Nombre_usuario,
                                  Users.Apellidos as Apellido_doctor, 
                                  Pacientes.Cedula, 
                                  Pacientes.Nombre, 
                                  Pacientes.Apellido, 
                                  Pacientes.Edad, 
                                  Pacientes.Direccion, 
                                  Pacientes.Sexo, 
                                  Pacientes.Fecha_Diagnotico
                            FROM 
                                Pacientes
                            INNER JOIN 
                                Users ON Pacientes.ID_user = Users.ID
                            WHERE 
                                Users.ID = ?
                            ORDER BY 
                                Pacientes.Fecha_Diagnotico ASC
                        """,(id_user,))
    datos_base = cursor.fetchall()
    cursor.close()
    return datos_base if datos_base else None

def recuperar_datos_bd():
    conexion = sqlite3.connect("interfaces/database.db")
    cursor = conexion.cursor()
    cursor.execute("""
                            SELECT 
          
                                  Users.Nombres as Nombre_usuario,
                                  Users.Apellidos as Apellido_doctor, 
                                  Pacientes.Cedula, 
                                  Pacientes.Nombre, 
                                  Pacientes.Apellido, 
                                  Pacientes.Edad, 
                                  Pacientes.Direccion, 
                                  Pacientes.Sexo, 
                                  Pacientes.Fecha_Diagnotico
                            FROM 
                                Pacientes
                            INNER JOIN 
                                Users ON Pacientes.ID_user = Users.ID
                            ORDER BY 
                                Pacientes.Fecha_Diagnotico ASC
                        """)
    datos_base = cursor.fetchall()
    cursor.close()
    return datos_base if datos_base else None
    
    
def crear_pdf(ruta_salida,datos):
  
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    print("Fecha actual:", fecha_formateada)
    datos_base = None
    
    if datos:
      datos_base = datos

        
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
   </head>
<body>
    <style>h3{{
        text-align: center;
        font-size:16px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }}

    th, td {{
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
        font-size: 10px;
        line-height: 1.2;
        text-align: center;
    }}
    p{{
        text-align: end;
        margin-top: -20px;
        font-size:12px;
    }}
    
    </style>
    
    <h3>
        Pacientes Registrados
    </h3>
    <p>Fecha de Impresión: <strong>{fecha_formateada}</strong></p>

    <table>
        <thead>
            <tr>
                <th>Nombre del Doctor</th>
                <th>Apellido del Doctor</th>
                <th>Cedula del Paciente</th>
                <th>Nombre del Paciente</th>
                <th>Apellido del Paciente</th>
                <th>Edad del Paciente</th>
                <th>Direccion del Paciente</th>
                <th>Sexo del Paciente</th>
                
                <th>Fecha del Diagnostico</th>
            </tr>
        </thead>
        <tbody>
        """
    for dato in datos_base:
      html += "<tr>"
      for valor in dato:
          html += f"<td>{valor}</td>"
      html += "</tr>"

# Cerrar la estructura HTML
    html += """
        </tbody>
    </table>


    </body>
    </html>
    
    """

    HTML(string=html).write_pdf(ruta_salida)

if __name__ == "__main__":
    # Obtén tus datos desde la base de datos
   
    # Llamada a la función con tus datos y ruta de salida
    ruta_salida = '/home/reinaldo/Documentos/dev/App-Consultas-y-Historias-Medicas/interfaces/waos.pdf'
    cedula = '31112639'
    crear_pdf(ruta_salida=ruta_salida)
