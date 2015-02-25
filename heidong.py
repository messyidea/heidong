# -*- coding: utf-8 -*-  
import re  
import urllib  
import urllib2  
import cookielib  
import datetime
import httplib

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
     #'Cookie':st,  
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
#print cookie

#cookie = st2 + cookie
#print cookie
get_headers = {
     'Host' : 'heidong.in',
     'Connection' : 'keep-alive' , 
     'Cache-Control' : 'max-age=0',
     'Cookie' : cookie ,
     'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
     'Referer': 'https://heidong.in/config/userData.php',
     'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6',
}



conn2 = httplib.HTTPSConnection('heidong.in')
conn2.request("GET", '/index.php',None,get_headers)
res2=conn2.getresponse()
cookie2=res2.getheader("set-cookie")

#print cookie2
#print type(cookie2)
md = cookie2.split(' ')
#print md
md0 = md[0]
#print md0


cok = md0+cookie
get_headers2 = {
     'Host' : 'heidong.in',
     'Connection' : 'keep-alive' , 
     'Cache-Control' : 'max-age=0',
     'Cookie' : cok ,
     'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
     'Referer': 'https://heidong.in/index.php',
     'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6',
}

conn3 = httplib.HTTPSConnection('heidong.in')
conn3.request("GET", '/mission.php',None,get_headers2)
res3=conn3.getresponse()
htm = res3.read();
#print htm
m=re.search(r"(once=)\d{5}",htm)
key = m.group(0)
_url = '/mission.php?'+key
#print _url


value={
    'once':key,
}
values = urllib.urlencode(value)
conn4 = httplib.HTTPSConnection('heidong.in')
conn4.request("GET", _url,values,get_headers2)
res4=conn4.getresponse()
ress4 = res4.read();
print ress4
