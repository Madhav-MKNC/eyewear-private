# image processing script

# some imports here
import requests
from bs4 import BeautifulSoup

# data
from data.frames import mapping
frames = mapping

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

# fetching results
def fetch_lenses_from_lenskart(type):
    response = requests.get(frames[type])
    soup = BeautifulSoup(response.text, 'html.parser')
    # lenses = [[data['href'], [data['src']]] for data in soup if 'src' in data.attrs and 'href' in data.attrs]
    hrefs = [tag['href'] for tag in soup.find_all('a', href=True)]
    srcs = [tag['src'] for tag in soup.find_all('img', src=True)]
    print(len(hrefs), len(srcs))



    # return lenses 


if __name__ == "__main__":
    # a = fetch_lenses_from_lenskart('c2')
    # for i in a:
    #     print(*i)
    # print(0)
    fetch_lenses_from_lenskart('c2')