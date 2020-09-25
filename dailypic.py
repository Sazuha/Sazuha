import requests
import time
import re
t = time.localtime(time.time())
year = t.tm_year
month = t.tm_mon
day = t.tm_mday
url = 'https://cn.bing.com/'
html = requests.get(url=url)
x = re.search(r'th\?id\=OHR\.[a-zA-z]+_ZH\-CN[0-9]+_1920x1080\.jpg',html.text).group()
bing = url + x
pic = requests.get(url=bing).content
name= "D:\\" + str(year) + "-" + str(month) + "-" + str(day) + ".jpg"
with open(file=name, mode = "wb") as f:
    f.write(pic)




