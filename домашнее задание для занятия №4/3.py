a = int(input('Введите число а: '))
b = int(input('Введите число b: '))

while a <= b:
	print('Число а должно быть больше числа b!')
	a = int(input('Введите число a: '))
	b = int(input('Введите число b: '))

for i in range(a,b - 1, -1):
	if i % 2 != 0:
		print(i)