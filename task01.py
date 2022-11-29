# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

numbers = []
for element in input().split():
    numbers.append(int(element))

sumOfOddPositions = 0
for i in range(1, len(numbers), 2):
    sumOfOddPositions += numbers[i]
print(
    f"Для списка {numbers} сумма элементов на нечётных позициях: {sumOfOddPositions}")
