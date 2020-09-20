from kafka import KafkaConsumer
import json
from kafka import KafkaProducer
import TwitchMiner as TM

consumer = KafkaConsumer(
    'Prova_acq',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: json.loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         json.dumps(x).encode('utf-8'))

for message in consumer:
    game_list = message.value
    game_list = TM.del_not_games(game_list)
    game_list = TM.add_ranking(game_list)
    game_list = TM.flatten_json(game_list)
    producer.send('prova_ing', value = game_list)
