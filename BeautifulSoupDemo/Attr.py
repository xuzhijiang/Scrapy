from Utils import get_html_text, build_soup

url = 'http://python123.io/ws/demo.html'
text = get_html_text(url)
soup = build_soup(text)
tag = soup.a
print(tag.attrs)
print(type(tag.attrs))
print(tag.attrs['class'])
print(tag.attrs['href'])
print(type(tag.attrs['class']))
print(type(tag.attrs['href']))