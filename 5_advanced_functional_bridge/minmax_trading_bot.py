from exchange import Exchange
from trading import GetPricesFunction


def should_buy_minmax(get_prices : GetPricesFunction,  symbol: str) -> bool:
    prices =get_prices(symbol)
    return prices[-1] < 32_000_00

def should_sell_minmax(get_prices : GetPricesFunction,   symbol: str) -> bool:
    prices =get_prices(symbol)
    return prices[-1] > 33_000_00