from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    # Enable CORS for all the routes
    CORS(app)

    # Import the routes from routes.py
    from .routes import main

    # Register the blueprint for the main routes
    app.register_blueprint(main)

    return app

if __name__ == 'main':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
