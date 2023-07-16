from typing import Callable

""" 
    @param : symbol
    #returns : list of prices
""" 
GetPricesFunction = Callable[[],list[int]]



""" 
    @param : symobol, fn to get list of prices
    #returns : boolean for buy or sell decision 
""" 
DecideFunction = Callable[[],bool]

""" 
    @param : symbol, price
    #returns : None
""" 
BuySellFunction = Callable[[],None]


def run_bot(
        should_buy : DecideFunction, 
        should_sell : DecideFunction, 
        buy : BuySellFunction,
        sell : BuySellFunction
):
    if should_buy ( ):
        buy( )
    elif should_sell ( ):
        sell()
    else : 
        print('not action to take')