Bridge design pattern aims to allow different concepts to be interacting each other through abstraction

In this example there are two concepts
1. Trading Exchange - get price feed, buy, sell
1. Trading Bot - decide on buy/sell and interact with Trading Exchange

### Organisation 
Complexity of the conceptual application is contained in different folders and x increases using `x_concept` convention 
