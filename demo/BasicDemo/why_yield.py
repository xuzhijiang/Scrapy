def gen(n):
	for i in range(n):
		yield i**2

for i in gen(6):
	print('i=%s\n' % i)

print('-------')

def square(n):
	ls = [i**2 for i in range(n)]
	return ls

for i in square(6):
	print('i=%s\n' % i)
