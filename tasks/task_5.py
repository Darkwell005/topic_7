num: int = int(input("Введите число: "))
factorial = 1
if num < 0:
    print("Факториал определен только для натуральных чисел.")
else:
    if num >= 0:
        for num in range(2, num + 1):
            factorial *= num
        print("Факториал числа", num, "равен", factorial)

