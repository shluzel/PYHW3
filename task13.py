# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X.
from random import randint


def GetValueByUser(Num):
    while True:
        getnum = input(Num)
        if getnum.isdigit():
            return getnum


def GetNewArray(size):
    arr = [randint(1, 10) for x in range(size)]
    return arr


def CountNumber(array, Number):
    count = 0
    for i in range(len(array)):
        if array[i] == Number:
            count = count+1
    return count


N = int(GetValueByUser('Введите число N (положительное): '))
NewArray = GetNewArray(N)
print(NewArray)
X = int(GetValueByUser('Введите число X (положительное), которое хотите найти в массиве: '))
print('Число', X, 'Встречается в массиве', CountNumber(NewArray, X), 'раз.')
