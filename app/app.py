# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import os

# from flask import Flask
# from flask import render_template, redirect, request, url_for, send_file
# from werkzeug.utils import secure_filename

# from PIL import Image
# from image_process import process_image

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads'

# # start web app
# def start(host="localhost", port=80, debug=True):
#     try:
#         app.run(host=host, port=port, debug=debug)
#     except Exception as err:
#         print("[error]", str(err))

# # routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     file = request.files['file']
#     if file:
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#         print('[*] File uploaded successfully')
#     else:
#         print("[!] No file uploaded")
#         return 'No file uploaded'
    
#     # Process the image
#     img = Image.open(file)
#     processed_img = process_image(img) # Your image processing code here

#     # Save the processed image to a temporary file
#     temp_file = 'temp.png'
#     processed_img.save(temp_file)

#     # Send the processed image file to the user's browser
#     return send_file(temp_file, mimetype='image/png')





# # main
# if __name__ == "__main__":
#     # run on defaults (host:port)
#     start(debug=True)







"""
############################################################################################
"""


from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Set the upload folder and allowed file types
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Define a function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Define the route for the upload form
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    
    # Check if the file has an allowed extension
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)
    
    # Save the file to the upload folder
    filename = secure_filename(file.filename)
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    file.save(os.path.join('uploads', filename))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
