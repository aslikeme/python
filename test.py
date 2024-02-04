while True:
    amplitude = int(input("Введите начальную амплитуду: "))
    amplitude_stop = float(input("Введите амплитуду остановки: "))
    count = 0
    if amplitude <= 0 or amplitude_stop <= 0 :
        print("\nОшибка ввода данных. Попробуйте еще раз! \n")
    else:
        while amplitude > amplitude_stop:
            amplitude *= 0.916
            count += 1
    print('Маятник считается остановившимся через ',count, 'колебаний')