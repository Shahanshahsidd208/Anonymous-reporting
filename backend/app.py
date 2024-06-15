from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS
from dotenv import load_dotenv
import os

app = Flask(__name__)
CORS(app)

# Load environment variables from .env file
load_dotenv()

# Twilio configuration using environment variables
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
DEVELOPER_PHONE_NUMBER = os.getenv('DEVELOPER_PHONE_NUMBER')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/scan', methods=['POST'])
def scan():
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
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
