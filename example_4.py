# Ответы сервера при GET запросе

import requests

response = requests.get('https://www.google.com/')

print(response.status_code)

print(response.headers)

print(response.text)
