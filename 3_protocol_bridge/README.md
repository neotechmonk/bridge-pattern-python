Abstract classes when implemted by the concrete sub classes, form an 'is-a' relationship
This relationship is the strongest form of coupling.  

The coupling coupling could be broken with `Exchange` as `Protocol`.  `Binance` and `Coinbase` now don't have a relationship with `Exchange` protocol. Instead the abstraction is ahieved through strucural typing.


A similar treatment is applied to the `TradingBot` too

Implications of this model
* its possible to add any number of exchanges matching the syntax of  `Exchange`
* its possible to add any number of trading bots matching the syntax of `TradingBot`
* more importantly the, `Protocol` classes now remove the coupling present with the `ABC` classes
* `Protocols` do not have instance variables. Considering `TradingBot` needs access to the `Exchange`, it needs to be dealt with differently. This is achived by keeping the `Exchange` as an instance variable in the sub classes, `AvgTradingBot` and `MinMaxTradingBot`. It could be argued that this is somewhat a duplication.