import boto3
import json
from datetime import datetime
import time
import binascii
import base64

# AWS Client Setup
# Credentials read from ~/.aws/credentials
my_stream_name = 'LoRaWAN'
kinesis_client = boto3.client('kinesis', region_name='us-east-2')

response = kinesis_client.describe_stream(StreamName=my_stream_name)
my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
shard_iterator = kinesis_client.get_shard_iterator(
					StreamName=my_stream_name,
					ShardId=my_shard_id,                                                     					ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(
					ShardIterator=my_shard_iterator,
					Limit=10)

def base64ToHex(data):
    binaryData = base64.b64decode(data)
    return binascii.hexlify(binaryData).upper()

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(
					ShardIterator=record_response['NextShardIterator'],
					Limit=10)

#   print record_response
    for val in record_response["Records"]:
		js_obj = json.loads(val["Data"])
		print js_obj["deveui"], js_obj["seq_no"], js_obj["timestamp"]
		# print base64ToHex(js_obj["prop"])
		print base64.b64decode(js_obj["prop"])

    # wait for 5 seconds
    time.sleep(5)