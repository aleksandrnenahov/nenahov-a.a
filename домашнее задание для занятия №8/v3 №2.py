A = input('Введите вашу строку: ')

n = A.split()

stroka = ''


for i in n:
	x = list(i)
	x.sort()
	a = ''.join(x)
	stroka = stroka + ' ' + a

print(stroka[1:])

