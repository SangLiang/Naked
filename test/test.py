import re  
import urllib.request 

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('gbk')
    
    reg = '百度'
    resaa = re.compile(reg)
    
    listmy = resaa.findall(html)
    print (html)


getHtml("http://www.baidu.com")
