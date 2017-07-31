# Send commands takes keystrokes as input and curls the Pi with instructions
import requests

url='http://localhost:5000/'

speed = 0
angle = 0
r = None

UP = 'w'
LEFT = 'a'
RIGHT = 'd'
DOWN = 's'

payload = {'speed': 0, 'angle': 0}

while True:
    var = raw_input(">")

    if len(var) > 0:
        if var[0] == UP:
            payload['speed'] += 10
        elif var[0] == DOWN:
            payload['speed'] = payload['speed'] - 10
        elif var[0] == RIGHT:
            payload['angle'] += 10
        elif var[0] == LEFT:
            payload['angle'] = payload['angle'] - 10

        r = requests.post(url, params=payload)

    print r.text
