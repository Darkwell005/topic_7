num: int = int(input("Введите число: "))
print("Таблица умножения для числа", num, "с помощью цикла for:")

for x in range(1, 11):
    print(num, "*", x, "=", x * num)

print("Таблица умножения для числа", num, "с помощью цикла while:")
num_2: int = 1
while 0 < num_2 < 11:
    print(num, "*", num_2, "=", num * num_2)
    num_2 += 1
