# Сергей Иванов, 9 когорта - Финальный проект. Инженер по тестированию Плюс.

import configuration
import requests
import data

# Создаём новый заказ
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body,
                         headers=data.headers)

# Получаем номер трека заказа
def get_track_number():
    response_new_order = post_new_order(data.new_order)
    track_number = response_new_order.json()["track"]
    return str(track_number)

