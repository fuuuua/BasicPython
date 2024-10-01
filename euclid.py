def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

result = gcd(10, 20)
print("2つの最大公約数は:", result)

result = gcd(14, 91)
print("2つの最大公約数は:", result)

result = gcd(91, 14)
print("2つの最大公約数は:", result)