onset: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if onset == end or (onset < 0 or end < 0):
    print("Некорректный диапазон")

else:
    flag = False
    # if onset > end:
    #     onset, end = end, onset

    onset, end = max()
    for num in range(onset, end + 1):

        num_digits = len(str(num))
        sum_of_digits = 0
        temp_num = num
        while temp_num > 0:
            digit = temp_num % 10
            sum_of_digits += digit ** num_digits
            temp_num //= 10

        if num == sum_of_digits:
            print(num, end=" ")
            flag = True

    if not flag:  # то же самое, что flag != True
        print("В указанном диапазоне нет чисел Армстронга")
