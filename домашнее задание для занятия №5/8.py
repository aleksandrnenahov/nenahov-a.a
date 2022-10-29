
length = 1
max_length = 1
x = 1
y = 1
cnt = 1


while x != 0:
	x = int(input('Введите натурально число: '))
	if y == x:
		length += 1
	else:
		if length > max_length:
			max_length = length
		length = 1
	y = x 
	cnt += 1

print('Наибольшая длина последовательности одинаковых символов, идущих подряд, равна ' + str(max_length))