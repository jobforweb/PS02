# POST запросы

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "тестовый пост запрос",
    "body" : "тестовый контент POST запроса",
    "userid" : 2
}

response = requests.post(url, data=data)

print(response.status_code)

print(f"Ответ: {response.json()}")

# Ответ от Сервера:
# 201
# Ответ: {'title': 'тестовый пост запрос', 'body': 'тестовый контент POST запроса', 'userid': '2', 'id': 101}

