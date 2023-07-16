# from minmax_trading_bot import should_buy_avg, should_sell_avg
from functools import partial

from avg_trading_bot import should_buy_avg, should_sell_avg
from coinbase import Coinbase
from trading import run_bot


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10


    # create the exchange
    exchange = Coinbase()

    should_buy_fn = partial(should_buy_avg, symbol=symbol, get_prices=exchange.get_prices)
    should_sell_fn = partial(should_sell_avg, symbol=symbol, get_prices=exchange.get_prices)
    buy_fn = partial(exchange.buy, symbol=symbol, amount = trade_amount)
    sell_fn = partial(exchange.sell, symbol=symbol, amount = trade_amount)

    

    #use the run_bot to delegate execution
    run_bot(
            should_buy=should_buy_fn,
            should_sell=should_sell_fn,
            buy=buy_fn,
            sell=sell_fn
    )


if __name__ == "__main__":
    main()
