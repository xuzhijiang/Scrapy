from Utils import get_html_text, build_soup

url = 'http://python123.io/ws/demo.html'
text = get_html_text(url)
soup = build_soup(text)
for link in soup.find_all('a'):
	print(link.get('href'))