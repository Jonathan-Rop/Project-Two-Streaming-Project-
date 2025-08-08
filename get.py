import requests
import json
from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

api_url = 'https://fakestoreapi.com/products'

while True:
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()  
            print(f"Data to Kafka: {data}")
            producer.send('Stream', value=data)
        else:
            print(f"API error: {response.status_code}")
    except Exception as e:
        print(f"Error fetching/sending data: {e}")
    
    time.sleep(5)
