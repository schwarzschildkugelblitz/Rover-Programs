from imutils.video import VideoStream
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

app = Flask(__name__)
cam1 = algo.videostream(0)
cam2 = algo.videostream(0)
cam3 = algo.videostream(0)
cam4 = algo.videostream(0)
@app.route("/")
def index():
	# return the rendered template
	return render_template("index.html")

@app.route("/video_feed")
def video_feed():
	return cam1.video_feed()

@app.route("/video_feed1")
def video_feed1():
	return cam2.video_feed()

@app.route("/video_feed2")
def video_feed2():
	return cam3.video_feed()

@app.route("/video_feed3")
def video_feed3():
	return cam4.video_feed()

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
