# import urllib.request
from PIL import Image # $ pip install pillow
import requests # $ pip install requests

# im = Image.open(urllib.request.urlopen(url))
# print(im.format, im.mode, im.size)

r = requests.get(url, stream=True)
r.raw.decode_content = True # handle spurious Content-Encoding
im = Image.open(r.raw)
print(im.format, im.mode, im.size)
