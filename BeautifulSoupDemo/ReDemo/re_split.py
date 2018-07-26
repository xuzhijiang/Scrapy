import re

print(re.split(r'[0-9]\d{5}', 'BIT100081 TSU100084'))
print('\n')
print(re.split(r'[0-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1))