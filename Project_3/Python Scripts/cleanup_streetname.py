# creating a dictionary for correcting some common street name abbrevations
mapping = { "Ct": "Court",
            "St": "Street",
            "st": "Street",
            "St.": "Street",
            "St,": "Street",
            "ST": "Street",
            "street": "Street",
            "Street.": "Street",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "ave": "Avenue",
            "Rd.": "Road",   
            "rd.": "Road",
            "Rd": "Road",    
            "Hwy": "Highway",
            "HIghway": "Highway",
            "Pl": "Place",      
            "place": "Place",
            }

# function that corrects incorrect street names
def update_name(name, mapping):    
    for key in mapping:
        if key in name:
            name = string.replace(name,key,mapping[key])
    return name