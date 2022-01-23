"""
Напишите программу, которая принимает на вход список чисел и число, после чего выводит все позиции, на которых это число встречается в переданном списке.

Позиции в списке нумеруются с нуля.
Если число x не найдено в списке, нужно вывести строку "None" (без кавычек, с большой буквы).

Формат ввода:
На первой строке содержатся значения списка -- целые числа, разделённые пробелом. На второй строке содержится целое число, позиции которого нужно найти.

Формат вывода:
Одна строка, в которой содержится слово "None" или через пробел перечислены числа -- позиции, на которых число x встречается в списке lst. Позиции должны быть выведены в порядке возрастания.
"""


input_list = [int(x) for x in input().split()]
input_num = int(input())
index_list = []
for ind, num in enumerate(input_list):
    if input_num == num:
        index_list.append(ind)
if index_list:
    print(" ".join(map(str, index_list)))
else:
    print("None")