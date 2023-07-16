`run_bot()` is introduced as a layer of abstraction 
This is called from the `main()`

run_bot is incrementally refactored to remove dependency on `symbol` and `trade_amount`

This makse the `run_bot()` login simple to understand

the logic is reduced to the following
```pseudocode
buy IF should_buy
sell IF should_sell
```


to be able to derive this simplicity, partial functions are introduced in `main()`


Implications of this model
* all aspects of the code could be substituted with functions which pure, making them easy to stub and test
* abstractions introduced to reduce dependency by limiting to the bare minimum requirements
* partial functions are used to port gap between simple `run_bot()`, exchange and trading strategy



### Noteworthy observations

Given `symbol` and `trade_amount` are not part of the control flow, they are not found to be relevant to the function `run_bot() `
```python
def run_bot(
        get_prices : GetPricesFunction,
        should_buy : DecideFunction, 
        should_sell : DecideFunction, 
        buy : BuySellFunction,
        sell : BuySellFunction,
        symbol : str,
        trade_amount : int
):
    if should_buy (symbol, get_prices):
        buy(symbol, trade_amount)
    elif should_sell (symbol, get_prices):
        sell(symbol, trade_amount)
    else : 
        print('not action to take')
```

This is used to inform the below simplification 

```python 

def run_bot(
        should_buy : DecideFunction, 
        should_sell : DecideFunction, 
        buy : BuySellFunction,
        sell : BuySellFunction
):
    if should_buy ( ):
        buy( )
    elif should_sell ( ):
        sell()
    else : 
        print('not action to take')
        ```