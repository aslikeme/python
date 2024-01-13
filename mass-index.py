height = float(input('Рост: '))
weight = float(input('Вес: '))

index = round(weight / (height ** 2),2)
print('Ваш индекс массы тела: ', index)
if index < 18.5:
    print('недобор')
elif 18.5 <= index < 25:
    print('норма')
elif 25 <= index < 30:
    print('избыток')
elif 30 <= index:
    print('ожирение')    

 