from coinbase import Coinbase
from minmax_trading_bot import should_buy_minmax, should_sell_minmax


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    # create the exchange
    exchange = Coinbase()

    #create the speicific trading bot
    should_buy = should_buy_minmax(exchange=exchange, symbol= symbol)
    should_sell = should_sell_minmax(exchange=exchange, symbol= symbol)

    if should_buy: 
        exchange.buy(symbol, trade_amount)
    elif should_sell: 
        exchange.sell(symbol, trade_amount)
    else : 
        print("no action needed")


if __name__ == "__main__":
    main()
