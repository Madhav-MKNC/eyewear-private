#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

from flask import Flask
from flask import render_template, redirect, request, url_for, send_file
from werkzeug.utils import secure_filename

from PIL import Image
from image_process import process_image, allowed_file, get_new_filename

app = Flask(__name__)

# start web app
def start(host="localhost", port=80, debug=True):
    try:
        app.run(host=host, port=port, debug=debug)
    except Exception as err:
        print("[error]", str(err))


""" /routes """
# home page
@app.route('/')
def index():
    return render_template('index.html')

# upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        print("[!] File not uploaded")
        return redirect(request.url)
    file = request.files['file']

    if file.filename == "" or not allowed_file(file.filename):
        print("[!] File not uploaded")
        return redirect(request.url)
    
    # save file to the uploads folder
    filename = get_new_filename(file.filename)
    if not os.path.exists('app/uploads'):
        os.makedirs('app/uploads')
    file.save(os.path.join('app/uploads', filename))
    print("[*] File uploaded successfully")
    
    # # Process the image
    # img = Image.open(file)
    # processed_img = process_image(img) # Your image processing code here

    # # Save the processed image to a temporary file
    # temp_file = 'temp.png'
    # processed_img.save(temp_file)

    # Send the processed image file to the user's browser
    return send_file(os.path.join('uploads', filename), mimetype='image/png')





# main
if __name__ == "__main__":
    try:
        host = input("[+] Enter the Host Address: ")
        port = input("[+] Enter the port for the program: ")
        debug = False if input("[+] Debug [y/n]: ").lower() in ['no', 'n'] else True
        start(host=host, port=port, debug=debug)

    except Exception as err:
        host = "localhost"
        port = 80
        print("[error]", str(err))
        print("[*] Using defaults")
        print(f"[=] host: {host}")
        print(f"[=] port: {port}")
        start(host=host, port=port, debug=debug)
