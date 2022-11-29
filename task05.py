# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Введите число: '))

def get_fibonacci(number):
    fibonacciNums = []
    a, b = 1, 1

    for i in range(number):
        fibonacciNums.append(a)
        a, b = b, a + b
    a, b = 1, -1
    for i in range (number):
        fibonacciNums.insert(0, a)
        a, b = b, a - b
    return fibonacciNums

fibonacciNums = get_fibonacci(number)
print(get_fibonacci(number))
print(fibonacciNums.index(1))
