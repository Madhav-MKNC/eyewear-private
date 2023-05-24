# image processing script

# some imports here
import requests
from bs4 import BeautifulSoup
from PIL import Image
import uuid

# ML stuff
# from detector.engine import detect_faces


""" constants """
INDEX = 'old_index.html'
RESULTS = 'results.html'
# data
mapping = {
    "c1": "https://www.lenskart.com/eyeglasses/promotions/new-arrivals-classic-eyeglasses.html#frame_shape_id=11346",
    "c2": "https://www.lenskart.com/eyeglasses/promotions/new-arrivals-classic-eyeglasses.html#frametype_id=11371",
    "c3": "https://www.lenskart.com/eyeglasses/promotions/new-arrivals-classic-eyeglasses.html#frame_shape_id=11345",
    "c4": "https://www.lenskart.com/eyeglasses/promotions/new-arrivals-classic-eyeglasses.html#frame_shape_id=24178",
    "c5": "https://www.lenskart.com/eyeglasses/promotions/new-arrivals-classic-eyeglasses.html#frame_shape_id=11351",
    "c6": "https://www.lenskart.com/eyeglasses/promotions/new-arrivals-classic-eyeglasses.html#frametype_id=11372",
    "c7": "https://www.lenskart.com/eyeglasses/promotions/new-arrivals-classic-eyeglasses.html#frametype_id=11371"
} 


""" start web app """
def start_server(app):
    try:
        host = input("[+] Enter the Host Address: ")
        port = int(input("[+] Enter the port for the program: "))
        debug = False if input("[+] Debug [y/n]: ").lower() in ['no', 'n'] else True
    except Exception as err:
        host = "localhost"
        port = 80
        debug = False
        print("[error]", str(err))
        print("[*] Using defaults")
        print(f"[=] host: {host}")
        print(f"[=] port: {port}")
    app.run(host=host, port=port, debug=debug)


""" functions here """
def process_image(img):
    print('[*] Image processed successfully')
    # testing
    return 'c4'


""" allowed files """
def allowed_file(filename):
    try:
        return '.' in filename and filename.split('.')[-1].lower() in ['png', 'jpg', 'jpeg']
    except:
        return False


""" get a new filename for a new file uploaded """
def get_new_filename(filename):
    return f"image{str(uuid.uuid1()).replace('-','X')}.{filename.split('.')[-1].lower()}"


""" fetching results """
def fetch_lenses_from_lenskart(type):
    response = requests.get(mapping[type])
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