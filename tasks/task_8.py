onset: int = int(input("Введите начало диапазона: "))
end: int = int(input("Введите конец диапазона: "))

if onset < end:
    for x in range(onset, end + 1):
        if x % 2 == 0:
            print(x)

elif onset == end:
    if onset and end % 2 != 0:
        print(0)
    else:
        print(onset or end)

else:
    for i in range(end, onset + 1):
        if i % 2 == 0:
            print(i)
