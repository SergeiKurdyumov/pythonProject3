N = abs(int(input('Введите количество элементов: ')))
n = input("Введите цифры через пробел: ").split()
num = list(map(int, n))
if len(num) != N or N == 0:
    print('колличество введённых символов не соответствует заданной длинне!')
else:
    X = int(input('Введите число, с которым необходимо сравнивать цифры из списка: '))
    min = abs(X - num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - num[i])
        if count < min:
            min = count
            index = i
    print(f'Число {num[index]} в списке наиболее близко по величине к числу {X}, их разница составляет {abs(X - num[index])}')
