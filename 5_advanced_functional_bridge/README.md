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


