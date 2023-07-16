from typing import Callable

""" 
    @param : symbol
    #returns : list of prices
""" 
GetPricesFunction = Callable[[str],list[int]]



""" 
    @param : symobol, fn to get list of prices
    #returns : boolean for buy or sell decision 
""" 
DecideFunction = Callable[[str, GetPricesFunction],bool]

""" 
    @param : symbol, price
    #returns : None
""" 
BuySellFunction = Callable[[str, int],None]


def run_bot(
        get_prices : GetPricesFunction,
        should_buy : DecideFunction, 
        should_sell : DecideFunction, 
        buy : BuySellFunction,
        sell : BuySellFunction,
        symbol : str,
        trade_amount : int
):
    if should_buy (symbol, get_prices):
        buy(symbol, trade_amount)
    elif should_sell (symbol, get_prices):
        sell(symbol, trade_amount)
    else : 
        print('not action to take')