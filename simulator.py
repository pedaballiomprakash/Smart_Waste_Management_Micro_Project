import random, time, json
import paho.mqtt.publish as publish

BROKER = "test.mosquitto.org"  # free public MQTT broker
TOPIC = "smartwaste/bin/data"

while True:
    data = {
        "bin_id": "BIN_01",
        "fill_level": random.randint(0, 100),
        "temperature": random.uniform(20, 40),
        "gas_level": random.uniform(100, 800),
        "latitude": 28.6139,
        "longitude": 77.2090
    }
    publish.single(TOPIC, json.dumps(data), hostname=BROKER)
    print("Sent:", data)
    time.sleep(5)
