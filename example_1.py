# Запрос к базовой странице

import requests
import pprint

# response = requests.get('https://www.google.com/')

response = requests.get('https://api.github.com/')

'''
# Работа со статусом запроса
print(response.status_code)

if response.ok:
    print('Запрос успешно выполнен')
else:
    print('Произошла ощибка')
'''

# Неформатированнный вывод ответа от сервера
# print(response.text)

response_json = response.json()

# Фрматированнный вывод ответа от сервера
pprint.pprint(response_json)