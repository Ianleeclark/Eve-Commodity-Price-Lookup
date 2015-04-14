from price_handling import item_price
from math import e as e_const
import player_stats

def shipping_cost(shipping):
    origin, destination = shipping[0], shipping[1]
    s = {'Jita': 0, 'Rens': 1, 'Dod': 2, 'Amarr': 3}
    #               Jita      Rens      Dod        Amarr  
    cost_matrix = [[0       , 26500000, 16500000, 10500000],
                   [26500000, 0       , 15500000, 21500000],
                   [16500000, 15500000, 0       , 17500000],
                   [10500000, 21500000, 17500000, 0]]

    return cost_matrix[s[origin]][s[destination]]

def transaction_tax(buy_price, origin, player_stats):
    p = player_stats
    corp = p.key_lookup(origin, 0)
    fact = p.key_lookup(origin, 1)

    broker_fee  = (buy_price * ((.01 - p.relations * 0.0005) / 
                  (e_const ** (p.standings[corp] * 0.1 + p.standings[fact] * 0.04))))
    sales_tax   = (buy_price * (.015 - (.0015 * 4)))
    
    return sales_tax + broker_fee

def total_cost(buy_price, shipping, player_stats=None):
    if shipping[0] == shipping[1]:
        return buy_price + transaction_tax(buy_price, shipping[0], player_stats)
    
    return int(buy_price) + shipping_cost(shipping) + transaction_tax(buy_price,
                                                                 shipping[0],
                                                                 player_stats)

def calculate_profit(price, shipping, player_stats):
    cost = total_cost(price, shipping, player_stats)
    return price - cost
    
if __name__ == "__main__":
    shipping = ['Jita', 'Amarr']
    player_stats = PlayerStats.PlayerStats(1, "1111" )
    price = item_price(17736, ["Jita", "Amarr"])
    print calculate_profit(price, shipping, player_stats)
