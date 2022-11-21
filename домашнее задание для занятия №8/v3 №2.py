def f(A):
	n = A.split()
	stroka = ''
	for i in n:
		x = list(i)
		x.sort()
		a = ''.join(x)
		stroka = stroka + ' ' + a
	return stroka

print(f(input('Введите вашу строку:')))

