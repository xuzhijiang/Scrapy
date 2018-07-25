from bs4 import BeautifulSoup
from Utils import get_html_text, build_soup

url = 'http://python123.io/ws/demo.html'
text = get_html_text(url)
soup = build_soup(text)
print(soup.title)
print(soup.a)
print(type(soup.a))
print(type(soup.title))
