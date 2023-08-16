onset: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if onset > end:
    onset, end = end, onset

for i in range(onset, end + 1):
    if i % 2 == 0:
        print(i)
    elif onset == end and i % 2 != 0:
        print(0)
