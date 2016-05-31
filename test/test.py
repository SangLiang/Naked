import re  
import urllib.request 

s =urllib.request.urlopen('http://www.baidu.com')
# sh = s.read().decode('utf-8')
sh  = str(s.read())
reObj1 = re.compile(r'src="(.+?\.png)"') 
s2=reObj1.findall(sh)

# print(sh)
print(s2)

    
   
