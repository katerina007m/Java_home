# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

from random import randint

# new_line_1 = []
# for i in range(10):
#     new_line_1.append(randint(0, 9))
#
# new_line_2 = []
# for i in range(10):
#     new_line_2.append(randint(0, 9))
#
# print(new_line_1)
# print(new_line_2)
# new_line_3 = new_line_1+new_line_2
# repeated_elements = set()
# setnewline3 = set(new_line_3)
# for element in setnewline3:
#     if element in new_line_1 and element in new_line_2:
#         repeated_elements.add(element)
# print(sorted(repeated_elements))

#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
#Она растет на круглой грядке, причем кусты высажены только по окружности.
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i- ом кусте
#выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники.
#Эта система состоит из управляющего модуля нескольких собирающих модулей. Собирающий модуль за один заход, находясь
#непосредственно перед кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
#находясь перед некоторым кустом заданной во входном файле грядки.

n = int(randint(4,6))
print(f'Количество кустов: {n}')
arr = []
for i in range(n):
    arr.append(randint(0, 9))
print(arr)

arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
    arr_count.append(arr[-2] + arr[-1] + arr[0])
print(max(arr_count))