TradingBot and Exchange and its concrete implementations are could be coverted into functions. 

Logically, the classes are best reserved for situations where a lot of instances of something needs to be created. They are also used to group like behaviours and state together. This premise is ignore in the attempt to convert these classes into functions. 



Implications of this model
* its possible to add any number of exchanges matching the syntax of  `Exchange`
* its possible to add any number of trading bots matching the syntax of `TradingBot`
* more importantly the, `Protocol` classes now remove the coupling present with the `ABC` classes
* `Protocols` do not have instance variables. Considering `TradingBot` needs access to the `Exchange`, it needs to be dealt with differently. This is achived by keeping the `Exchange` as an instance variable in the sub classes, `AvgTradingBot` and `MinMaxTradingBot`. It could be argued that this is somewhat a duplication.