import re  
import urllib.request  
import Naked
import os
url = "http://www.27270.com/ent/meinvtupian/"


def getHtml(url):  
    page = urllib.request.urlopen(url)  
    html = page.read().decode('gbk')  
    # print (html) 
    return html  
  
def getImg(html):  
    reg = r'src="(.+?\.jpg)"'  
    imgre = re.compile(reg)  
   
    imglist = imgre.findall(html)
    x = 0  
    for imgurl in imglist:  
#         result = Naked.IsPictureNaked(imgurl)
        print(imgurl)
#         if (result==True):
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x) 
        picsname = str(x)+'.jpg'
        result = Naked.IsPictureNaked(picsname)
        if(result==True):
            x = x + 1
             
            continue
        else:
            os.remove(picsname)
            x = x + 1
            print('删除了不符合要求%d'%(x))  
            continue
     
html = getHtml(url)
getImg(html) 