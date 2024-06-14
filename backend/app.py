from flask import Flask, request, jsonify
from twilio.rest import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Twilio configuration
ACCOUNT_SID = 'AC4780812bbf205dce89373df85efe437d'
AUTH_TOKEN = '0b1d7fe4f863feb0059d41d60cba9314'
TWILIO_PHONE_NUMBER = '+19853338520'
DEVELOPER_PHONE_NUMBER = '+917063031336'

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
