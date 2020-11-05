import urllib,json
from urllib import request

url = 'https://jsonplaceholder.typicode.com/todos/1'
response = request.urlopen(url)
datos = json.loads(response.read())

print(datos)