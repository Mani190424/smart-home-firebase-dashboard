import requests
import random
import time
from firebase_secrets import FIREBASE_URL

rooms = ["Bedroom1", "Bedroom2", "Kitchen", "LivingRoom", "StoreRoom"]

def generate_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 60.0), 2),
        "motion": random.choice([True, False]),
        "light": random.randint(100, 800),
        "energy": round(random.uniform(100, 500), 2)
    }

while True:
    for room in rooms:
        data = generate_sensor_data()
        response = requests.put(f"{FIREBASE_URL}/{room}.json", json=data)
        print(f"Updated {room}: {data} | Status: {response.status_code}")
    time.sleep(5)
