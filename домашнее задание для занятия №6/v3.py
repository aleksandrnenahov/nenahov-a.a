stroka = input('Введите вашу строку: ')

deleted = stroka.count('.')

stroka2 = ' '.join(stroka.split('.'))

print('>>' + stroka2 + '<<' ,'Количество удаленных символов: ' + str(deleted))