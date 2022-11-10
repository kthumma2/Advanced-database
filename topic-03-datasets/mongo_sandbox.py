from pymongo import MongoClient

client = MongoClient("mongodb+srv://kthumma2:Dadiloveu143@kthumma2.brhwe8q.mongodb.net/?retryWrites=true&w=majority")

from bson.objectid import ObjectId

Phones_db = client.Phones_db
list_collection = Phones_db.list_collection

list_collection.delete_many({})

list_collection.insert_many([
{"description": 'Apple'},
{"description": 'Samsung'},
{"description": 'Oneplus'},
{"description": 'Sony'}
])

items = list(list_collection.find())
print(items)