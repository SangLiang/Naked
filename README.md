# Naked
判断一张图片是否为暴露的（裸露的）。

---

## v0.0.1 指南

---
版本:Python3.5

依赖:pillow库


启动文件方式：进入**Spider**文件夹，然后使用cmd 或者shell指令 python Spider.py 即可。

抓取到的文件将会放入Spider文件夹内.

切换爬虫地址请修改Spider.py第一行

```python
url = "http://www.27270.com/ent/meinvtupian/"
```

如果出现编码错误，可以事先查看网页编码。然后修改:
```python
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read().decode('gbk')
    return html
```

中的"decode('gbk')"，将其修改为与网页编码相同的编码方式即可（一般都是gbk或者utf-8）。


