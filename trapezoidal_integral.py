from math import sin,pi
# --example--
# print(sin(0))
# >>> 0
# -----------

a =int('0')
b =pi /int('2')
n =int('100')
h =(b-a)/n
S =0

for k in range(1, n+1):
    x1 =a +(k-1)*h
    x2 =a +k*h
    f1 =sin(x1)
    f2 =sin(x2)
    S +=h*(f1+f2)/2
print("{:.10f}".format(S))