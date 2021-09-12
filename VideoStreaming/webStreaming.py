from flask import Response
from flask import Flask
from flask import render_template
from threading import Thread
import threading
import argparse
import datetime
import imutils
import time
import cv2
from VideoStreaming import algo
width = 1280
height = 720
flip = 2
camSet = 'nvarguscamerasrc sensor-id=0 ee-mode=1 ee-strength=0 tnr-mode=2 tnr-strength=1 wbmode=3 ! video/x-raw(memory:NVMM), width=3264, height=2464, framerate=21/1,format=NV12 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(width)+', height='+str(height)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! videobalance contrast=1.3 brightness=-.2 saturation=1.2 ! appsink '
app = Flask(__name__)

cam1 = algo.videostream(camSet)
'''
cam2 = algo.videostream(0)
cam3 = algo.videostream(0)
# cam4 is the panaromic camera
cam4 = algo.videostream(0)
cam5 = algo.videostream(0)
cam6 = algo.videostream(0)
'''
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/video_feed")
def video_feed():
	return cam1.video_feed()

@app.route("/science")
def science():
	return render_template("index_science.html")
'''
@app.route("/video_feed1")
def video_feed1():
	return cam2.video_feed()

@app.route("/video_feed2")
def video_feed2():
	return cam3.video_feed()

@app.route("/video_feed3")
def video_feed3():
	return cam4.video_feed()

@app.route("/video_feed4")
def video_feed4():
	return cam5.video_feed()

@app.route("/video_feed5")
def video_feed5():
	return cam6.video_feed()
'''
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	args = vars(ap.parse_args())
	# start the flask app
	app.run(host=args["ip"], port=args["port"],
		threaded=True, use_reloader=False, debug = True)
