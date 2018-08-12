import re

match = re.match(r'[0-9]\d{5}', 'BIT 100081')
if match:
	print(match.group(0))
else:
	print('match is NoneType')

# print(match.group(0))

match = re.match(r'[0-9]\d{5}', '100081 BIT')
if match:
	print(match.group(0))