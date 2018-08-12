import requests
from bs4 import BeautifulSoup

def get_html_text(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return 'get_html_text failed!'


def build_soup(text):
	return BeautifulSoup(text, 'html.parser')