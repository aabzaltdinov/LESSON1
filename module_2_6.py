def get_cod(number):
    cod = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                cod += str(i) + str(j)
    return cod

n = int(input('Введите целое число от 3 до 20: '))

result = get_cod(n)
print('твой ответ :', result)
