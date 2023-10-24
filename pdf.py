import  jinja2
import pdfkit

def createPdf(ruta_template ,info ,rutacss =''):
    nombre_template = ruta_template.split('/')[-1]
    ruta_template = ruta_template.replace(nombre_template ,'')
    
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template = env.get_template(nombre_template)
    html = template.render(info)
    options  = {
        'page-size' : 'Letter',
        'margin-top' : '0.05in',
        'margin-right' :'0.05in',
        'margin-bottom' :'0.05in',
        'margin-left' : '0.05in',
        'encoding ' : 'UTF-8'
    }
    config = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    ruta_salida = 'uiPdf/test.pdf'
    pdfkit.from_string(html , ruta_salida , options= options, configuration= config)
    
if __name__ == "__main__":
    ruta_template = 'uiPdf/test.html'
    info = {"cedulaPaciente" : "30433058" ,"Nombre" : "Reinaldo Bellorin"}
    createPdf(ruta_template, info)