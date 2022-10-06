n = int(input('Введите натуральное число n <= 9: '))
while n < 0 or n > 9:
	print('Ошибка!Число n должно быть натуральным и быть меньше, либо равно 9!')
	n = int(input('Введите натуральное число n <= 9: '))

for i in range(n):
	for j in range(1, i + 2):
		print(j, end = '')
	print()
	