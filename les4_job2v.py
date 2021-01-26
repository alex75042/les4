#2. Представлен список чисел. 
#Необходимо вывести элементы исходного списка, 
#значения которых больше предыдущего элемента.

#Подсказка: элементы, удовлетворяющие условию, 
#оформить в виде списка.
# Для формирования списка использовать генератор.

#Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#Результат: [12, 44, 4, 10, 78, 123].

import random
number_elements = []
fin_number_elements = []
number = int(input('Сколько элементов в списке'))

for i in range(number):
    number_elements.append(int(random.random() *1000))

print(number_elements)

el = 1
#while  el < number - 1:
#    if number_elements[el + 1] > number_elements[el]:
#        fin_number_elements.append(number_elements[el + 1])
#    el +=1
fin_number_elements = [number_elements[el] for el in range(1, number)  if number_elements[el] > number_elements[el - 1]]
print(fin_number_elements)


#print(number_elements, '\n', fin_number_elements)