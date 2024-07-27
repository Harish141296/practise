"""
Mongodb Aggregate and Group
1. Avg
2. Sum
3. Project 
"""

from pymongo import MongoClient 
from dotenv import load_dotenv
import os 
from datetime import datetime 

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

client = MongoClient(f'mongodb+srv://{username}:{password}@jerry.yil7qvo.mongodb.net/')

mydb = client['Student'] # create db Student

col = mydb['stud_scores']

data = [
    {"user":"jerry", "subject":"Database", "score": 100},    {"user":"harry", "subject":"Data Science", "score": 90 },    
    {"user":"jerry", "title":"Data Science", "score": 85 },
    {"user":"harry", "title":"Database", "score": 75 },
    {"user":"harry", "title":"python", "score": 95},
    {"user":"jerry", "title":"python", "score": 100},
]

col.insert_many(data)

for record in col.find():
    print(record)

# Total number of records

agg_result = col.aggregate(
    [
        {"$group":{
            "_id": "$user",  # user is the column name
            "Total Subject": {"$sum" : 1}
        }}
    ]
)

for i in agg_result:
    print(i)

## sum of scores 
agg_result = col.aggregate(
    [{"$group":{
        "_id":"$user",
        "Total Scores" :{"$sum": "$score"}
    }}]
)

for i in agg_result:
    print(i)

# avg score based on user 
agg_result = col.aggregate(
    [{"$group":{
        "_id":"$user",
        "student_average":{"$avg":"$score"}
    }
    
    }]
)

for i in agg_result:
    print(i)

# lets create a new collection
data = [
    {"_id": 1, "item":"abc", "price": 2, "qty" : 2, "date": datetime.now()},
    {"_id": 2, "item":"jay", "price": 100, "qty" : 1, "date": datetime.now()},
    {"_id": 3, "item":"hay", "price": 5, "qty" : 5, "date": datetime.now()},
    {"_id": 4, "item":"jay", "price": 10, "qty" : 10, "date": datetime.now()},
    {"_id": 5, "item":"hay", "price": 5, "qty" : 10, "date": datetime.now()},
]

col = mydb['stores']
col.insert_many(data)

agg_result = col.aggregate(
    [
        {"$group":{
            "_id":"$item",
            "avgAmount":{"$avg":{"$multiply":["$price","$qty"]}},
            "avgQuantity":{"$avg":"$qty"}
        }}
    ]
)

for i in agg_result:
    print(i)

# project - just like select query 
data=[{
  "_id" : 1,
  "title": "abc123",
  "isbn": "0001122223334",
  "author": { "last": "zzz", "first": "aaa" },
  "copies": 5
},
{
  "_id" : 2,
  "title": "Baked Goods",
  "isbn": "9999999999999",
  "author": { "last": "xyz", "first": "abc", "middle": "" },
  "copies": 2
}
]

col = mydb['Books']
col.insert_many(data)

for row in col.aggregate([{"$project":{"title": 1}}]):
    print(row)

for row in col.aggregate([{"$project":{"title": True,"author.first": True, "author.last": 1, "copies":True }}]):
    print(row)

# project -> simple like a select statement in sql, where we select particular column in it.