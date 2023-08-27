num: int = int(input("Введите целое положительное число: "))

counter: int = 1
for i in range(1, num + 1):
    for j in range(i):
        print(counter, end=" ")
        counter += 1
    print()
