import re
import urllib.request
import Naked
import os
import chardet
# 输入开始地址
# url = "http://www.27270.com/ent/meinvtupian/"
print('请输入您要爬的网址')
url = input()
print('请输入网址的编码格式')
codeStyle = input()
htmlGetCode = 0

def getHtml(url):
    page = urllib.request.urlopen(url)
    global  htmlGetCode
    htmlGetCode = page.getcode()
    html = page.read().decode(codeStyle)
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)

    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        picsname = str(x) + '.jpg'
        result = Naked.IsPictureNaked(picsname)
        if (result == True):
            x = x + 1
            continue
        else:
            os.remove(picsname)
            x = x + 1
            print('删除了不符合要求%d' % (x))
            continue
html = getHtml(url)
if(htmlGetCode==200):
    getImg(html)
else:
    print (htmlGetCode)
    print('网址未找到')
