from avg_trading_bot import AvgTradingBot
from coinbase import Coinbase


def main() -> None:
    # symbol we trade on
    symbol = "BTC/USD"
    trade_amount = 10

    # create the exchange
    exchange = Coinbase()

    #create the speicific trading bot
    trading_bot = AvgTradingBot(exchange = exchange)
    should_buy = trading_bot.should_buy(symbol= symbol)
    should_sell = trading_bot.should_sell(symbol= symbol)

    if should_buy: 
        exchange.buy(symbol, trade_amount)
    elif should_sell: 
        exchange.sell(symbol, trade_amount)
    else : 
        print("no action needed")


if __name__ == "__main__":
    main()
