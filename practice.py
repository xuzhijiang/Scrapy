"""
# get JD information
import requests
url = "https://item.jd.com/2967929.html"
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("spider failed!")
"""


"""
# get information from amazon
# modify user-agent
import requests
url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
	kv = {'user-agent' : 'Chrome/10'}
	r = requests.get(url, headers = kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print('get information from amazon failed!')
"""


'''
# BaiDu/360 search keyword
# http://www.baidu.com/s?wd=keyword
# http://www.so.com/s?q=keyword
import requests

url = "http://www.baidu.com/s"
# url = "http://www.so.com/s"
keyword = "stock"
try:
	kv = {'wd': keyword}
	r = request.get(url, params=kv)
	print(r.request.url)
	r.raise_for_status
	print(len(r.text))
except:
	print("spider failed!")
'''

'''
# 网络图片的爬取
import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "D://pics//"
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, "wb") as f:
			f.write(r.content)
			f.close()
			print("save successfully")
	else:
		print("file already exists!")
except:
	print("spider failed!")
'''

'''
# ip地址查询
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
	r = requests.get(url + '202.204.80.112')
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])
except:
	print("IP address query failed!")
'''
