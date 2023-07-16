
from exchange import Exchange


def should_buy_minmax(exchange : Exchange, symbol: str) -> bool:
    prices =exchange.get_prices(symbol)
    return prices[-1] < 32_000_00

def should_sell_minmax(exchange : Exchange,  symbol: str) -> bool:
    prices =exchange.get_prices(symbol)
    return prices[-1] > 33_000_00