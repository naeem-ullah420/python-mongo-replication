import os
import pymongo

CHANGE_STREAM_DB="mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
# client = pymongo.MongoClient(os.environ['CHANGE_STREAM_DB'])
client = pymongo.MongoClient(CHANGE_STREAM_DB)
client.changestream.collection1.insert_one({"_id": 2, "hello": "world"})
client.changestream.collection1.update_one({"_id": 2}, {"$set": {"hello": "mars"}})
client.changestream.collection1.replace_one({"_id": 2} , {"bye": "world"})
client.changestream.collection1.delete_one({"_id": 2})
print(client.changestream.collection1.insert_one({"hello": "world"}).inserted_id)
# client.changestream.collection1.drop()
# print(client.changestream.collection1.insert_one({"hello": "world"}).inserted_id)

