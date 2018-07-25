from  Utils import get_html_text, build_soup

text = '<b><!--This is a comment!--></b><p>This is not a comment!!</p>'
soup = build_soup(text)
print(soup.b.string)
print(type(soup.b.string))
print(soup.p.string)
print(type(soup.p.string))
