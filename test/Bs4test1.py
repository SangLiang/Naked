#encoding:UTF-8
from bs4 import BeautifulSoup
import sys
import urllib.request
url = "https://www.taobao.com"
# url = "http://www.jd.com"
# request = urllib.request.Request('http://www.qq.com')
page = urllib.request.urlopen(url);
print (page.info())
print (page.getcode())
data = page.read().decode('utf-8');

# print (page.getcode())
print(data)


