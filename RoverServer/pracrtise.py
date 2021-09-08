from flask import Flask, request, Response
import requests
import cv2
import json
import numpy as np
import matplotlib.pyplot as plt
address = "http://192.168.29.13:8000/capture"
resp = requests.get(address)
with open('file1.jpg', 'wb') as f:
	f.write(resp.content)