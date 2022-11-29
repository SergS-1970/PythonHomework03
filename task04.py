# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number10 = int(input("Введите десятичное число:\n"))
binaryNumber = ""
while number10 != 0:
    binaryNumber = str(number10%2) + binaryNumber
    number10 //=2
print(f"Двоичная форма будет выглядеть как {binaryNumber}")