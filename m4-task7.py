hours = int(input('Введите количество отработанных часов: '))
credit = int(input('Введите остаток по кредиту: '))
food = int(input('Введите количество денег на еду: '))

earning = ((200 * hours) / 2**3) + hours
expenses = credit + food

if earning >= expenses:
  print('Часов хватает. Можно отдохнуть')
else:
  print('Часов не хватает. Придётся работать больше!')
