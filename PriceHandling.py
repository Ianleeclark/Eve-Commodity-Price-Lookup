from xml.etree.ElementTree import ElementTree, fromstring
from urllib2 import urlopen
import os

ip = os.getenv('IP', '0.0.0.0')
port = int(os.getenv('PORT', 8080))

def retrieve_xml(itemid, system, *args):
    systems = {"Jita": 30000142, "Rens": 30002510,
                   "Dodixie": 30002659, "Amarr": 30002187}
    xml_data = []
    url_data = []
    if type(system) is list:
        urls = []
        for key in system:
            urls.append("http://api.eve-central.com/api/marketstat?typeid={}&usesystem={}".format(itemid, systems.get(key)))
    else:
        urls = "http://api.eve-central.com/api/marketstat?typeid={}&usesystem={}".format(itemid, systems.get(system))
    
    for url in urls:
        if type(urls) is not list:
            url_open = urlopen(urls)
        else:
            url_open = urlopen(url)
        _xml_data = []
        for line in url_open:
            _xml_data.append(line)
        xml_data.append("".join(_xml_data))
        
    return xml_data

def parse_system_prices(xml_tree, xpath):
    if type(xml_tree) is list:
        return "Nil"
    else:
        prices = []
        root = xml_tree.getroot()[0][0]
        for path in xpath:
            xpath1 = root.find(xpath[0][0]).find(xpath[0][1]).text
            xpath2 = root.find(xpath[1][0]).find(xpath[1][1]).text
            return (float(xpath1), float(xpath2))

def item_price(itemid, system):
    xml_data = retrieve_xml(itemid, system)
    for element in xml_data:
        ele = ElementTree(fromstring(element))
        prices = parse_system_prices(ele, [("buy", "max"), ("sell", "min")])
        return prices