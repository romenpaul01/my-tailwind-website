
def f(x):
    return x**3 - 4*x - 9

a = 0
b = 1

while f(a)*f(b) > 0:
    a = b
    b = b + 1

while True:
    c = (a*f(b) - b*f(a)) / (f(b) - f(a))

    if abs(f(c)) < 0.01:
        break

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print("Root =", round(c, 2))
