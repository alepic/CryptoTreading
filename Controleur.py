from datetime import datetime
import time
import requests
import findPatterns as findPatterns

# in minuts, it can be 30 60 or 90 (90 means 90 or more )
time_from_last_purchase = 90

while True:
    if time_from_last_purchase == 90 :
        anwser = requests.get('https://api.binance.com/api/v1/klines?symbol=ARKBTC&interval=30m&limit=10')
        Candlesticks = [[0]*12 for i in range(0,1000)]
        for i,Candlestick in enumerate(anwser.json()):
            Candlesticks[i][0] = Candlestick[0]
            Candlesticks[i][1] = float(Candlestick[1])
            Candlesticks[i][2] = float(Candlestick[2])
            Candlesticks[i][3] = float(Candlestick[3])
            Candlesticks[i][4] = float(Candlestick[4])
            Candlesticks[i][5] = float(Candlestick[5])
            Candlesticks[i][6] = Candlestick[6]
            Candlesticks[i][7] = float(Candlestick[7])
            Candlesticks[i][8] = Candlestick[8]
            Candlesticks[i][9] = float(Candlestick[9])
            Candlesticks[i][10] = float(Candlestick[10])
            Candlesticks[i][11] = float(Candlestick[11])
        if (findPatterns.test_hammer(Candlesticks) or findPatterns.test_inverted_hammer(Candlesticks) or findPatterns.test_three_white_soldiers(Candlesticks) ):
            time_from_last_purchase = 30
            print ("[{}] buy".format(datetime.now()))
        else:
            print("[{}] wait".format(datetime.now()))
    elif time_from_last_purchase == 60:
        print("[{}] sell".format(datetime.now()))
        time_from_last_purchase += 30
    elif time_from_last_purchase < 60:
        print("[{}] wait".format(datetime.now()))
        time_from_last_purchase += 30

    #wait untile xx:(0/3)0:05 to get new data and comput nex order.
    time.sleep(1805-( datetime.now() - datetime(1970,1,1)).total_seconds()%1800)
    pass
