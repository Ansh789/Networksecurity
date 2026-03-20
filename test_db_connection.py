from pymongo import MongoClient
from networksecurity.constant.mongodb import MONGO_URI

def test_mongo_connection():
    client = MongoClient(MONGO_URI)
    print("✅ Connected to MongoDB Atlas")

    print("Databases available:")
    print(client.list_database_names())

if __name__ == "__main__":
    test_mongo_connection()
    