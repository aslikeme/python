
number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))

if number_1 > number_2:
  if number_1 > number_3:
    print(number_1)
  else:
    print(number_3)
else:
  if number_2 > number_3:
    print(number_2)
  else:
    print(number_3)
