from Utils import get_html_text, build_soup
import re

url = 'http://python123.io/ws/demo.html'
text = get_html_text(url)
soup = build_soup(text)
print(soup.find_all('a'))
print('\n')
print(soup.find_all('a', recursive=False))