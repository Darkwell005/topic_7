# Исходный список строковых объектов
numbers: list = [
    "105", "42", "98", "120", "84", "80", "110", "119", "130", "99"
]

print("Числа, кратные 5 или 7 и больше 100:", end=" ")
for x in numbers:
    x: int = int(x)
    if ((x % 5 == 0) or (x % 7 == 0)) and x > 100:
        print(x, end=" ")
