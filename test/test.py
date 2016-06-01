#encoding:UTF-8
import re  
import urllib.request 
piclist = []
s =urllib.request.urlopen('https://github.com/SangLiang?tab=repositories')

sh = s.read().decode('utf-8')
# sh  = str(s.read())
reObj1 = re.compile(r'src="(.+?\.js)"') 
s2=reObj1.findall(sh)


piclist.append(s2)
print ('finish')
print(sh)
print(s2)

    
   
