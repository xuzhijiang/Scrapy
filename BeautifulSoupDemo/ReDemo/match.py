import re

m = re.search(r'[0-9]\d{5}', 'BIT100081 UTC100084')
print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)
print(m.group(0))
print(m.start())
print(m.end())
print(m.span())
