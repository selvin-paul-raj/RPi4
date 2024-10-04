from flask import Flask, render_template, request
from flask_cors import CORS 
# import RPi.GPIO as GPIO

# # Setup GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# LED_PIN = 17
# GPIO.setup(LED_PIN, GPIO.OUT)

app = Flask(__name__)
CORS(app)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led_control', methods=['POST'])
def led_control():
    led_state = request.form['led']
    
    if led_state == 'on':
        print("ON")
        # GPIO.output(LED_PIN, GPIO.HIGH)  
    elif led_state == 'off':
        print("OFF")
        # GPIO.output(LED_PIN, GPIO.LOW)  
    
    return 'LED state changed to ' + led_state

if __name__ == '__main__':
    app.run( port=5000)
