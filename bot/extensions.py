import json
import requests
from config import exch

class ApiExp(Exception):
    pass

class converter():
    @staticmethod
    def get_price(base, quote, amount):

        try:
            amount_ = float ( amount )
        except ValueError:
            raise ApiExp (f'Не удалось обработать количество: {amount}' )

        try:
            base_=exch[base.lower()]
        except KeyError:
            raise ApiExp ( f'Не удалось обработать валюту: {base}' )

        try:
            quote_=exch[quote.lower()]
        except KeyError:
            raise ApiExp ( f'Не удалось обработать валюту: {quote}' )

        if base_ == quote_:
            raise ApiExp ( f'Указаны одинаковые валюты: {base}' )

        r = requests.get ( f'https://min-api.cryptocompare.com/data/price?fsym={base_}&tsyms={quote_}' )
        resp = json.loads ( r.content )
        summa=round(float ( resp[quote_] ) * amount_, 2)
        return f'Результат конвертации: {amount_} {base_} = {summa} {quote_}'




