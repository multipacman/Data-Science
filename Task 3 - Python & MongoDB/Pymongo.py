try:
    import pymongo
    from pymongo import MongoClient
    import pandas as pd
except Exception as e:
    print("Import Module Error!")


client = MongoClient("localhost",27017)
database = client["DataScience"]
creation = client.list_database_names()
if "DataScience" in creation:
    print("Database already exists")
else:
    print("Database created successfully")


df = pd.read_csv('https://query.data.world/s/5hyczoogvkbnk7gmvtdbj4lnxxunyi')
data = df.to_dict('records')

database.globalClimate.insert_many(data, ordered=False)
print("Data added successfully")