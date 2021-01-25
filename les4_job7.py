#7. Реализовать генератор с помощью функции 
#с ключевым словом yield, создающим очередное значение. 
#При вызове функции должен создаваться объект-генератор. 
#Функция должна вызываться следующим образом:
# for el in fact(n).
#Функция отвечает за получение факториала числа, 
#а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

#Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def ft(n):
    fact_fin = 1
    for i in range(n):
        fact_fin *= (i + 1)
    return fact_fin

def fact_2(n):
    factorial = 1
    for i in n:
        factorial *= int(i)
        yield factorial

fact_st = int(input('Факториал какого числа посчитаем?'))

#в1
fact_f = ft(fact_st)
print('Факториал числа ', fact_st, ' = ', fact_f)

#в2
num =[]
for i in range(fact_st):
    num.append(i+1)


i = 0

k = fact_2(num)

while i < len(num):
    print(next(k))
    i += 1

#в3
print([el for el in fact_2(num)])

