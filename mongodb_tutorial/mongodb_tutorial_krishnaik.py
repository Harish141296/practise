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

#print(client)

mydb = client['Employee'] # will create Employee db if not present
empinfo = mydb.employee_information # Table (Collection) is created
record = {
    '_id' : 1,
    'firstname': 'Jerry',
    'lastname' : 'harry',
    'department':'bankingsector'
}

empinfo.insert_one(record)
records = [{
    '_id':2,
    'firstname': 'krishna',
    'lastname':'moorthi',
    'department':'cooptextile_govt',
    'qualification':'periyapadipu',
    'age' : '60'
    },
    {
        '_id': 3,
        'firstname':'amutha',
        'secondname':'krishnamoorthi',
        'department':'housemaker',
        'qualification':'Enough to train daughter as Queen',
        'age':45
    }
]

empinfo.insert_many(records)

# To find the first record by Querying use 'find_one()'
print(empinfo.find_one())

# to fetch all the records -> find()

for record in empinfo.find():
    print(record)

print(empinfo.find({'firstname':'Jerry'})) # this returns as cursor, to get his we need a for loop

for record in empinfo.find({'firstname':'Jerry'}):
    print(record)

# Query documents using query operators ($in, $lt, $gt)
for record in empinfo.find({'qualification':{'$in':['phd','cooptextile_govt']}}):
    print(record)

# And and Query operators  -> lesserthan - $lt
for record in empinfo.find({'department':'housemaker', 'age' : {'$lt':50}}):
    print(record)

# greaterthan -> $gt
for record in empinfo.find({'department':'housemaker', 'age' : {'$gt':30}}):
    print(record)

# OR Operators
for record in empinfo.find({'$or':[{'firstname':'Jerry'},{'department':'cooptextile_govt'}]}):
    print(record)

for record in empinfo.find({'$and':[{'firstname':'Jerry'},{'department':'cooptextile_govt'}]}):
    print(record)

