from  Utils import get_html_text, build_soup

url = 'http://python123.io/ws/demo.html'
text = get_html_text(url)
soup = build_soup(text)
print(soup.a.name)
print(soup.a.parent.name)
print(type(soup.a.name))
