#1. Реализовать скрипт, в котором должна быть 
#предусмотрена функция расчета заработной платы сотрудника. 
#В расчете необходимо использовать формулу: 
#(выработка в часах * ставка в час) + премия. 
#Для выполнения расчета для конкретных значений 
#необходимо запускать скрипт с параметрами.

from  my_module import my_les1
name_forname = input('введи ФИО сотрудника')
work_ur = int(input('отработанное время'))
geld_ur = int(input('ставка в час'))
prize = int(input('премия'))

print( name_forname, ' - зарплата - ', my_les1(work_ur, geld_ur, prize))