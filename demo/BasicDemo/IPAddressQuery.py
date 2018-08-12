import requests

ipAddr = '202.204.80.112'
url = 'http://m.ip138.com/ip.asp'
ip = {'ip': ipAddr}

try:
	r = requests.get(url, params=ip)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.request.url)
	# 获取倒数第500个开始到最后的字符
	print(r.text[-500:])
except:
	print('ip address query failed!')