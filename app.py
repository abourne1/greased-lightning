import serial
from flask import Flask, request
app = Flask(__name__)

# BAUD = 9600
# ser = serial.Serial('/dev/ttyACM0', BAUD)

@app.route('/', methods=['POST','GET'])
def main():
    speed = request.args.get('speed')
    angle = request.args.get('angle')
    print speed, angle
    # now send this data to arduino
    # ser.write("%d,%d"%(angle, speed))
    return 'speed: ' + speed + ', angle: ' + angle

if __name__ == "__main__":
    app.run()