from abc import ABC, abstractmethod

from exchange import Exchange


class TradingBot(ABC):
    def __init__(self,exchange :Exchange):
        self.exchange = exchange

    @abstractmethod
    def should_buy(self, symbol :str)->bool:
        """Logic for Bot to buy or not"""
    @abstractmethod
    def should_sell(self, symbol :str)->bool:
        """Logic for Bot to sell or not"""