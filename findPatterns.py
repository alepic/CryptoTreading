#param: Candlestick: 10 Candlestick extracte withe the binance layout
#OutPut: True is ther is a hammer on the 7th Candlestick
def test_hammer(Candlesticks):

    #cheack if their is a downtrend befor the Hammer (oppening < closing_befor_hammer)

    is_a_global_downtrend_befor = Candlesticks[0][1]*0.995>Candlesticks[5][4]

    #cheack if their is a Hammer
    is_a_hammer = ((Candlesticks[6][4] > Candlesticks[6][1])) and ((Candlesticks[6][2]-Candlesticks[6][1])<(Candlesticks[6][1]-Candlesticks[6][3]))


    #cheack if their is a uptrend after the Hammer
    is_a_global_uptrend_after = (Candlesticks[7][1]*1.005<Candlesticks[9][4])

    #cheack if their is an incrised volume after the Hammer
    is_a_incrised_volume_after = Candlesticks[6][5]<Candlesticks[8][5]

    if (is_a_global_downtrend_befor and is_a_hammer and is_a_global_uptrend_after and is_a_global_uptrend_after ):
        return True
    else :
        return False


#param: Candlestick: 10 Candlestick extracte withe the binance layout
#OutPut: True is ther is a Invertied hammer on the 7th Candlestick
def test_inverted_hammer(Candlesticks):

    #cheack if their is a downtrend befor the Hammer (oppening < closing_befor_hammer)

    is_a_global_downtrend_befor = Candlesticks[0][1]*0.995>Candlesticks[5][4]


    #cheack if their is an inverted Hammer
    is_an_inverted_hammer = ((Candlesticks[6][4] > Candlesticks[6][1])) and ((Candlesticks[6][4]-Candlesticks[6][3])<(Candlesticks[6][2]-Candlesticks[6][4]))

    #cheack if their is a uptrend after the Hammer
    is_a_global_uptrend_after = (Candlesticks[7][1]*1.005<Candlesticks[9][4])

    #cheack if their is an incrised volume after the Hammer
    is_a_incrised_volume_after = Candlesticks[6][5]<Candlesticks[8][5]

    if (is_a_global_downtrend_befor and is_an_inverted_hammer and is_a_global_uptrend_after and is_a_global_uptrend_after ):
        return True
    else :
        return False

#param: Candlestick: 10 Candlestick extracte withe the binance layout
#OutPut: True if ther is a three white soldiers pattern on the 8th-10th Candlestick
def test_three_white_soldiers(Candlesticks):

    #cheack if their is a downtrend befor the soldiers (oppening < closing_befor_hammer)

    is_a_global_downtrend_befor = Candlesticks[0][1]*0.995>Candlesticks[6][4]


    #cheack if the 8th is a soldire
    is_soldire_one = (Candlesticks[7][4] > Candlesticks[7][1])
    #cheack if their is a uptrend after the Hammer
    is_soldire_tow = (Candlesticks[8][4] > Candlesticks[8][1])
    #cheack if their is an incrised volume after the Hammer
    is_soldire_three = (Candlesticks[9][4] > Candlesticks[9][1])

    if (is_a_global_downtrend_befor and is_soldire_one and is_soldire_tow and is_soldire_three):
        return True
    else :
        return False

import random

def test_rand():
    return random.randint(0, 1)==1
