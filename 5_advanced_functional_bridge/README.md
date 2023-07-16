TradingBot and Exchange and its concrete implementations are could be coverted into functions. 

Logically, the classes are best reserved for situations where a lot of instances of something needs to be created. They are also used to group like behaviours and state together. This premise is ignore in the attempt to convert these classes into functions. 



Implications of this model
* its possible to add any number of exchanges matching the syntax of  `Exchange`
* its possible to add any number of trading bots matching the syntax of `TradingBot`
* more importantly the, `Protocol` classes now remove the coupling present with the `ABC` classes
* `Protocols` do not have instance variables. Considering `TradingBot` needs access to the `Exchange`, it needs to be dealt with differently. This is achived by keeping the `Exchange` as an instance variable in the sub classes, `AvgTradingBot` and `MinMaxTradingBot`. It could be argued that this is somewhat a duplication.



## Some noteworthy changes
passing of `exchange` is an example of inappririate intimacy. `should_buy_avg` only requires the price feeb hence it could just be provided a function or paramter that provides just that 
```python
def should_buy_avg(exchange :Exchange, symbol: str) -> bool:
    prices = exchange.get_prices(symbol)
    list_window = prices[-3:]
    return prices[-1] < statistics.mean(list_window)
```

the below just does that. When calling `should_buy`, `exchage.get_prices()` could passed as it matching the method signature of `GetPricesFunction`

```python

GetPricesFunction = Callable[[str], List[int]]
def should_buy(get_prices : GetPricesFunction, symbol: str) -> bool:
    prices = get_prices(symbol)
    list_window = prices[-3:]
    return prices[-1] < statistics.mean(list_window)
```