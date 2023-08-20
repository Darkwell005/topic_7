n: int = int(input("Введите число: "))

largest_prime_num: int = 2

while largest_prime_num <= n:
    if n % largest_prime_num != 0:
        largest_prime_num += 1
    else:
        n //= largest_prime_num
        print(largest_prime_num, end=" ")
