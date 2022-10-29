N = int(input('Введите натуральное число N: '))

while N < 1:
    print('Вы ввели ненатуральное число!')
    N = int(input('Введите натуральное число N: '))


c= 1
count = 0

while c <= N:
    c *= 2
    count += 1
print(count - 1, c // 2)