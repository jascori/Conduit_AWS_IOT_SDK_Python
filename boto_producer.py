import boto3
import json
import paho.mqtt.client as mqtt

# AWS Client Setup
# Credentials loaded from ~/.aws/credentials
aws_client = boto3.client('kinesis', region_name='us-east-2')
my_stream_name = "LoRaWAN"

# Push a data item to the stream
def put_to_stream(deveui, seq_no, property_value, property_timestamp):
        payload = {
                'prop': str(property_value),
                'timestamp': str(property_timestamp),
                'seq_no': seq_no,
                'deveui': deveui
        }

        put_response = aws_client.put_record(
                StreamName=my_stream_name,
                Data=json.dumps(payload),
                PartitionKey=deveui)

# Subscribe to LoRaWAN packet uplinks
def on_connect(client, userdata, flags, rc):
        print "MQTT connected"
        client.subscribe("lora/+/up")

# On message received forward the data and eui to the cloud
def on_message(client, userdata, msg):
        print(msg.topic)
        print(str(msg.payload))
        packet = json.loads(msg.payload)
        print(packet['deveui'], packet['data'], packet['time'])
        put_to_stream(packet['deveui'], packet['seqn'], packet['data'], packet['time'])

# MQTT Client Setup
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to localhost to receive messages from lora-network-server
mqtt_client.connect("localhost", 1883, 60)
                          
# Wait for messages       
mqtt_client.loop_forever()