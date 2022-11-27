from flask import Flask, request, Response
import time

PATH_TO_TEST_IMAGES_DIR = './subidos'
app = Flask(__name__)

@app.route('/')
def index():
    return Response(open('page.html').read(), mimetype="text/html")

@app.route('/upload', methods=['POST'])
def image():
    variable = request.form.get("Nombre")
    print("Variable Nombre: "+variable)
    file = request.files['Archivo']
    if file.filename != '':
        nuevonombre = ('%s.jpeg' % time.strftime("%Y%m%d-%H%M%S"))
        file.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, nuevonombre))
        print("Subida Completada "+nuevonombre)
        return Response("Variable Nombre: "+variable+" \n<br>Subida Completada "+nuevonombre)
    else:
        print("Error al obtener el archivo del cliente")
        return Response("Variable Nombre: "+variable+" \n<br>Error al obtener el archivo el servidor")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
