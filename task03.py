# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbersList = list(map(float, input("Введите числа через пробел:\n").split()))
fractionalParts = [round(i%1,2) for i in numbersList if i%1 != 0]
print(f"Максимальная разница между дробными частями:  {max(fractionalParts) - min(fractionalParts)}")