# Попробуем получать не всю запрашиваемую страницу, а что-то более конкретное

import requests
import pprint

# Параметры запроса
params = {
    'q' : 'python'
}

# Запрос с параметрами
response = requests.get('https://api.github.com/search/repositories',params=params)

response_json = response.json()

# Ответ с форматированным JSON
# pprint.pprint(response_json)

print(f"Количество репозиториев: {response_json['total_count']}")