"""
Задание 2: Параметры запроса
Используйте API, который позволяет фильтрацию данных 
через URL-параметры (например, https://jsonplaceholder.typicode.com/posts).
Отправьте GET-запрос с параметром userId, равным 1.
Распечатайте полученные записи.
"""

import requests
import pprint

# Фильтрация ресурса, типовой запрос:
# https://jsonplaceholder.typicode.com/posts?userId=1
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId" : 1
}

response = requests.get(url,params=params)

#print(response.status_code)

pprint.pprint(response.json())