import time
import boto3
import os
import boto3.session
from dotenv import load_dotenv
from flask import json, Response

load_dotenv()

session = boto3.Session(region_name='eu-north-1')
client = session.client(
    'ec2',
    aws_access_key_id=os.getenv('AWS_SDK_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SDK_ACCESS_KEY'),
)

def fetch_ec2_instances():
    response = client.describe_instances()
    
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            tags = instance.get('Tags', [])
            name_tag = next((tag['Value'] for tag in tags if tag['Key'] == 'Name'), 'none')
            instances.append({
                'InstanceId': instance['InstanceId'],
                'InstanceName': name_tag,
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A')
            })
    return instances

def stream_ec2_instances():
    def event_stream():
        while True:
            instances = fetch_ec2_instances()
            data = json.dumps(instances)
            yield f"data: {data}\n\n"
            time.sleep(15)
    return Response(event_stream(), mimetype="text/event-stream")
