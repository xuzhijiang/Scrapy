import re

for m in re.finditer(r'[0-9]\d{5}', 'BIT100081 UTC100084'):
	if m:
		print(m.group(0))