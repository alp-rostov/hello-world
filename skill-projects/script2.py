# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "@:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
#
# for event in events:
#     event_obj = Event(timestamp=event.get("timestamp"),
# 	              event_type=event.get("type"),
# 		      session_id=event.get("session_id"))
#     print(event_obj.timestamp)


class Human:
    age=None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if 120 > age > 0 and isinstance ( age,
                                    int ):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age


h = Human ( )
h.set_age ( 119 )
print ( h.get_age ( ) )
