#coding=utf-8
'''import requests
import urllib
import urllib.request
import re

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
#cookie = {'cookie':'__cfduid=d70327cfba7a072305ed6c921477b0e961526353086; PHPSESSID=0c2f7e851a7309c1b075ae5b1873d340a2eed9e3473d2b5a1c9e856d1d8d3aed6880c4d3c26f8e4199a2932d43a02b1822e920eb643efbc4bafed057a96f74dc; lang_en=I9IL6HL1; language=en; lang_selection=1'}
#url = 'https://kiwivm.64clouds.com/main.php'

def login(data):
    s = requests.session()
    afterURL = 'https://kiwivm.64clouds.com/main.php'
    loginURL = 'https://kiwivm.64clouds.com/'
    login = s.post(loginURL,headers=header )
    response = s.get(afterURL,data=data,cookie = login.cookies,headers = header)
    return response

#html = requests.get(url,cookie).text
#print(html)
data = {"login":"98.142.139.74","password":"sxx15265540638"}
print (login(data).content)'''


'''import sys
import io
from urllib import request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网站
url = 'https://kiwivm.64clouds.com/main.php'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'__cfduid=d70327cfba7a072305ed6c921477b0e961526353086; PHPSESSID=0c2f7e851a7309c1b075ae5b1873d340a2eed9e3473d2b5a1c9e856d1d8d3aed6880c4d3c26f8e4199a2932d43a02b1822e920eb643efbc4bafed057a96f74dc; lang_en=I9IL6HL1; language=en; lang_selection=1'

#登录后才能访问的网页
#url = 'http://ssfw.xmu.edu.cn/cmstar/index.portal'

req = request.Request(url)
#设置cookie
req.add_header('cookie', cookie_str)
#设置请求头
req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36')

resp = request.urlopen(req)

print(resp.read().decode('utf-8'))'''


import requests
import sys
import io
from bs4 import BeautifulSoup
import re
from tkinter import *
import tkinter.filedialog
import threading
import time

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
data = {
'login': '98.142.139.74',
'password': 'sxx15265540638'
}
# 设置请求头
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

login_url = 'https://kiwivm.64clouds.com/?mode=login'
#登录后才能访问的网页
url = 'https://kiwivm.64clouds.com/kiwi-main-controls.php'

root= Tk(className='搬瓦工控制台')

Label(root, text='IP地址：' ).grid(row=0,column=0)

Label(root, text='端口:').grid(row=1,column=0)

Label(root, text='内存：').grid(row=2,column=0)

Label(root, text='交换分区：').grid(row=3,column=0)

Label(root, text='磁盘使用情况：').grid(row=4,column=0)

Label(root, text='带宽使用情况：').grid(row=5,column=0)
Label(root, text='到期时间：').grid(row=6,column=0)


def fun():

    #构造Session
    session = requests.Session()
    resp = session.post(login_url, data)

    #发送访问请求
    resp = session.get(url)

    #print(resp.content.decode('utf-8'))

    text = resp.content.decode('utf-8')
    soup = BeautifulSoup(text, "html.parser")
    #r = re.compile(r"<font color='#a0a0a0'>(.*?)</font>")
    new = re.findall(r"<td>(.*?)</td>", text, re.I|re.M)
    news = re.findall(r"<font color='#a0a0a0'>(.*?)</font>", text, re.I|re.M)
    #print(news)
    #print(len(news))
    #for i in range(0,len(news)):
    #print(news[i])
    ipaddress = new[7]
    port = new[9]
    ram = news[0]
    swap = news[1]
    diskusage = news[2]
    timeout = news[3]
    bwusage = news[4]

    #root= Tk(className='搬瓦工控制台')
    #Label(root, text='IP地址：' ).grid(row=0,column=0)
    Label(root, text=ipaddress).grid(row=0,column=1)
    #Label(root, text='端口:').grid(row=1,column=0)
    Label(root, text=port).grid(row=1,column=1)
    #Label(root, text='内存：').grid(row=2,column=0)
    Label(root, text=ram).grid(row=2,column=1)
    #Label(root, text='交换分区：').grid(row=3,column=0)
    Label(root, text=swap).grid(row=3,column=1)
    #Label(root, text='磁盘使用情况：').grid(row=4,column=0)
    Label(root, text=diskusage).grid(row=4,column=1)
    #Label(root, text='带宽使用情况：').grid(row=5,column=0)
    Label(root, text=bwusage).grid(row=5,column=1)
    #Label(root, text='到期时间：').grid(row=6,column=0)
    Label(root, text=timeout).grid(row=6,column=1)
    Label(root,text=time.strftime('%H:%M:%S',time.localtime(time.time()))).grid(row=7,column=1)
    global timer
    timer = threading.Timer(60, fun)
    timer.start()


timer = threading.Timer(1,fun)
timer.start()
root.mainloop()




'''#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'__cfduid=d70327cfba7a072305ed6c921477b0e961526353086; PHPSESSID=0c2f7e851a7309c1b075ae5b1873d340a2eed9e3473d2b5a1c9e856d1d8d3aed6880c4d3c26f8e4199a2932d43a02b1822e920eb643efbc4bafed057a96f74dc; lang_en=I9IL6HL1; language=en; lang_selection=1'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

# 设置请求头
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

# 在发送get请求时带上请求头和cookies
resp = requests.get(url, headers=headers, cookies=cookies)

#print(resp.content.decode('utf-8'))
text = resp.content.decode('utf-8')
soup = BeautifulSoup(text, "html.parser")

print(soup.body.div.font)'''


'''r = re.compile(r'<a href="intramural/content/news/(?P<ID>.{5}).*" target="_blank">(?P<Title>.+)</a>')
r = re.compile(r\'''<tr><td>(.*?)<td><td><span class='indicator'><table cellspacing="0" cellpadding="0" style="width:100;border:1px solid #00a000"><tr><td style='width:(^\d{m,n}$)%;background:#00a000;height:8px;vertical-align:middle'></td><td style='width:(^\d{m,n}$)%'></td></tr></table></span><font color='#a0a0a0'>(.*?)</font></td></tr>\''')
#news = r.findall(resp.content.decode('utf-8'),text,re.S|re.M)
news = r.findall(resp,text,re.S|re.M)
for i in range(len(news)):
    ID = news[i][0]
    title = news[i][1]
# data = data.decode('utf-8')
# title = title.decode('utf-8')
print (title + " " + ID + " ")'''