print("Таблица умножения с помощью цикла for:")
num = int(input("Введите число: "))

for x in range(1, 11):
    print(num, "*", x, "=", x * num)

print("Таблица умножения с помощью цикла while:")
num = int(input("Введите число: "))
num_2 = 1
while 0 < num_2 < 11:
    print(num, "*", num_2, "=", num * num_2)
    num_2 += 1
