# from minmax_trading_bot import should_buy_avg, should_sell_avg
from avg_trading_bot import should_buy_avg, should_sell_avg
from binance import Binance
from trading import run_bot


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    # create the exchange
    exchange = Binance()

    #use the run_bot to delegate execution
    run_bot(get_prices=exchange.get_prices,
            should_buy=should_buy_avg,
            should_sell=should_sell_avg,
            buy=exchange.buy,
            sell=exchange.sell,
            symbol=symbol,
            trade_amount=trade_amount
    )


if __name__ == "__main__":
    main()
