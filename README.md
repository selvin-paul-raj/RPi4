# IoT LED Control Project

This project allows you to control an LED connected to a Raspberry Pi 4 via a web interface. When you click the buttons on the webpage, the LED will turn on or off accordingly.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Hardware Setup](#hardware-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed on your Raspberry Pi 4:

- **Raspberry Pi 4** with Raspberry Pi OS installed
- **Python 3** (pre-installed on Raspberry Pi OS)
- **pip** (Python package installer, pre-installed on Raspberry Pi OS)
- **Flask**
- **RPi.GPIO**

## Hardware Setup

1. **Connect the LED**:
   - Connect the positive (longer) leg of the LED to GPIO pin 17 on the Raspberry Pi.
   - Connect the negative (shorter) leg of the LED to a resistor (220Ω is a common value).
   - Connect the other end of the resistor to a ground (GND) pin on the Raspberry Pi.

   **Circuit Diagram** (you can draw or reference a diagram here):
        +---(LED)---|>|---(220Ω resistor)---GND
   |
   |
 GPIO 17



## Installation

1. **Clone the repository** (replace `your-repo-url` with the actual repository URL):

```bash
git clone https://github.com/selvin-paul-raj/RPi4
cd RPi4
```
2.Create a virtual environment (recommended):
```
python3 -m venv venv
```
3.Activate the virtual environment:
```
source venv/bin/activate
```
4.Install Flask and other dependencies:
```
pip install Flask Flask-CORS RPi.GPIO
```
5.Run the Flask application:
```
python app.py
```
## Using ngrok
To expose your Flask application to the internet, you can use ngrok. Follow these steps:

1. Download and install ngrok:

Go to the ngrok website and follow the instructions for downloading and installing ngrok on your Raspberry Pi.

2. Expose your Flask app:

Run the following command in a new terminal window while your Flask app is running:
```
ngrok http http://127.0.0.1:5000

```

This updated README file provides clear instructions for using ngrok alongside the other setup details, making it easier for users to run and access your IoT LED control project remotely. Feel free to modify any sections or add additional details as needed!



