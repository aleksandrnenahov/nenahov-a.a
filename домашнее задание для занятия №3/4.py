a = int(input('Введите расстояние между шнурками: '))
b = int(input('Введите расстояние между дырочками в ряду: '))
l = int(input('Введите длину свободного конца шнурка: '))
N = int(input('Введите кол-во дырочек: '))



def func(a,b,l,N):	
	return l * 2 + (N - 1) * 2 * b + a * (N - 1)


print(func(a,b,l,N))