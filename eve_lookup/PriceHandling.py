import xml.etree.ElementTree as ET
from requests import get

def retrieve_xml(itemid, system):
    """
    Main driving function of the project. Retrieves the XML (to be parsed) for
    itemid, which can be located on eve-central; and the system (currently 
    restrained to the four main trading hubs).
    """
    systems = {"Jita": 30000142, "Rens": 30002510, "Dodixie": 30002659, 
               "Amarr": 30002187}
    
    ec_url = "http://api.eve-central.com/api/marketstat?typeid={}".format(itemid)
    
    xml_data = []
        
    if system is list:
        urls = []
        for key in system:
            _url = ec_url + "&usesystem={}".format(systems.get(key))
            urls.append(_url)
    else:
        urls = ec_url + "&usesystem={}".format(systems.get(system))
    
    if urls is not list:
        return get(urls)

    for url in urls:
        if type(urls) is not list:
            print url
            url_open = get(url)
        else:
            pass 
            # There should be an error of sorts here.
            # If the sub-url is a list, there is an error somewhere
        xml_data.append(url_open)
        
    return xml_data

def parse_system_prices(xml_tree, xpath):
    return xml_tree[0][0].find('buy').find('max').text
        

def item_price(itemid, system):
    """
    The function to be called!
    
    itemid is the item id from eve-central.
    system is the system, again restrained to the four main trading hubs.
    """

    if isinstance(system, list):
        xml_data = retrieve_xml(itemid, system[0])
    else:
        xml_data = retrieve_xml(itemid, system)
    for element in xml_data:
        root = ET.fromstring(xml_data.text)
        prices = float(parse_system_prices(root, [("buy", "max"), ("sell", "min")]))
        return prices
