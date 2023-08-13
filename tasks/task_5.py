num: int = int(input("Введите число: "))

if num < 0:
    print("Факториал определен только для натуральных чисел.")
else:
    factorial: int = 1
    for x in range(2, num + 1):
        factorial *= x
    print("Факториал числа", num, "равен", factorial)
