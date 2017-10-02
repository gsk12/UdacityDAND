# loading libraries
import os
import xml.etree.cElementTree as cET
from collections import defaultdict
import pprint
import re
import codecs
import json
import string
from pymongo import MongoClient

filename = "bangalore.osm" # osm filename
path = "C:\Users\sampa\Desktop\Other\Udacity\Lesson 4" # directory contain the osm file
bangaloreOSM = os.path.join(path, filename)

#  regular expression to check tags that contain ony lowercase are valid, lower case with colon 
#  or with problematic characters otherwise valid
lower = re.compile(r'^([a-z]|_)*$') 
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# expected street names , Halli , nagar, Palya are locally common street names
expected = ["Street", "Avenue", "Halli", "Nagar", "Palya", "Place", "Square", "Lane", "Road"]

def key_type(element, keys):
    if element.tag == "tag":
        for tag in element.iter('tag'):
            k = tag.get('k')
            if lower.search(k):
                keys['lower'] += 1
            elif lower_colon.search(k):
                keys['lower_colon'] += 1
            elif problemchars.search(k):
                keys['problemchars'] += 1
            else:
                keys['other'] += 1
    return keys


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys

ban_keys = process_map(bangaloreOSM)
pprint.pprint(ban_keys)