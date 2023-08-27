onset: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if (onset < 0) or (end < 0):
    print("Указан неверный диапазон!")
    if onset > end:
        while temp_num > 0:
            digit = temp_num % 10
            sum_of_digits += digit ** num_digits
            temp_num //= 10