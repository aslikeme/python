print('Задача 5. Часы')

# Напишите программу, 
# которая получает на вход число n — количество минут, — затем считает,
# 1) сколько это будет в часах 
# 2) сколько минут останется
# и выводит на экран эти два результата.
# (В вычислениях вам помогут операции // и %)

n = int(input('Введите количество минут: '))

hours = n // 60
minutes = n % 60

print('В часах это будет ', hours)
print('Остаток минут ', minutes)