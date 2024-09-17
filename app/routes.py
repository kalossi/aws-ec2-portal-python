from flask import Blueprint, jsonify
from .utils import fetch_ec2_instances

main = Blueprint('main', __name__)

# Define the route for a simple API that returns JSON
@main.route('/api/ec2', methods=['GET'])
def ec2_api():
    try:
        ec2_instances = fetch_ec2_instances()
        return jsonify(ec2_instances), 200  # Return the fetched instances and HTTP 200 OK status
    except Exception as e:
        return jsonify({'error': str(e)}), 500

