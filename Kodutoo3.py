#17.Напишите программу, печатающую столбик таблицу умножения такого вида:
a=int(input("Какое число умножить от 1 до 10?"))
for i in range(1, 10, 1):
    i=int(i)
    a=int(a)
    b=a*i
    print(f"{a}*{i}={b} \n")
ans = 0
#22. Найти сумму чисел от 100 до 200, кратных 17.
for i in range(100,200):
   if(i % 17 == 0):
       ans += i
print(ans)
#20. Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые делятся на 5 или на 7.
ans = 0
for i in range(1,50):
   if(i % 5 == 0):
       ans += i
   elif(i % 7 == 0):
       ans +=i
print(ans)
#19.    Даны натуральные числа от 35 до 87. Найти и напечатать те из них, которые при делении на 7 дают остаток 1, 2 или 5.
for i in range(35,87):
   if(i % 7 == 1):
       print(i)
   elif(i % 7 == 2):
       print(i)
   elif(i % 7 == 5):
       print(i)
#30.    В программе создаются 2 случайных числа M и N. И выводятся на экран в срочку 2 последовательности от N к M, и обратно  .
import random
m=random.randint(1,10)
n=5
print (f"Количество котлет для жарки = {m}, максимальное количество котлет на сковородке = {n}")
if n>=m:
    print("Все пожарит на 1 сковородке")
elif m==0:
    print("Все пожарит на 1 сковородке")
else:
    m %= n
    print(f"Останется дожарит {m} котлет")
#9.    В банк на трехпроцентный вклад положили S евро. Какой станет сумма вклада через N лет?
i=int(input("На сколько лет делаем вклад? "))+1
s=int(input("Сколько кладем денег? "))
for i in range(1,i):
   s=s*1.03
   s=round(s,2)
   print(f"Через {i} лет у вас будет {s}$")
#8.    Составьте программу, которая печатает таблицу перевода расстояний из дюймов в сантиметры (1 дюйм =2,5 см) для значений длин от 1 до 20 дюймов.
for i in range(1,21):
   h=i*2.5
   print(f"{i} дюймов будет {h} в см ")
#7.    Вывести на экран числа, кратные К из промежутка [А,В].
a=int(input("Введите наименьшее число для промежутка"))
b=int(input("Введите наибольшее число для промежутка"))
k=int(input("Введите кратное число для промежутка"))
for i in range(a,b):
   if(i % k == 0):
       print(i)
#   Вводят 15 чисел. Определить, сколько среди них целых.
b=0
for i in range(0,15):
    a=int(input("Введите число: "))
    if a>=0:
        b=b+1
print(f"Среди введеных вами чисел, целыми оказались {b} чисел")
#Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
a=int(input("Введите число "))
summ=0
if a<=0:
    print("Вы ввели 0 или ненатуральное число")
else:
    for i in range (1, a+1):
        summ=i+summ
    print(f"Сумма всех натуральных чисел с 1 до {a} равна {summ}")
