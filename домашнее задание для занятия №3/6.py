a = int(input('Введите число от 1 до 8 для столбца первой доски: '))
while a < 1 or a > 8:
	print('Вы ввели неккоректное число!')
	a = int(input('Введите число от 1 до 8 для столбца первой доски: '))
a1 = int(input('Введите число от 1 до 8 для строки первой доски: '))
while a1 < 1 or a1 > 8:
	print('Вы ввели неккоректное число!')
	a1 = int(input('Введите число от 1 до 8 для строки первой доски: '))
b = int(input('Введите число от 1 до 8 для столбца второй доски: '))
while b < 1 or b > 8:
	print('Вы ввели неккоректное число!')
	b = int(input('Введите число от 1 до 8 для столбца второй доски: '))
b1 = int(input('Введите число от 1 до 8 для строки второй доски: '))
while b1 < 1 or b1 > 8:
	print('Вы ввели неккоректное число!')
	b1 = int(input('Введите число от 1 до 8 для строки второй доски: '))


def func(a,a1,b,b1):
	if (a1 + a1) % 2 == (b + b1) % 2:
		return 'Да'
	else:
		return 'Нет'

print(func(a,a1,b,b1))