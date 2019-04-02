# -*- coding: utf-8 -*-
# 爬爬虫网站的爬虫
# appbot.co 后端没有对js的请求进行校验，导致可以直接自定义收取json条目数目，从而导致一个请求直接拿到所有数据
# Api 生成算法：
# message= "/data/apps/1505993/reviews count='10' end='2019-01-13' page='3' start='2018-10-15'"
# key= window._____.k = "aea3104db25bbe02386fe48ca6e9104e1611b04d"
# HMAC-SHA1 加密生成 s

import requests
import urllib
import hmac
import sys
try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse
from hashlib import sha1
from pdb import set_trace as bp
import json
s = requests.Session()
mycookie=sys.argv[1]
keyStr=sys.argv[2].encode('utf-8')
key = bytearray()
try:
	key.extend(keyStr)
except:
	key.extend(map(ord, keyStr))
baseUrl=sys.argv[3]
query=urlparse(baseUrl).query.split('&')
appId=query[0].strip('app=')
startDate=query[1].strip('start=')
endDate=query[2].strip('end=')
i=1;
while True:
	print("crawling...please wait...");
	url='https://app.appbot.co/data/apps/'+appId+'/reviews?start='+startDate+'&end='+endDate+'&count=5000&page='+str(i)
	raw="/data/apps/"+appId+"/reviews count='5000' end='"+endDate+"' page='"+str(i)+"' start='"+startDate+"'"
	hashed = hmac.new(key, raw.encode('utf-8'), sha1)
	#print(hashed.hexdigest())
	#print(raw)
	s.headers.update({'s': hashed.hexdigest(),'Cookie':'_appbot_session='+mycookie+';'})
	#print(s.headers)
	#bp()
	r=s.get(url).json()
	if len(r['reviews'])==0:
		break
	with open('AppId'+appId+'From'+startDate+'To'+endDate+'_'+str(i)+'.json', 'w') as outfile:
		json.dump(r, outfile)
	i=i+1

print('crawl Finished!');
