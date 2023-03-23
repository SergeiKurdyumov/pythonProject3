N = abs(int(input('Введите количество элементов: ')))
n = input("Введите цифры через пробел: ").split()
num = list(map(int, n))
if len(num) != N:
    print('колличество введённых символов не соответствует заданной длинне!')
else:
    X = int(input('Введите число, которое нужно найти : '))
    count = 0
    for i in range(N):
        if num[i] == X:
            count += 1
    print(f'Число {X} встречается {count} раз')