from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS
from dotenv import load_dotenv
import os
import logging

# Initialize Flask application
app = Flask(__name__)
CORS(app, resources={r"/scan": {"origins": "https://anonymous-reporting-4.onrender.com"}})

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()


# Twilio configuration
ACCOUNT_SID = 'AC4780812bbf205dce89373df85efe437d'
AUTH_TOKEN = '0b1d7fe4f863feb0059d41d60cba9314'
TWILIO_PHONE_NUMBER = '+19853338520'
DEVELOPER_PHONE_NUMBER = '+917063031336'

# Initialize Twilio client outside of route handler
client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/scan', methods=['POST'])
def scan():
    app.logger.info('Request received')
    phone_number = request.form.get('phone_number')
    location = request.form.get('location')
    
    if not phone_number or not location:
        return jsonify({"success": False, "error": "Phone number and location are required"}), 400
    
    try:
        message = f"Phone Number: {phone_number}\nLocation: {location}"
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=DEVELOPER_PHONE_NUMBER
        )
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
