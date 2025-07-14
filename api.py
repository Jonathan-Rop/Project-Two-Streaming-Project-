import requests
import time

def get_api():
    url = "https://api.openaq.org/v2/latest?city=Nairobi"
    response = requests.get(url)
    return response.json()

while True:
    data = get_api()
    # send to Kafka or process directly
    print(data)
    time.sleep(10)
    