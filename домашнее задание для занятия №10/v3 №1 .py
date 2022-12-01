
print('Задание 1: ')
file =  open('C:/Users/Thermaltake/Desktop/проекты/nenahov-a.a/домашнее задание для занятия №10/НенаховАА_У-222_vvod1.txt','r') 

fiile =  open('C:/Users/Thermaltake/Desktop/проекты/nenahov-a.a/домашнее задание для занятия №10/НенаховАА_У-222_vivod1.txt','w+') 


N = []

c = file.readlines()
for i in range(len(c)):
	N.append((c[i].rstrip()).split())
print(N)

def f(x):

	m = len(c) 	
	count = 0
	
	for i in range(len(c)):
		for j in range(1,len(c)):
			if N[i][j] == N[j][i]:
				count += 1
	if count == (len(c) * (len(c) - 1)):
		fiile.write('Матрица симметрична!')
		fiile.close()
	else:
		fiile.write('Матрица несимметрична!')
		fiile.close()

f(N)



