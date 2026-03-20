import os
import sys
import json
import certifi
import pandas as pd
import pymongo

from dotenv import load_dotenv
load_dotenv()

from networksecurity.constant.mongodb import MONGO_URI
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class NetworkDataExtract:
    def __init__(self):
        try:
            self.mongo_client = pymongo.MongoClient(
                MONGO_URI,
                tls=True,
                tlsCAFile=certifi.where(),
                serverSelectionTimeoutMS=30000,
                retryWrites=True
            )
            logging.info("MongoDB connection established")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path: str):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = json.loads(df.to_json(orient="records"))
            logging.info("CSV converted to JSON successfully")
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database_name, collection_name):
        try:
            database = self.mongo_client[database_name]
            collection = database[collection_name]

            if not records:
                logging.warning("No records found to insert")
                return 0

            collection.insert_many(records)
            logging.info(f"{len(records)} records inserted into MongoDB")

            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":

    FILE_PATH = r"C:\Users\anshv\OneDrive\Desktop\NetworkSecurity-e2e\Network_Data\phisingData.csv"
    DATABASE_NAME = "ANSHAI"
    COLLECTION_NAME = "NetworkData"

    network_obj = NetworkDataExtract()

    records = network_obj.csv_to_json_converter(FILE_PATH)
    print("Sample record:", records[0])

    total_records = network_obj.insert_data_mongodb(
        records,
        DATABASE_NAME,
        COLLECTION_NAME
    )

    print(f"✅ Total records inserted: {total_records}")
