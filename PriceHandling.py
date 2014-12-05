import os
from xml.etree.ElementTree import ElementTree, fromstring
import urllib2

ip = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', 8080))

def retrieve_xml(itemid, system, *args):
    systems = {"Jita": 30000142, "Rens": 30002510,
                   "Dodixie": 30002659, "Amarr": 30002187}
    xml_data = []
    
    if type(system) is list:
        urls = []
        for key, systemid in systems.iteritems():
            print systemid
            urls.append("http://api.eve-central.com/api/marketstat?typeid={}&usesystem={}".format(itemid, systemid))
    else:
        urls = "http://api.eve-central.com/api/marketstat?typeid={}&usesystem={}".format(itemid, systems.get(system))
    
    url_data = urllib2.urlopen(urls)
    for line in url_data:
        xml_data.append(line)
    
    return ElementTree(fromstring("".join(xml_data)))

def parse_system_prices(xml_tree, xpath):
    if type(xml_tree) is list:
        pass
    else:
        root = xml_tree.getroot()[0][0]
        buymax = root.find("buy").find("max").text
        sellmin = root.find("sell").find("min").text

        return (buymax, sellmin)

retrieve_xml(34, ["Jita", "Rens"])

#print parse_prices(retrieve_xml(34, "Jita"), "//buy/max")