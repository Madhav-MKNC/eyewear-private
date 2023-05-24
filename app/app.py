#!/usr/bin/python
# -*- coding: UTF-8 -*-

""" imports """
import os
from flask import Flask
from flask import render_template, redirect, request, url_for, send_file
# from werkzeug.utils import secure_filename
from PIL import Image
from utils import *


""" app """
app = Flask(__name__)


""" index page """
@app.route('/')
def index():
    return render_template(INDEX)

""" upload """
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        print("[!] File not uploaded")
        return render_template(INDEX, error_message="File not uploaded!")
    file = request.files['file']
    if file.filename == "" or not allowed_file(file.filename):
        print("[!] File not uploaded")
        return render_template(INDEX, error_message="File not uploaded!")

    # save file to the uploads folder
    filename = get_new_filename(file.filename)
    if not os.path.exists('app/uploads'):
        os.makedirs('app/uploads')
    file.save(os.path.join('app/uploads', filename))
    print("[*] File uploaded successfully")
    
    # Process the image
    img = Image.open(file)
    contour_type = process_image(img) # Your image processing code here

    # Send the processed image file to the user's browser
    # return send_file(os.path.join('uploads', filename), mimetype='image/png')
    return render_template(RESULTS, type=contour_type)


""" results """
@app.route('/results/<string:type>', methods=['GET'])
def results(type):
    if type not in ['c1','c2','c3','c4','c5','c6','c7']:
        return render_template(INDEX, error_message="some error occured!")
    lenses = fetch_lenses_from_lenskart(type)
    print("#####################################")
    print(lenses)
    print("#####################################")
    return render_template(RESULTS, lenses=lenses)



""" main """
if __name__ == "__main__":
    start_server(app)
