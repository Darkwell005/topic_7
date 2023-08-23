num: int = int(input("Введите целое положительное число: "))

x = 0
while x < num:
    i = 0
    x += 1
    while i < x:
        print(x, end=" ")
        i += 1
    print()

# -----
i = 1
while i <= num:
    j = 0
    while j < i:
        print(i, end=" ")
        j += 1
    print()
    i += 1

# -----

for i in range(1, num + 1):
    for j in range(i):
        print(i, end=" ")
    print()
