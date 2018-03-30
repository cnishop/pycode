import urllib.request as ur
#url='http://www.iheartquotes.com/api/v1/random'
url='http://www.baidu.com'
conn=ur.urlopen(url)
print(conn)


data =conn.read()
#print(data)

print(conn.getheader('Content-Type'))

for key,value in conn.getheaders():
    print(key,value)
