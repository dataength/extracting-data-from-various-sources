import configparser

import pymongo


if __name__ == "__main__":
    parser = configparser.ConfigParser()
    parser.read("pipeline.conf")

    dbname = parser.get("mongo_config", "database")
    collection = parser.get("mongo_config", "collection")
    username = parser.get("mongo_config", "username")
    password = parser.get("mongo_config", "password")
    hostname = parser.get("mongo_config", "hostname")

    dsn = f"mongodb+srv://{username}:{password}@{hostname}/{dbname}?retryWrites=true&w=majority"
    client = pymongo.MongoClient(dsn)

    db = client[dbname]
    collection = db[collection]
    query = {}
    docs = collection.find(query, batch_size=1000)
    for each in docs:
        print(each)
