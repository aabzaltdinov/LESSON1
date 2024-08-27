first = int(input('введите число: '))
second = int(input('введите число: '))
third = int(input('введите число: '))

if first == second == third:
    print('вывод :3')
elif first == second or first == third or second == third:
    print('вывод :2')
else:
    print('вывод :0')
