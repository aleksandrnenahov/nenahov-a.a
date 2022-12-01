





print('Задание 2: ')
file =  open('C:/Users/Thermaltake/Desktop/проекты/nenahov-a.a/домашнее задание для занятия №10/НенаховАА_У-222_vvod2.txt','r') 

fiile =  open('C:/Users/Thermaltake/Desktop/проекты/nenahov-a.a/домашнее задание для занятия №10/НенаховАА_У-222_vivod2.txt','w+') 


N = []

c = file.readlines()
for i in range(len(c)):
	N.append((c[i].rstrip()).split())
N1 = []
for i in range(len(N)):
	d = []
	for j in range(len(N[0])):
		d.append(int(N[i][j]))
	N1.append(d)

print('Исходная матрица: ', N1)




def f(n,m):
	for i in range(n-1):
		if max(N1[n - i - 1]) > max(N1[n - i - 2]):
			N1[n-i-1],N1[n-i-2] = N1[n-i-2],N1[n-i-1]
	
	d = []
	for i in range(m):
		c = []
		for j in range(n):
			c.append(N1[j][i])
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
	return u

g = f(len(N1),len(N1[0]))
N2 = []
for i in range(len(g)):
	d = []
	for j in range(len(g[0])):
		d.append(str(g[i][j]))
	N2.append(d)

for i in range(len(N2)):
	fiile.write(' '.join(N2[i]) +'\n')




