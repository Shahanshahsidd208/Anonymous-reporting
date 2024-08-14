from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging
from flask_socketio import SocketIO  # For real-time WebSocket communication

# Initialize Flask application
app = Flask(__name__)
CORS(app, resources={r"/scan": {"origins": "https://anonymous-reporting-4.onrender.com"}})

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

# Twilio configuration using environment variables
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
DEVELOPER_PHONE_NUMBER = os.getenv('DEVELOPER_PHONE_NUMBER')
#these things should be updated in env file
# Log environment variables to ensure they are loaded (excluding sensitive ones)
app.logger.info(f"ACCOUNT_SID: {ACCOUNT_SID}")
app.logger.info(f"AUTH_TOKEN: {'***' + AUTH_TOKEN[-4:]}")  # Masking sensitive part
app.logger.info(f"TWILIO_PHONE_NUMBER: {TWILIO_PHONE_NUMBER}")
app.logger.info(f"DEVELOPER_PHONE_NUMBER: {DEVELOPER_PHONE_NUMBER}")

# Initialize Twilio client outside of route handler
client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/scan', methods=['POST'])
def scan():
    app.logger.info('Request received')
    phone_number = request.form.get('phone_number')
    location = request.form.get('location')
    
    app.logger.info(f'Received data - Phone Number: {phone_number}, Location: {location}')
    
    if not phone_number or not location:
        app.logger.error('Phone number or location not provided')
        return jsonify({"success": False, "error": "Phone number and location are required"}), 400
    
    try:
        message = f"Phone Number: {phone_number}\nLocation: {location}"
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=DEVELOPER_PHONE_NUMBER
        )
        app.logger.info('Message sent successfully')
        return jsonify({"success": True}), 200
    except Exception as e:
        app.logger.error(f'Error processing request: {str(e)}')
        return jsonify({"success": False, "error": str(e)}), 500

# Route to confirm server is running
@app.route('/')
def home():
    return jsonify({"message": "Server is running!"})

# For deployment on Render.com or similar platforms
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
