

class PlayerStats:
    """
    Class operating as a container for player statistics, such as: corporation
    standing, accounting skill level, &c.
    
    TODO: Add EVE API lookup.
    """
    
    def __init__(self, corp_stand, fact_stand, relations, accounting):
        self.corp_stand = corp_stand
        self.fact_stand = fact_stand
        self.relations  = relations
        self.acctng     = accounting      