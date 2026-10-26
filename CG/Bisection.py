
def f(x):
    return 2*x**3 - 2*x - 5

a = 0
b = 1

while f(a)*f(b) > 0:
    a = b
    b = b + 1

while True:
    c = (a + b) / 2

    if abs(f(c)) < 0.01:
        break

    if f(a)*f(c) < 0:
        b = c
    else:
        a = c

print("Root =", round(c, 2))
