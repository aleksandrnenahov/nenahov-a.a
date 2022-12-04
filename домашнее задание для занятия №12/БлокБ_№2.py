l=[]
def f(l):
	n=int(input('Введите число: '))
	if n == 0:
		return l
	l.append(n)
	return f(l)


a=f(l)
a.sort()
print('Второе по величине число: ',a[-2])