import requests
from flask import Flask, request

app = Flask(__name__)
url = 'https://localhost:5000/'

# This endpoint receives an image, speed, and angle
# this data is used to train the model that sends requests to the pi
@app.route('/', methods=['POST','GET'])
def main():
    speed = request.args.get('speed')
    angle = request.args.get('angle')
    image = request.args.get('image')

    # add some code that can identify a stop sign?

    requests.post(url, data={'speed': speed, 'angle': angle})

    print speed, angle
    # now send this data to arduino
    # ser.write("%d,%d"%(angle, speed))
    return 'speed: ' + speed + ', angle: ' + angle

if __name__ == "__main__":
    app.run()