import boto3
import os
import boto3.session
from dotenv import load_dotenv

load_dotenv()

session = boto3.Session(region_name='eu-north-1')
print(f"Region: {session.region_name}")
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
    print(instances)
    return instances
