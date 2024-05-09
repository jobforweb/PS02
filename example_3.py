# Скачаем изображение при помощи get-запроса

import requests

img = "https://hameleone.ru/wp-content/uploads/4/8/1/4812217951a03babc907ef5e2b5c8a8e.jpeg"

response = requests.get(img)

with open("test.jpg", "wb") as file: # wb = write binary
    file.write(response.content)
