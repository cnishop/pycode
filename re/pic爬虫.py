import re
import urllib.request

def getHtml(url):
    page = urllib.request.urlopen(url)
    html=page.read()
    return html

def getImg(html):
    reg=r'src="(.*?\.jpg)" size'
    imgre = re.compile(reg)
    html=html.decode('utf-8')#python3
    imglist = re.findall(imgre,html)
    #return imglist
    x=0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg'%x)
        x = x+1

html = getHtml("https://tieba.baidu.com/p/5622978717")
#print(html)
print(getImg(html))
