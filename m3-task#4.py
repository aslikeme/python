print('Задача 4. Площадь треугольника')

# Напишите программу,
# которая запрашивает у пользователя длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.

# Формула: 
# S = ab/2

kat_a = int(input('Введите длину катета А: '))
kat_b = int(input('Введите длину катета В: '))

square = (kat_a * kat_b) / 2

print("Площадь прямоугольного треугольника равна ", square)