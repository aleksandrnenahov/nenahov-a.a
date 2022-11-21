
def f(n,m):
	a = []
	for i in range(n):
		b = []
		for j in range(m):
			print('Введите [',i,',',j,'] элемент')
			b.append(int(input()))
		a.append(b)
	
	#изначальная матрица
	print('Исходная матрица: ')
	for i in range(n):
		for j in range(m):
			print(a[i][j], end = ' ')
		print()
	
	
	for i in range(n-1):
		if max(a[n - i - 1]) > max(a[n - i - 2]):
			a[n-i-1],a[n-i-2] = a[n-i-2],a[n-i-1]
	
	d = []
	for i in range(m):
		c = []
		for j in range(n):
			c.append(a[j][i])
		d.append(c)
	
	
	for i in range(m-1):
		if max(d[m - i - 1]) > max(d[m - i - 2]):
			d[m-i-1],d[m-i-2] = d[m-i-2],d[m-i-1]
	
	u = []
	
	for i in range(n):
		t = []
		for j in range(m):
			t.append(d[j][i])
		u.append(t)
	print('Измененнная матрица: ')
	for i in range(n):
		for j in range(m):
			print(u[i][j], end = ' ')
		print()

f(int(input('Введите количество строк в матрице: ')),int(input('Введите количество столбцов в матрице: ')))


