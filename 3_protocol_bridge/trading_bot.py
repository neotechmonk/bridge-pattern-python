
from typing import Protocol


class TradingBot(Protocol):

    def should_buy(self, symbol :str)->bool:
        """Logic for Bot to buy or not"""

    def should_sell(self, symbol :str)->bool:
        """Logic for Bot to sell or not"""