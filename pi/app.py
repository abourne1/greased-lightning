import serial
from flask import Flask, request
app = Flask(__name__)

BAUD = 115200
ser = serial.Serial('/dev/cu.usbmodem1411', BAUD)


@app.route('/', methods=['POST','GET'])
def main():
    if not ser.isOpen():
        ser.open()

    speed = request.args.get('speed')
    angle = request.args.get('angle')
    suc = ser.write(speed.encode('utf-8'))

    return 'speed: ' + speed + ', angle: ' + angle

if __name__ == "__main__":
    app.run()