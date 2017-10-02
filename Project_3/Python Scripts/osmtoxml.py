CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):
    node = {}
    node["created"]={}
    node["address"]={}
    node["pos"]=[]
    refs=[]
    
    # we only process the node and way tags
    if element.tag == "node" or element.tag == "way" :
        if "id" in element.attrib:
            node["id"]=element.attrib["id"]
        node["type"]=element.tag

        if "visible" in element.attrib.keys():
            node["visible"]=element.attrib["visible"]
      
        # the key-value pairs with attributes in the CREATED list are added under key "created"
        for elem in CREATED:
            if elem in element.attrib:
                node["created"][elem]=element.attrib[elem]
                
        # attributes for latitude and longitude are added to a "pos" array
        # include latitude value        
        if "lat" in element.attrib:
            node["pos"].append(float(element.attrib["lat"]))
        # include longitude value    
        if "lon" in element.attrib:
            node["pos"].append(float(element.attrib["lon"]))

        
        for tag in element.iter("tag"):
            if not(problemchars.search(tag.attrib['k'])):
                if tag.attrib['k'] == "addr:housenumber":
                    node["address"]["housenumber"]=tag.attrib['v']
                    
                if tag.attrib['k'] == "addr:postcode":
                    node["address"]["postcode"]=tag.attrib['v']
                
                # handling the street attribute, update incorrect names using the strategy developed before   
                if tag.attrib['k'] == "addr:street":
                    node["address"]["street"]=tag.attrib['v']
                    

                if tag.attrib['k'].find("addr")==-1:
                    node[tag.attrib['k']]=tag.attrib['v']
                    
        for nd in element.iter("nd"):
             refs.append(nd.attrib["ref"])
                
        if node["address"] =={}:
            node.pop("address", None)

        if refs != []:
           node["node_refs"]=refs
            
        return node
    else:
        return None

# process the OSM file, write a json out file and return a list of dictionaries
def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in cET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data