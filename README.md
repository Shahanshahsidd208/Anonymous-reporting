# Anonymous Reporter

## Table of Contents

- [Problem Statement](#problem-statement)
- [Architecture](#architecture)
- [Features](#features)
- [Working](#working)
- [Application Screenshot](#application-screenshot)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Problem Statement

In many situations, individuals witness crimes or incidents but hesitate to report them due to fear of retaliation or concerns about privacy. There is a need for a system that allows anonymous reporting while ensuring that precise location details are captured to aid in incident management and response.

## Architecture

The Anonymous Reporter project comprises two main components:-

1. **Frontend**: A simple web interface that allows users to report crimes by entering their phone number and providing their location access.
2. **Backend**: A Flask application that receives the data, processes it, and sends the information via SMS to a designated police phone numbers using the Twilio API.

![Architecture Diagram](https://github.com/user-attachments/assets/b0555e54-aabf-4f1b-9d53-95e78a3d3fe5)

## Architecture Diagram Description

### Client (User Device)

- **Browser**
  - Initiates requests to the web application.
  - Sends phone number and location data.
  - Displays confirmation messages and error alerts.

### Frontend

- **HTML/CSS/JavaScript**
  - Hosts the user interface.
  - Handles user input and geolocation.
  - Sends POST requests to the backend server.

### Backend (Flask Application)

- **Endpoints**
  - `/scan`: Handles incoming POST requests with phone number and location.
  - `/`: Confirms the server is running.
- **Middleware**
  - Flask-CORS: Handles cross-origin requests.
- **Environment**
  - Uses environment variables for configuration (Twilio credentials, etc.).
- **Twilio Client**
  - Sends SMS messages containing the phone number and location to the police phone numbers.

### Twilio Service

- **API Endpoint**
  - Receives API requests from the Flask backend.
  - Sends SMS messages to the specified police phone numbers.

### Police's Phone

- **SMS**
  - Receives SMS notifications with crime report details and exact location coordinates.

## Features

- **Precise Incident Reporting**: Sends exact location details for precise incident reporting.
- **Automatic Reporting**: Automatically sends only the exact location coordinates after waiting 45 seconds if the user hesitates to enter their number and submit.
- **Anonymous Reporting**: Users can choose to be anonymous reporters or victims themselves.
- **Widespread Accessibility**: QR codes are pasted all across the city to ensure it is reachable in every corner.

<img src="https://github.com/user-attachments/assets/ca11e8c1-72e7-4ae1-99d8-02c592889afe" width="500">

## Working

1. User accesses the web interface by scanning a QR code pasted in all corners of Hubballi-Dharwad and enters their phone number.
2. User allows location access.
3. The system waits 45 seconds; if the user doesn't submit, it sends the location automatically.
4. Data is sent to the backend server.
5. The backend processes the data and sends an SMS with the details using Twilio.

## Application Screenshot

### Home Page
![Screenshot 2](https://github.com/user-attachments/assets/36054028-9e39-47d5-849c-e44a0fa0fdeb)

### About us Page
![Screenshot (286)](https://github.com/user-attachments/assets/f78dc0f7-0b01-4fa0-8e5a-2d8507a68191)

### Contact us Page
![Screenshot (287)](https://github.com/user-attachments/assets/e5fb7e25-f8c4-4c42-ae5c-33c8c1f7740e)

### Data received on Police mobile numbers

![image](https://github.com/user-attachments/assets/edbe24ba-d250-461d-8eda-2a4f25185a9e)


Details like user exact location coordinates received within 2 seconds.

### Prerequisites for developing this project

- Python 3.x
- Flask
- Twilio account

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/anonymous-reporter.git
    cd anonymous-reporter
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    Create a `.env` file in the project root and add your Twilio credentials and phone numbers:

    ```plaintext
    TWILIO_ACCOUNT_SID=your_account_sid
    TWILIO_AUTH_TOKEN=your_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    DEVELOPER_PHONE_NUMBER=your_developer_phone_number
    ```

## Usage

1. Start the Flask server:

    ```bash
    python app.py
    ```

2. Access the frontend:

    Open `index.html` in your browser or deploy it to a static hosting service.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact:

- **Shahanshah Siddiqui**
  - [Email](mailto:shahanshahsidd208@gmail.com)
  - [LinkedIn](https://www.linkedin.com/in/shahanshah-siddiqui-851354304/)
  - [GitHub](https://github.com/Shahanshahsidd208)

- **Mehwish Nidgundi**
  - [Email](mailto:mehwish.codes@gmail.com)
  - [LinkedIn](https://www.linkedin.com/in/mehwish-nidgundi-712372238/)
  - [GitHub](https://github.com/mehwishferoz)
