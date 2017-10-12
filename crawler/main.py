# coding : UTF-8

import urllib.request
import binascii
from bs4 import BeautifulSoup
from PIL import Image
import io

url = "http://www.hokudai.ac.jp"

def get_html():
    html = urllib.request.urlopen(url).read() \
            .decode('UTF-8')
    print(html)
    return html

def get_logo_url(html):
    soup = BeautifulSoup(html, 'lxml')
    logo_src = soup.find('h1') \
                .a.img.get('src')
    logo_url = url + logo_src
    return logo_url

def save_logo_url(logo_url):
    binimg = urllib.request.urlopen(logo_url)
    binimg_o = io.BytesIO(binimg.read())
    img = Image.open(binimg_o)
    img.save('logo.png')

if __name__ == '__main__':
    html = get_html()
    logo_url = get_logo_url(html)
    save_logo_url(logo_url)
