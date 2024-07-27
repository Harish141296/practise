# select query based on name 
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
 
# Access the variables
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')


# Connect to the MongoDB server
client = MongoClient(f'mongodb+srv://{username}:{password}@jerry.yil7qvo.mongodb.net/')  # Replace with your MongoDB URI
db = client['sample_airbnb']  # Replace with your database name
collection = db['listingsAndReviews']  # Replace with your collection name


# Perform the query
document = collection.find_one({'name': 'Ribeira Charming Duplex'})

# Print the result
if document:
    print(document)
else:
    print("No document found with the given _id")
