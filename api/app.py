import cv2

from flask import Flask, render_template, redirect, Response
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)

imWth = 450
imHgt = 450

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/capture', methods=['POST'])
def capture():

    camera = cv2.VideoCapture(0)

    while camera.isOpened():
    
        ret, frame = camera.read()

        frame = cv2.resize(frame,(imWth,imHgt))

        # Encode the captured image as base64
        _, buffer = cv2.imencode('.jpg', frame)
        image_base64 = base64.b64encode(buffer).decode('utf-8')

        return {'image': image_base64}
    
    #camera.release()

if __name__ == '__main__':
    app.run()