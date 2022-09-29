a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

def func(z,x,c):
	if z == x == c:
		return '3'
	if (x == z) != c or (c == z) != x or (x == c) != z:
		return '2'
	if z != x != c:
		return '0'

print(func(a,b,c))