# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def listOfPairedProducts(lst):
    l = len(listOfNumbers)//2 + 1 if len(listOfNumbers) % 2 != 0 else len(listOfNumbers)//2
    new_list = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(new_list)

listOfNumbers = list(map(int, input("Введите список чисел через пробел:\n").split()))
listOfPairedProducts(listOfNumbers)