# encoding: utf-8
import sys
from PIL import Image 
img = Image.open(sys.argv[1]).convert('YCbCr')
print(img.format, img.size, img.mode) 
# print img
w, h = img.size  
data = img.getdata() 
# print data 
cnt = 0  
for i, ycbcr in enumerate(data):  
    y, cb, cr = ycbcr  
    if 86 <= cb <= 117 and 140 <= cr <= 168:  
        cnt += 1  
print (cnt)
print (w*h,w*h*0.3)
print ('%s %s 一张暴露图片.'%(sys.argv[1], '是' if cnt > w * h * 0.3 else '不是') ) 