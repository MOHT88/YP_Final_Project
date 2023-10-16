import requests
import configuration
import request


# Выполняем запрос на получение заказа по треку
def get_order_info(order_track):
   return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO + "?t=" + order_track)


# Выполняем проверку успешного запроса
def test_order_info():
     get_info = get_order_info(request.get_track_number())
     assert get_info.status_code == 200


