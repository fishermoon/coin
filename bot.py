# bot.py


import requests
import json

markets = {
    'KRW':['BTC', 'ETH', 'XRP'],
    'BTC':['BTC', 'ETH', 'XRP'],
    'ETH':['BTC', 'ETH', 'XRP'],
    'USDT':['BTC', 'ETH', 'XRP']
}

if __name__ == '__main__':
    for market in markets:
        for coin in markets[market]:
            url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-BTC'.format(market, coin)
            print (url)
            r = requests.get(url, auth=('user', 'pass'))
            if r.status_code == 200:
                print (r.status_text)
'''
[{"code":"CRIX.UPBIT.KRW-BTC","candleDateTime":"2018-01-19T11:36:00+00:00","candleDateTimeKst":"2018-01-19T20:36:00+09:00","openingPrice":14884000.00000000,"highPrice":14890000.00000000,"lowPrice":14874000.0,"tradePrice":14874000.0,"candleAccTradeVolume":15.35527905,"candleAccTradePrice":228506807.11562000,"timestamp":1516361810391,"unit":1}]
'''
