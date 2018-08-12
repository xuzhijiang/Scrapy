from Utils import get_html_text, build_soup
import re

url = 'http://python123.io/ws/demo.html'
text = get_html_text(url)
soup = build_soup(text)
# 检索标签名为p，并且属性中包含course的p标签,属性名不一定为course
print(soup.find_all('p', 'course'))
print('\n')
print(soup.find_all(id='link1'))
print('\n')
print(soup.find_all(id='link'))
print('\n')
print(soup.find_all(id=re.compile('link')))