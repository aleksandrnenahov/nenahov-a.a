n = int(input('Введите первую сторону шоколадки: '))
m = int(input('Введите вторую сторону шоколадки: '))
k = int(input('Введите кол-во долек: '))

def func(n,m,k):
	if k < n * m and (k % n == 0 or k % m == 0):
		return 'Да'
	else:
		return 'Нет'

print(func(n,m,k))