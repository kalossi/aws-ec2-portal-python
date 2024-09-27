from flask import Blueprint, jsonify, request
from .utils import fetch_ec2_instances, stream_ec2_instances

main = Blueprint('main', __name__)

# Define the route for a simple API that returns JSON
@main.route('/api/ec2', methods=['GET'])
def ec2_api():
    try:
        if 'Accept' in request.headers and request.headers['Accept'] == 'text/event-stream':
            return stream_ec2_instances()
        else:
            ec2_instances = fetch_ec2_instances()
            print(f"fetched instances on server: \n",  ec2_instances, flush=True)
            return ec2_instances
    except Exception as e:
        return jsonify({'error': str(e)}), 500

