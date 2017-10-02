def audit_street_type(street_types, street_name):
    # add unexpected street name to a list
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            
def is_street_name(elem):
    # determine whether a element is a street name
    return (elem.attrib['k'] == "addr:street")

def audit_street(osmfile):
    # iterate through all street name tag under node or way and audit the street name value
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in cET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    return street_types

st_types = audit_street(bangaloreOSM)
# print out unexpected street names
pprint.pprint(dict(st_types))