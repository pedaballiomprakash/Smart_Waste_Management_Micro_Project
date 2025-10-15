import paho.mqtt.client as mqtt
import json, sqlite3

DB_FILE = "data.db"

# Setup database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS bin_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bin_id TEXT,
    fill_level REAL,
    temperature REAL,
    gas_level REAL,
    latitude REAL,
    longitude REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    print("Received:", data)
    cursor.execute("""
        INSERT INTO bin_data (bin_id, fill_level, temperature, gas_level, latitude, longitude)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data["bin_id"], data["fill_level"], data["temperature"],
          data["gas_level"], data["latitude"], data["longitude"]))
    conn.commit()

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("smartwaste/bin/data")
client.on_message = on_message
client.loop_forever()
