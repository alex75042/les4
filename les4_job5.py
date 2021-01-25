#5. Реализовать формирование списка, 
#используя функцию range() и возможности генератора. 
#В список должны войти четные числа от 100 до 1000 (включая границы). 
#Необходимо получить результат вычисления произведения
# всех элементов списка.

#Подсказка: использовать функцию reduce().
from functools import reduce

el_list = []
for i in range(100, 1001, 2):
    el_list.append(i)

print(reduce(lambda x, y: x * y, el_list))

#mult_el = reduce(lambda x, y: x * y, el_list)

#print(mult_el)


