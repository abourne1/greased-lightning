import serial
import math
import time
import xbox_read
import threading 

"""
Sxxx: speed command
Dxxx: degree command

maybe I should send multiple commands in one serial write to speed things up
"""

BAUD = 9600

ser = serial.Serial('/dev/ttyACM5', BAUD)
x = 0
y = 0
theta = 90

def sgn(x):
    if x >= 0:
	return 1
    return -1 

def getAngle(x, y):
    if y == 0: return 90
    return 90 - int((sgn(y)*math.degrees(math.atan(float(x)/y))))

def setUp():
    print ser.isOpen()
    print("Using port: %s" % ser.portstr)

def destroy():
    ser.close()
    
class KeyCollection(object):
	def __init__(self):
		self.keys = {}
	
	def update(self, e):
		self.keys[e.key] = e.value
		
	def read(self):
		return self.keys
		
class SerialCommmand(object):
	def __init__(self,angle, speed):
		self.angle = angle
		self.speed = speed
		self.cmd = "a%d.s%d" % angle, speed
		
	def __repr__(self):
		return self.toString()
		
	def toString(self):
		return "Angle: %d, Speed: %d" % (self.degree, self.speed)
		
if __name__ == '__main__':
	setUp()
	
	kc = KeyCollection()
	t = threading.Thread(target=xbox_read.get_event, args=(kc,))
	t.start()
	
	"""
	Test sending multiple speed and angle commands in each serial write
	to make controls more reflexive
	"""
	
	while(True):
		states = kc.read()
		if len(states) > 0:
			print states
			angle = getAngle(states['X1'], states['Y1'])
			speed = states['RT']
			sc = SerialCommmand(angle, speed)
			print sc
			ser.write(sc.toString())
			print "written"
		time.sleep(1.25)
		
	destroy()
