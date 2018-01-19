# bot.py


import requests
import json
import time


if __name__ == '__main__':
    with open('pair.txt') as myfile:
        lines = myfile.readlines()
        for idx, line, in enumerate(lines):
            # 0: index, -1: pair
            cols = line.split(',')
            pair = cols[-2]

            # 0: coin, 1: market
            pair_info= pair.split('/')
            coin = pair_info[0]
            market = pair_info[1]

'''
url = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/1?code=CRIX.UPBIT.KRW-BTC'.format(market, coin)
[{"code":"CRIX.UPBIT.KRW-BTC","candleDateTime":"2018-01-19T11:36:00+00:00","candleDateTimeKst":"2018-01-19T20:36:00+09:00","openingPrice":14884000.00000000,"highPrice":14890000.00000000,"lowPrice":14874000.0,"tradePrice":14874000.0,"candleAccTradeVolume":15.35527905,"candleAccT
'''
