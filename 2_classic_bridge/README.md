<abstract> `Excahnge` class is implemented by `Binance` and `Coinbase`

all methods are implemented at the level of the specific excahnges


<abstract> `TradingBot` class is implemented by `AvgTradingBot` and `MinmaxTradingBot`

Implications of this model
* its possible to add any number of exchanges that inherit `Exchange`
* its possible to add any number of trading bots that inherity  `TradingBot`
* more importantly interactions between specific implementation of  `Exchange` and `TradingBot` are only through the abstractions. This increases scalability so long as abstractions are still valid in the future implementations 