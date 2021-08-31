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

class videostream:
	def __init__(self, src):
		self.src = src
		self.vs = cv2.VideoCapture(index = self.src)
		self.vs.set(cv2.CAP_PROP_BUFFERSIZE, 2)
		#self.vs.start()
		self.outputFrame = None
		self.lock = threading.Lock()
		self.thread = Thread(target = self.video_feed, args = ())
		self.thread.daemon = True
		self.thread.start()

	def __del__(self):
		self.vs.release()

	def generate(self):
		while True:
			# wait until the lock is acquired
			with self.lock:
				(self.status, self.outputFrame) = self.vs.read()
				self.outputFrame = imutils.resize(self.outputFrame, width = 400)
				#self.outputFrame = cv2.resize(self.outputFrame, (400, 200), interpolation = cv2.INTER_AREA)

				# check if the output frame is available, otherwise skip
				# the iteration of the loop
				if self.outputFrame is None:
					continue
				# encode the frame in JPEG format
				(flag, encodedImage) = cv2.imencode(".jpg", self.outputFrame)
				# ensure the frame was successfully encoded
				if not flag:
					continue
			# yield the output frame in the byte format
			yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
				bytearray(encodedImage) + b'\r\n')

	def video_feed(self):
		return Response(self.generate(),
			mimetype = "multipart/x-mixed-replace; boundary=frame")