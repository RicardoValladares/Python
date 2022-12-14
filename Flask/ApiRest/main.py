import json
import requests
from datetime import timedelta
from flask_basicauth import BasicAuth
from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'usuario'
app.config['BASIC_AUTH_PASSWORD'] = 'contrasenia'
basic_auth = BasicAuth(app)
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=15)
jwt = JWTManager(app)


@app.route("/")
def Test():
    try:
        base_url = "http://127.0.0.1:5002/"
        url = base_url + "ObtenerToken"
        headers = {
            'Authorization':  "Basic dXN1YXJpbzpjb250cmFzZW5pYQ=="
        }
        response = requests.request("POST", url, headers=headers)
        data = response.json()
        token = data['access_token']
        url = base_url + "ServicioConToken"
        headers = {
            'Authorization':  "Bearer "+token,
            'Content-Type':  "application/json"
        }
        body = {
            'Nombre': 'RICARDO',
            'Documentos': [
                {
                    'TipoDocumento': "DUI",
                    'NumeroDocumento': "123456789-0"
                },
                {
                    'TipoDocumento': "PASAPORTE",
                    'NumeroDocumento': "A04566888"
                }
            ]
        }
        payload = json.dumps(body)
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()
    except:
        return jsonify({"Dato": "Error en el test", "Error": 1}), 401


@app.route("/ObtenerToken", methods=["POST", "GET"])
@basic_auth.required
def ObtenerToken():
    access_token = create_access_token(identity=app.config['BASIC_AUTH_USERNAME'])
    return jsonify(access_token=access_token)


@app.route("/ServicioConToken", methods=["POST", "GET"])
@jwt_required()
def ServicioConToken():
    try:
        content = request.json
        respuesta = jsonify({"Dato": "Documento Invalido", "Error": 0})
        for recepcion in content['Documentos']:
            if recepcion['TipoDocumento']=="DUI" and recepcion['NumeroDocumento']=="123456789-0":
                respuesta = jsonify({"Dato": "Documento Valido", "Error": 0})
        return respuesta
    except:
        return jsonify({"Dato": "JSON no valido", "Error": 1}), 401


if __name__ == "__main__":
    #SERVIDOR CON HTTP
    app.run(debug=True, host='0.0.0.0', port=5002)
    #SERVIDOR CON HTTPS
    #app.run(host='0.0.0.0', port=5002, ssl_context=('/etc/letsencrypt/live/apps.localhost.com-0001/fullchain.pem','/etc/letsencrypt/live/apps.localhost.com-0001/privkey.pem'))
    



#EJECUCION NORMAL CON PYTHON
#python main.py
#EJECUCION EN PROCEOS PARALELO
#gunicorn -w 4 -b 0.0.0.0:5002 --log-level=debug main:app --daemon
#EJECUCION EN PROCEOS PARALELO CON CERTIFICADO HTTPS
#gunicorn -w 4 -b 0.0.0.0:5002 --certfile=/etc/letsencrypt/live/apps.localhost.com-0001/fullchain.pem --keyfile=/etc/letsencrypt/live/apps.localhost.com-0001/privkey.pem --log-level=debug main:app --daemon
