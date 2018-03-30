import requests
#url='http://www.iheartquotes.com/api/v1/random'
url='http://www.baidu.com'
resp=requests.get(url)

print(resp)
print(resp.text)
