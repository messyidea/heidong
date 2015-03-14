# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import cookielib
import datetime
import httplib

#用户名和密码
username = 'username'
password = 'password'
login_post_data= {
    'op': 'login',
    'email': username,
    'password': password,
}

def login():
    post_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
	'Connection' : 'keep-alive',
	'Referer':'https://heidong.in/signin.php',
	'Origin':'https://heidong.in',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    #print login_post_data
    post_data = urllib.urlencode(login_post_data)
    conn = httplib.HTTPSConnection('heidong.in', 443)
    conn.request("POST", '/config/userData.php', post_data, post_headers)
    response = conn.getresponse()
    #print 'Login: ', response.status, response.reason
    res1 = response.read()
    cookie = response.getheader("set-cookie")
    #print "cookie == ", cookie
    return cookie


def get_PHPSESSID(cookie):
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
    response2=conn2.getresponse()
    cookie2=response2.getheader("set-cookie")
    mp = cookie2.split(' ')
    mp0 = mp[0]
    #print mp0
    return str(mp0)


def mission(cookie):
    get_headers2 = {
        'Host' : 'heidong.in',
        'Connection' : 'keep-alive' ,
        'Cache-Control' : 'max-age=0',
        'Cookie' : cookie ,
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Referer': 'https://heidong.in/index.php',
        'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6',
    }
    conn3 = httplib.HTTPSConnection('heidong.in')
    conn3.request("GET", '/mission.php',None,get_headers2)
    response3=conn3.getresponse()
    html = response3.read();
    #print html
    m=re.search(r"(once=)\d{5}",html)
    if(m == None) :
        return "yes";
    key = m.group(0);
    _url = '/mission.php?'+key
    value={
        'once':key,
    }
    values = urllib.urlencode(value)
    conn4 = httplib.HTTPSConnection('heidong.in')
    conn4.request("GET", _url,values,get_headers2)
    res4=conn4.getresponse()
    html2 = res4.read();
    m1 = re.search(r'<div class="message">(.{60})',html2)
    m2 = m1.group(0)
    m3 = re.search(r'\d+',m2)
    return m3.group(0);


if __name__ == '__main__':
    cookie1 = login()
    if(cookie1 == None):
        print "账号或密码有误"
        exit(1)
    cookie2 = get_PHPSESSID(cookie1)
    cookie = str(cookie2) + str(cookie1)
    #print "cookie == ", cookie
    result = mission(cookie)
    if(result == "yes"):
        print "你已经签过到"
    else:
        print "今天你获取了 ",result," 金币"

