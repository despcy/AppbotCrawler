# -*- coding: utf-8 -*-
# 爬爬虫网站的爬虫
# appbot.co 后端没有对js的请求进行校验，导致可以直接自定义收取json条目数目，从而导致一个请求直接拿到所有数据
# Api 生成算法：
# message= "/data/apps/1505993/reviews count='10' end='2019-01-13' page='3' start='2018-10-15'"
# key= window._____.k = "aea3104db25bbe02386fe48ca6e9104e1611b04d"
# HMAC-SHA1 加密生成 s
# 所有需要的参数自己添加，我懒得写了

import requests
import urllib
import hmac
from hashlib import sha1
from pdb import set_trace as bp
import json
s = requests.Session()
mycookie="appbot_convert={%22referer%22:%22https://www.google.com/%22%2C%22landing%22:%22https://appbot.co/%22}; _ga=GA1.2.678209996.1545190278; intercom-id-glvjson7=87213707-f555-4612-be42-3f5886db93c5; _gid=GA1.2.53426666.1547361286; filterOpen=true; cookieconsent_status=allow; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaGJDRnNHYVFMQW1TSWlKREpoSkRFd0pIQTRWVkYwT1dSMFVUQnBVbEpGWTFCUVZHaERTVTlKSWhZeE5UUTNNemcxTnprNUxqTTJOVE16TlFZNkJrVkciLCJleHAiOiIyMDE5LTA0LTEzVDEzOjIzOjE5LjM2NVoiLCJwdXIiOm51bGx9fQ%3D%3D--89ed958726019192e450edba95e72018b9d77f3e; appbot_session_active=true; _hp2_ses_props.116503402=%7B%22r%22%3A%22https%3A%2F%2Fappbot.co%2F%22%2C%22ts%22%3A1547389679869%2C%22d%22%3A%22app.appbot.co%22%2C%22h%22%3A%22%2Freviews%22%7D; _hp2_id.116503402=%7B%22userId%22%3A%221523576842408228%22%2C%22pageviewId%22%3A%221552147591347385%22%2C%22sessionId%22%3A%228440837272881460%22%2C%22identity%22%3A%22tes333333t1uci%40uci.edu%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%2C%22oldIdentity%22%3Anull%7D; intercom-session-glvjson7=ZkFhSWVrNTNxa2Q1Nmt6RktPa0J5bHlpbGVkRUhGQ0tkQ1dsR1Nzcm40VVl0SE45V0lLcmUwcjExUkttdFptTC0teTNqbExkTHpaUE00OFViY0FJN21zdz09--7b18e5cae5c749dfde68a954e3381864fc7e4c4e; _appbot_session=%2FVPuomCOK68tRRe15%2BOwOLhNv9%2Baa59H29L%2FS2xpcuK4%2Fs3tbVPpT%2BznlqUpFrBNSqqGTaX%2FE7SELv7u9tce38gJopiGJJB07gbgu6yOgN%2F9306Wez0xGHTCkBewaCbJtKWhQ1bozPiNqertzIvn3RmaA4yudQa7Xayl201aDAxJ%2FbasTaqsRC9w8EjLlpg80gPcVQIPma%2FFI6autdg3AS5Q%2F7FZKL9zxRmhPc1gKY5lY3Dl5G49sJf686IGOlcpwNZCYMMHYlqoyi0o70fXoPAZZRQD3Ox5LjmPCOu4H54TY%2BHai1vEQXXQ3qFbyF8bM5tM%2BhXmR07ZJUTwc3isj%2Bmaj6ksxHTmtr6YwSCh1cIFvuJgLIQwmdsQlZUY1Duj13BptfVxCCGWHv0jOXvAb7UDcgviOSZm6SnHuP4D%2BiHosJsf7AmRh2dc%2BelYyGVMJBsSWAiP36RViq2fEJjECc%2FDgJE%2FZ3mh09zIo6djcZJ8tznX--zA6YbOsIjaR%2BTyzm--xGPUeUpiHrr93wzeDTGTRQ%3D%3D"
key="231c8f45cea2e54da080551592561985817ed2c0"
i=1;
while True:
	url='https://app.appbot.co/data/apps/1505993/reviews?start=2008-07-10&end=2019-01-13&count=5000&page='+str(i)
	raw="/data/apps/1505993/reviews count='5000' end='2019-01-13' page='"+str(i)+"' start='2008-07-10'"
	hashed = hmac.new(key, raw, sha1)
	s.headers.update({'s': hashed.hexdigest(),'cookie':mycookie})
	print(hashed.hexdigest())
	print(raw)
	r=s.get(url).json()
	if len(r['reviews'])==0:
		break
	with open('Google'+str(i)+'.json', 'w') as outfile:
		json.dump(r, outfile)
	i=i+1






