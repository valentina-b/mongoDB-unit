import pymongo
import os

from os import path
if path.exists("env.py"):
    import env

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

# # insert a new record
# # save it in a var
# new_doc = {'first': 'douglas', 'last': 'adams', 'dob': '11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'}

# coll.insert(new_doc)



# # what if we want to add more than one record?
# # create a new var
# # send an array of dictionaries
# new_docs = [{'first': 'terry', 'last': 'pratchett', 'dob': '28/04/1948', 'gender': 'm', 'hair_colour': 'not much', 'occupation': 'writer', 'nationality': 'english'}, {'first': 'george', 'last': 'rr martin', 'dob': '20/09/1948', 'gender': 'm', 'hair_colour': 'white', 'occupation': 'writer', 'nationality': 'american'}]

# coll.insert_many(new_docs)




# # how do we find specific data?
# # in find() send in key calue pairs in a dictionary of what it is that we're searching for
# documents = coll.find({'first': 'douglas'})



# update one
coll.update_one({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})



# documents = coll.find()

# how to print the object line by line
for doc in documents:
    print(doc)
