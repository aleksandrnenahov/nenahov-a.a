
def func(n):
	hours = n % (60 * 24) // 60
	minutes = n % 60
	return hours, minutes

print(func(10000000))

