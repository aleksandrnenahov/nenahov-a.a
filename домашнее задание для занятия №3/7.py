n = int(input('Введите натуральное число(>0): '))
while n <= 0:
	print('Ошибка! Число не является натуральным')
	n = int(input('Введите натуральное число(>0): '))




def func(c):
	if c % 4 == 0 and c % 100 != 0 or c % 400 == 0:
		return 'Да'
	else:
		return 'Нет'

print(func(n))
