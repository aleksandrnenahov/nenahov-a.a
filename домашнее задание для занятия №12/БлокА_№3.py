
def f(n):
	if len(n) == 0:
		return n 
	else:
		return f(n[1:]) + n[0]

numb = str(input('Введите ваше число: '))
print(f(numb))

