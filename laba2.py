'''
Вариант 29.
Шеснадцатиричные числа, у которых 5 справа цифра равна В16, расположенные в порядке не убывания. Четные цифры выводить словами.
'''

import re

def multiple_replace(numbers, dictionary):
    for i, j in dictionary.items():
        numbers = numbers.replace(i, j)
    return numbers

slovar = {'0' : 'ноль ', '1' : 'один ', '2' : 'два ', '3' : 'три ', '4' : 'четыре ',
     '5' : 'пять ', '6' : 'шесть ', '7' : 'семь ', '8' : 'восемь ', '9' : 'девять ',
     'A' : 'десять ', 'B' : 'одиннадцать ', 'C' : 'двенадцать ', 'D' : 'тринадцать ', 'E' : 'четырнадцать ', 'F' : 'пятнадцать '}

final=[]
f = open("test.txt", "r")
while True:
    s = f.readline().split()
    if not s:
        print("")
        break
    for i in s:
        res = re.findall(r"^[0-9A-F]*\d*[B]{1}[0-9A-F]{4}", i)
        if len(res) == 1:
            if len(final)==0:
                final.append(res[0])
            else:
                if int(res[0], 16) >= int(final[-1], 16):
                    final.append(res[0])
    if len(final)==0:
        print("В файле нет нужных значений")


for i in range(len(final)):
    if int(final[i], 16) % 2 == 0:
        final[i] = multiple_replace(final[i], slovar)
print(final)










