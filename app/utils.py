# image processing script

# some imports here
import requests



# functions here
def process_image(img):
    print('[*] Image processed successfully')


# allowed files
def allowed_file(filename):
    return '.' in filename and filename.split('.')[-1].lower() in ['png', 'jpg', 'jpeg']

# get a new filename for a new file uploaded
number = 0
def get_new_filename(filename):
    global number
    number += 1 
    return f"image{number}.{filename.split('.')[-1].lower()}"

def fetch_lenses_from_lenskart():
    pass