num: int = int(input("Введите число: "))

if num < 1:
    print("Число должно быть больше или равно 1")
elif num == 1:
    print(1)
else:
    summa = 0
    for x in range(1, num + 1):
        summa += x
    print("Сумма всех чисел от 1 до", num, "равна:", summa)
