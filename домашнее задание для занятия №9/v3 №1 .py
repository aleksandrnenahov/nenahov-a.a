n = int(input('Введите количество строк и столбцов квадратной матрицы: '))
m = n 

a = []

for i in range(n):
	b = []
	for j in range(m):
		print('Введите [',i,',',j,'] элемент')
		b.append(int(input()))
	a.append(b)

print('Исходный массив: ')
for i in range(n):
	for j in range(m):
		print(a[i][j], end = ' ')
	print()

count = 0

for i in range(n):
	for j in range(1,n):
		if a[i][j] == a[j][i]:
			count += 1
if count == (n * (n - 1)):
	print('Матрица симметрична!')
else:
	print('Матрица несимметрична!')




