from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)


#para usar el comando http instala httpie
#http POST :5002/ObtenerToken username=usuario password=contrasenia
@app.route("/ObtenerToken", methods=["POST"])
def ObtenerToken():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "usuario" or password != "contrasenia":
        return jsonify({"Dato": "No autorizado", "Error": 1}), 401
    else:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)


#para usar el comando http instala httpie
#http GET :5002/ServicioConToken Authorization:"Bearer $JWT" TipoDocumento=DUI NumeroDocumento=123456789-0
@app.route("/ServicioConToken", methods=["GET"])
@jwt_required()
def ServicioConToken():
    try:
        tipo = request.json.get("TipoDocumento", None)
        dui = request.json.get("NumeroDocumento", None)
        if tipo=="DUI" and dui=="123456789-0":
            return jsonify({"Dato": "Documento Valido", "Error": 0})
        else:
            return jsonify({"Dato": "Documento Invalido", "Error": 0})
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
