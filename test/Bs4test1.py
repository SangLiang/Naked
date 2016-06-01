#encoding:UTF-8
from bs4 import BeautifulSoup
import sys
import urllib.request
url = "http://www.baidu.com"
# request = urllib.request.Request('http://www.qq.com')
page = urllib.request.urlopen(url);
data = page.read().decode('utf-8');


