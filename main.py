from fastapi import FastAPI
import pymongo
from pymongo import MongoClient
import json
from pprint import pprint

### DB connectivity
cluster = MongoClient("mongodb+srv://AurumUser:latestPlacid@cluster0.icdds.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["igr"]
collection = db["igr"]



# create instance of fastapi
app = FastAPI()

@app.get("/")
async def root():
    return{"message": "Hello GCP WORLD"}

figu={}
@app.get("/search/{location} {reraid}")
async def search(location:str, reraid:str):
    data = collection.find()
    c=0
    try:
        for i in data:
            for k,v in i.items():
                descr=i['translated description']
                rera=i["RERA Code"]
                if ((location.lower() in descr.lower()) and rera==reraid):
                    c += 1
                    pprint(i)
    except:
        pass
    print(c)
    return {"status": "SUCCESS"}
