def count_number_len(x):
    count = 0
    while x:
        count += 1
        x //= 10
    print(count)

count_number_len(10)        