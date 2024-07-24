# from pymongo.mongo_client import MongoClient
# import urllib.parse
# username = urllib.parse.quote_plus('username')
# password = urllib.parse.quote_plus('password')
# print(username, password)

# replace username with your username, password with your created password, host with the current cluster host address

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://<username>:<password>@<host>/mydatabase?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)