from requests import get
import xml.etree.cElementTree as ET


def player_lookup(key_id, vCode):
    url_base = "https://api.eveonline.com/"
    char_param = "char/CharacterSheet.xml.aspx?keyID={}" \
                 "&vCode={}".format(key_id, vCode)
    stand_param = "corp/Standings.xml.aspx?keyID={}" \
                  "&vCode={}".format(key_id, vCode)
    typeIDs = [16622, 3446]  # Accounting then Broker Relations
    
    url = url_base + char_param

    r = get(url)
    root = ET.fromstring(r.text)
    result = root.findall('result/rowset[@name="skills"]/row'
                          '[@typeID="3446"]')[0].attrib['level']

    print result


class PlayerStats:
    """
    Class operating as a container for player statistics, such as: corporation
    standing, accounting skill level, &c.
    TODO: Add EVE API lookup.
    """
    def __init__(self, corp_stand, fact_stand, relations, accounting):
        self.corp_stand = corp_stand
        self.fact_stand = fact_stand
        self.relations = relations
        self.acctng = accounting

if __name__ == "__main__":
    player_lookup(1, "111")
