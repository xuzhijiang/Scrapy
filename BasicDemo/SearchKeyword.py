import requests

baidu_url = 'http://www.baidu.com/s'
so_url = 'http://www.so.com/s'
keyword = 'stock'

try:
	baidu_kw = {'wd': keyword}
	so_kw = {'q': keyword}
	baidu_r = requests.get(baidu_url, params=baidu_kw)
	so_r = requests.get(so_url, params=so_kw)
	baidu_r.raise_for_status()
	so_r.raise_for_status()
	print(len(baidu_r.text))
	print(len(so_r.text))
	print(baidu_r.request.url)
	print(so_r.request.url)
except:
	print('search failed!!')