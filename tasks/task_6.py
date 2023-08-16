num: int = abs(int(input()))

i: int = 0 if num > 0 else 1
while num > 0:
    last_digit = num % 10
    num //= 10  # num = num // 10
    i += 1

print('Количество цифр в числе:', i)

# -----------------------

# num = 123
#
# # %
# # //
# # --------------------
#
# print(num)
# last = num % 10
# print(last)
#
# print('---------------------')
# num = num // 10
# print(num)
#
# last = num % 10
# print(last)
#
# print('---------------------')
# num = num // 10
# print(num)
#
# last = num % 10
# print(last)

# -------------------------
# num = int(input())
#
# num_copy = num
# prod = 1
# i = 1
# while num > 0:
#     last_digit = num % 10
#     prod *= last_digit
#     print('Последняя цифра в', i, 'итерации', last_digit)
#     num = num // 10
#     print('Отбросили цифру', num)
#     print('------------\n')
#
#     i += 1
#
# print(i)
# print(prod)
# print(num_copy, num)
