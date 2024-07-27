"""
Lets learn pymongo with Python
@author: harish 
"""
# select query based on name 
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
 
# Access the variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

#client to interact with mongodb
client = MongoClient(f'mongodb+srv://{username}:{password}@jerry.yil7qvo.mongodb.net/')

mydb = client['Employee'] 
inventory = mydb.inventory 

inventory.insert_many([
    {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}])

inventory.update_one(
    {"item":"notebook"},
    {"$set":{"size.uom":"out","status":"O"},
    "$currentDate":{"LastModifiedDate":True}}
)

inventory.update_many(
    {"qty":{"$lt":60}},
    {"$set":{"size.uom":"j","status":"Nil"},
    "$currentDate": {"LostModifiedDate":True}}
)

inventory.update_many(
    {"qty":{"$gt":50}},
    {
        "$set":{
            "size.uom":"M",
            "status": "J"
        },
        "$currentDate":{"LastModifiedDate":True}
    }
)


inventory.replace_one(
        {"item":"canvas"},
        {"item":"canvas","instock":[{"warehouse":"A","qty":60},{"warehouse":"B","qty":50}]}
    )


for item in inventory.find({"item":"canvas"}):
    print(item)
















