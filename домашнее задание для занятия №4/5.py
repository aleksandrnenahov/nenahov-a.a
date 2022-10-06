n = int(input('Введите число n > 0: '))
while n <= 0:
	print('Ошибка! число должно быть натуральным!')
	n = int(input('Введите число n > 0: '))

sum_v_kube = 0

for i in range(1, n + 1):
	sum_v_kube += i ** 3

print(sum_v_kube)
