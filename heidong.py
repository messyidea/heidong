# -*- coding: utf-8 -*-  
import re  
import urllib  
import urllib2  
import cookielib  
import datetime
import httplib


#模拟登录  
cj = cookielib.CookieJar() 
path = 'https://heidong.in/index.php'  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
opener.addheaders = [('User-agent', 'Opera/9.23')]  
urllib2.install_opener(opener)  
req = urllib2.Request(path)  
conn = urllib2.urlopen(req)  
html = conn.read()

#获取PHPSESSID
for ck in cj:
    #print ck.name,':',ck.value
    f1 = ck.name
    f2 = ck.value
print f1,':',f2
st = f1+'='+f2
print st
st2 = st + ';'
#print st2

#用户名和密码
username = 'yourusername'
password = 'yourpassword'
login_post_data= {
    'op': 'login',
    'email': username,
    'password': password,
    }

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
     'Content-Type': 'application/x-www-form-urlencoded',
     'Connection' : 'keep-alive',
     'Cookie':st,  
     'Referer':'https://heidong.in/signin.php',
     'Origin':'https://heidong.in',
     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}

post_data = urllib.urlencode(login_post_data)  
conn = httplib.HTTPSConnection('heidong.in', 443)
conn.request("POST", '/config/userData.php', post_data, headers)
response = conn.getresponse()
print 'Login: ', response.status, response.reason
ress1 = response.read();
#print ress1.decode("utf-8")


cookie = response.getheader("set-cookie")
cookie = st2 + cookie
print cookie
get_headers = {
     'Host' : 'heidong.in',
     'Connection' : 'keep-alive' , 
     'Cache-Control' : 'max-age=0',
     'Cookie' : cookie ,
     'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
     'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6',
}



conn2 = httplib.HTTPSConnection('heidong.in')
conn2.request("GET", '/mission.php',None,get_headers)
res2=conn2.getresponse()
ress = res2.read();
print ress.decode("utf-8")


m=re.search(r"(once=)\d{5}",ress)
key = m.group(0)
print key
_url = '/mission.php?'+key
print _url


value={
    'once':key,
}
values = urllib.urlencode(value)
conn3 = httplib.HTTPSConnection('heidong.in')
conn3.request("GET", _url,values,get_headers)
res3=conn3.getresponse()
ress3 = res3.read();
print ress3
