n = int(input('Введите число n > 0: '))
while n <= 0:
	print('Ошибка! число n должно быть натуральным!')
	n = int(input('Введите число n > 0: '))

factorial = 1

for i in range(1, n + 1):
	factorial *= i

print('Факториал числа ' + str(n) + ' равен: ',factorial)
