# encoding: utf-8
import sys
from PIL import Image 



def IsPictureNaked(imgsrc):
    img = Image.open(imgsrc).convert('YCbCr')
#     print(img.format, img.size, img.mode) 
    # print img
    w, h = img.size  
    data = img.getdata() 
    cnt = 0  
    for i, ycbcr in enumerate(data):  
        y, cb, cr = ycbcr  
        if 86 <= cb <= 117 and 140 <= cr <= 168:  
            cnt += 1  
#     print (cnt)
#     print (w*h,w*h*0.3)
#     print (cnt/(w*h*0.3))
#     print ('该图片 %s 一张暴露图片.'%('是' if cnt > w * h * 0.3 else '不是') ) 
    if(cnt > w * h * 0.3):
        return True
    else:
        return False
    
    
