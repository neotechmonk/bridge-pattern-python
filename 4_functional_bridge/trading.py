from typing import Callable

""" 
    @param : symobol
    #returns : list of prices
""" 
GetPricesFunction = Callable[[str],list[int]]
