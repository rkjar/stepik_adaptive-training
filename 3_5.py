"""
Напишите программу, которая выводит nn первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно).

Формат ввода:
Строка, содержащая одно целое число nn, n \gt 0n>0.

Формат вывода:
Строка, содержащая требуемую последовательность чисел, разделённых пробелом.

Sample Input:

7
Sample Output:

1 2 2 3 3 3 4
"""

user_input = input()

nums = []
s = ''
num = int(user_input)
for i in range(1, num + 1):
    nums += (i * str(i))
for elements in nums[:num]:
    s += elements + " "
print(s[0:-1])