height = float(input('Рост: '))
weight = float(input('Вес: '))

index = weight / (height ** 2)

if index < 18.5:
    print('недобор')
elif 18.5 <= index < 25:
    print('норма')
elif 25 <= index < 30:
    print('избыток')
elif 30 <= index:
    print('ожирение')    

 