# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.

print ("Введите размер списка n: ")
n = int(input())
  
list = [round((1+1/i)**i, 3) for i in range(1, n+1)]

print(f"{list} \nСумма: {round(sum(list), 3)}")
