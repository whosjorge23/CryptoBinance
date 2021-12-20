import time
import ccxt
from datetime import datetime
import pytz

def ask_last_price():
    
    store_crypto_prices = open('store_crypto_prices.txt', 'a')

    tz_User = pytz.timezone('Europe/Rome')
    datetime_User = datetime.now(tz_User)
    date_User = datetime_User.strftime("%H:%M:%S")
    time_User = datetime_User.strftime("%H:%M:%S")
    #print("Rome time:", datetime_Rome.strftime("%H:%M:%S"))

    exchange = ccxt.binance({'enableRateLimit':True})
    crypto = input('type the crypto code: ').upper()
    last_price = exchange.fetchTicker(f'{crypto}USDT')['last']
    last_price_eur = exchange.fetchTicker(f'{crypto}EUR')['last']
    return_str = f'The last {crypto} price is: ${last_price}/€{last_price_eur} in date {date_User} at {time_User}'
    print(return_str)
    store_crypto_prices.write(f'{return_str}\n')


ask_last_price()