
### Preintalar Python con los modulos 
```sh
pip install Flask
pip install Flask-JWT-Extended
pip install Flask-BasicAuth
```

### probar la api para obtener el token
```bash
curl --location --request POST "http://127.0.0.1:5002/ObtenerToken" --header "Authorization: Basic dXN1YXJpbzpjb250cmFzZW5pYQ=="
```

### probar la api con el token obtenido
```bash
curl --location --request GET "http://127.0.0.1:5002/ServicioConToken" \ 
--header "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2ODM4NTQyMCwianRpIjoiNzAwNTYyMWItOGI1NC00NjE5LTkzZmEtNWQyNDM4NDM2YTk1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InVzdWFyaW8iLCJuYmYiOjE2NjgzODU0MjAsImV4cCI6MTY2ODM4NjMyMH0.6l1_gnFK99NlSRIKqG6ErLe46mx4ajg14rPiqRPrcTM" \ 
--header "Content-Type: application/json" \ 
--data-raw "{
  \"Nombre\": \"RICARDO\",
  \"Documentos\": [
    {
      \"TipoDocumento\": \"DUI\",
      \"NumeroDocumento\": \"123456789-0\"
    },
    {
      \"TipoDocumento\": \"PASAPORTE\",
      \"NumeroDocumento\": \"A04566888\"
    }
  ] 
}"
```
