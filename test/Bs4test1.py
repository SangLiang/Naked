#encoding:UTF-8
from bs4 import BeautifulSoup
import sys
import urllib.request
url = "http://www.soso.com"
# request = urllib.request.Request('http://www.qq.com')
page = urllib.request.urlopen(url);
data = page.read().decode('utf-8');
# str.decode(encoding='UTF-8',errors='ignore')

# sh = s.read().decode('utf-8')
# sh  = str(s.read().decode('utf-8'))
# print (str(response.read()))
# print (response.read().decode('utf-8','ignore'))
print (data)

