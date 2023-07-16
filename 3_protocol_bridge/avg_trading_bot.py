import statistics

from exchange import Exchange


def should_buy_avg(exchange :Exchange, symbol: str) -> bool:
    prices = exchange.get_prices(symbol)
    list_window = prices[-3:]
    return prices[-1] < statistics.mean(list_window)

def should_sell_avg( exchange :Exchange, symbol: str) -> bool:
    prices =exchange.get_prices(symbol)
    list_window = prices[-3:]
    return prices[-1] > statistics.mean(list_window)
