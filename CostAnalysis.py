from PriceHandling import item_price
from math import e as e_constt

def transaction_tax(buy_price, player_stats):
    p = player_stats
    
    broker_fee  = (buy_price * ((.01 - p.relations * 0.0005) / 
                  (e_const**(p.fact_stand * 0.1 + p.corp_stand * 0.04))))
    sales_tax   = (buy_price * (.015 - (.0015 * 4)))
    
    return sales_tax + broker_fee

def total_cost(buy_price, player_stats=None, shipping=None):
    if shipping is None:
        return buy_price + transaction_tax(buy_price)
    
    # For the time being, we're assuming a Jita origin because it just doesn't 
    # matter for what I'm currently trying to do with the project.
    # However, this will be adjusted later.
    #               Jita      Rens      Dod        Amarr  
    cost_matrix = [0       , 26500000, 16500000, 10500000,
                   26500000, 0       , 15500000, 21500000,
                   16500000, 15500000, 0       , 17500000,
                   10500000, 21500000, 17500000, 0]
    
    temp_cost = {"Jita": 0, "Rens": 26500000,
                 "Dodixie": 16500000, "Amarr": 10500000}
    origin = "Jita"
    shipping_cost = temp_cost.get(shipping[1])
    
    return buy_price + shipping_cost + transaction_tax(buy_price, player_stats)

def calculate_profit(prices, shipping=None):
    cost = total_cost(prices[0], shipping)
    if shipping is None:
        pass
    return prices[1] - cost
    
if __name__ == "__main__":
    player_stats = PlayerStats(1.00, 5.00, 4, 4)
    prices = item_price(17736, "Jita")
    print calculate_profit(prices, player_stats["Jita", "Amarr"])