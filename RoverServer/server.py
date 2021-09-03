from flask import Flask
import argparse
import datetime
import time
from Propulsion import propulsion_algo
from RoboticArm import arm_algo
app = Flask(__name__)

global prop_running, arm_running, science_running
prop_running = False
arm_running = False
science_running = False

@app.route("/propulsion")
def propulsion():
	global prop_running
	if prop_running == True:
		return "Propulsion is running!"
	else:
		prop_running = True
		prop = propulsion_algo.Propulsion()
		del prop
		return "Started propulsion!"

@app.route("/robotic_arm")
def robotic_arm():
	global arm_running
	if arm_running == True:
		return "Arm is running!"
	else:
		arm_running = True
		arm = arm_algo.Robotic_Arm()
		del arm
		return "Started arm!"

@app.route("/science")
def science():
	global science_running
	if science_running == True:
		return "Science module is running!"
	else:
		science_running = True
		return "Started Science module!"

if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=False, default = "0.0.0.0",
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=False, default = "8001",
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	args = vars(ap.parse_args())
	# start the flask app
	app.run(host=args["ip"], port=args["port"],
		threaded=True, use_reloader=False, debug = True)
