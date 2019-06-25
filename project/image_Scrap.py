from bs4 import BeautifulSoup
import requests
handle = raw_input('Input your account name on Twitter: ') 
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text,'lxml')
import re
images = list(bs.find_all('img', {'src':re.compile('.jpg')}))
url=images[0]['src']

from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()
