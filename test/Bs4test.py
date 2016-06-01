#encoding: utf-8
from bs4 import BeautifulSoup
import sys
import urllib.request 
import re

urlLibs = [];
url =urllib.request.urlopen('http://www.baidu.com')
url_read= str(url.read())
reg = r'href="http://(.+?)"' 
findurl = re.compile(reg)  
urllist = findurl.findall(url_read)
# print (sh)
_temp = 0
for item in urllist:
    urlLibs.append(item) 
    _temp = _temp+1
    
print (urllist)
print ('url待爬库的数量为%d'%(len(urllist)))


