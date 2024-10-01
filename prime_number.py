a = 61
b = 10

if a <= 1:
    print(False)
else:
    is_prime_a = True
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            is_prime_a = False
            break
print(is_prime_a)

if b <= 1:
    print(False)
else:
    is_prime_b = True
    for i in range(2, int(b**0.5)+1):
        if b % i == 0:
            is_prime_b = False
            break
print(is_prime_b)