import requests

response = requests.get("https://viacep.com.br/ws//json/")
print('status code', response.statu_code)
data = response.json()
print('dados',data['logradouro',''])