#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
from random import randint
import math

def GetValueByUser(Num):
    while True:
        getnum = input(Num)
        if getnum.isdigit():
            return getnum


def GetNewArray(size):
    arr = [randint(1, 10) for x in range(size)]
    return arr


def ClosestNumber(array, Number):
    num = 0
    minrange = 10
    for i in range(len(array)):
        if array[i] == Number:
            num = array [i]
        else:
            if minrange > abs(Number - array[i]):
                num = array [i]
                minrange = abs(Number - array[i])
    return num


N = int(GetValueByUser('Введите число N (положительное): '))
NewArray = GetNewArray(N)
print(NewArray)
X = int(GetValueByUser('Введите число X (положительное), которое хотите найти в массиве: '))
N = ClosestNumber(NewArray, X)
print('Число, ближайшее по значению, либо равное Х  - ', N)