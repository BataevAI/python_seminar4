# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел. 


lst1 = list((input('Введите целые числа, список1 \n')).split())
lst1 = [int(s) for s in lst1]

lst2 = list((input('Введите целые числа, список2 \n')).split())
lst2 = [int(s) for s in lst2]

print(lst1)
print(lst2)

set_s = set(lst1).intersection(set(lst2))
lst_total = []
for item in set_s: lst_total.append(item)

lst_total.sort()
print(f'итоговый список: {lst_total}')