N = int(input('Введите целое число N: '))
cnt = 0 
summary = 0

while cnt != N:
	summary += int(input('Введите число: '))
	cnt += 1
print('Сумма ваших чисел равна: ',summary)
