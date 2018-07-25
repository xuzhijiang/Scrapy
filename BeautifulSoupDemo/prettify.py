from Utils import get_html_text
from bs4 import BeautifulSoup


def prettify_html_text(text):
    soup = BeautifulSoup(text, 'html.parser')
    print(soup.prettify())


url = 'http://python123.io/ws/demo.html'
text = get_html_text(url)
prettify_html_text(text)
