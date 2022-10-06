a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
while a > b:
	print('Число а должно быть меньше либо равно числу b')
	a = int(input('Введите число a: '))
	b = int(input('Введите число b: '))

for i in range(a,  b + 1):
	print(i)
