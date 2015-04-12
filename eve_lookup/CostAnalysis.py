from PriceHandling import item_price
from math import e as e_const
import PlayerStats

def shipping_cost(shipping):
    origin, destination = shipping[0], shipping[1]
    #               Jita      Rens      Dod        Amarr  
    cost_matrix = [[0       , 26500000, 16500000, 10500000],
                   [26500000, 0       , 15500000, 21500000],
                   [16500000, 15500000, 0       , 17500000],
                   [10500000, 21500000, 17500000, 0]]

    return cost_matrix[origin][destination]


def transaction_tax(buy_price, origin, player_stats):
    """
    Needs to lookup origin within PlayerStats.corp_stand
    and correctly identify Jita:whatever location id
    """
    p = player_stats
    
    broker_fee  = (buy_price * ((.01 - p.relations * 0.0005) / 
                  (e_const**(p.fact_stand[origin] * 0.1 +
                             p.corp_stand[origin] * 0.04))))
    sales_tax   = (buy_price * (.015 - (.0015 * 4)))
    
    return sales_tax + broker_fee

def total_cost(buy_price, shipping, player_stats=None):
    if shipping[0] == shipping[1]:
        return buy_price + transaction_tax(buy_price, None, player_stats)
    
    return buy_price + shipping_cost(shipping) + transaction_tax(buy_price,
                                                                 shipping[0],
                                                                 player_stats)

def calculate_profit(prices, shipping):
    cost = total_cost(prices[0], shipping, player_stats)
    return prices[1] - cost
    
if __name__ == "__main__":
    player_stats = PlayerStats(111, "1111")
    prices = item_price(17736, ["Jita", "Amarr"])
    print calculate_profit(prices, player_stats)
