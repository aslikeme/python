print('Введите местоположение коня: \n')
chessPosX = float(input())
chessPosY = float(input())
print('Введите местоположение точки на доске: \n')
boardPosX = float(input())
boardPosY = float(input())

x = int(chessPosX * 10)
y = int(chessPosY * 10)
bx = int(boardPosX * 10)
by = int(boardPosY * 10)

print('Конь в клетке (',x,',',y,'). Точка в клетке (',bx,',',by,')')

if (abs(y - by) == 2 and abs(x - bx) == 1) or (abs(x - bx) == 2 and abs(y - by) == 1):
    print('Да, конь может ходить в эту точку.')
else:
    print('Нет, конь не может ходить в эту точку.')     