def update_name(zipcode):
    testNum = re.findall('[a-zA-Z]*', zipcode)
    if testNum:
        testNum = testNum[0]
    testNum.strip()
    if testNum == "- 5":
        convertedZipcode = (re.findall(r'\d+', zipcode))
        if convertedZipcode:
            if convertedZipcode.__len__() == 3:
                return (re.findall(r'\d+', zipcode))[0] + "-" +(re.findall(r'\d+', zipcode))[1]
            else:
                return (re.findall(r'\d+', zipcode))[0]

## or
# zipcodes = audit_zipcodes(bangaloreOSM)

# for zipcode in zipcodes:
#     if zipcode.startswith('- 5'):
#         zipcode = zipcode[2:]
#     print zipcode, zipcodes[zipcode]