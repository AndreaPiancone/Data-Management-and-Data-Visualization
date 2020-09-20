from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'prova_ing',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.ProvaDataMan.Twitch

for message in consumer:
    message = message.value
    for document in message:
        collection.insert_one(document)
