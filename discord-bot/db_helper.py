import json
from pymongo import MongoClient
from dotenv import load_dotenv
import os 

load_dotenv()
CONNECTION_STRING = os.getenv('CONNECTION_STRING')

def get_random_challenge():
    client = MongoClient(CONNECTION_STRING)
   
    db = client['discord-bot']
    collection = db['challenges']
    random_record = collection.aggregate([{ '$sample': { 'size': 1 } }]).next()
    challenge = "{}:{}".format(random_record['name'],random_record['url'])
    return challenge

def add_challenge(challenge_name,url):
    
    data = {
        "name":challenge_name,
        "url":url
    }
    
    client = MongoClient(CONNECTION_STRING)
   
    db = client['discord-bot']
    collection = db['challenges']

    collection.insert_one(data)

    client.close()


def main():
    with open('challenges.json', 'r') as file:
        data = json.load(file)
    client = MongoClient(CONNECTION_STRING)
    print("connection made")
    db = client['discord-bot']
    collection = db['challenges']

    collection.insert_many(data['challenges'])
    print("uploaded challenges")
    client.close()

if __name__ == '__main__':
    get_random_challenge()
