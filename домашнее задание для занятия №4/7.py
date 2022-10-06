n = int(input('Введите натуральное число n: '))
while n <= 0:
	print('Ошибка! Вы ввели ненатуральное число!')
	n = int(input('Введите натуральное число n: '))



summa = 0 
s = 1

for i in range(1,n + 1):
	m = s * i 
	summa += m 
	s = m 

print(summa)