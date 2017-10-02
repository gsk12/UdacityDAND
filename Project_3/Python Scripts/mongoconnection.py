# Processing the file
data = process_map(bangaloreOSM)

client = MongoClient()
db = client.bangaloreOSM
collection = db.bangaloreMAP
collection.insert(data)
collection

