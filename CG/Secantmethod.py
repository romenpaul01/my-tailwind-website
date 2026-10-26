
def f(x):
    return 2*x**3 - 2*x - 5

x0 = 0
x1 = 1

while f(x0)*f(x1) > 0:
    x0 = x1
    x1 = x1 + 1

while True:
    x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))

    if abs(x2-x1) < 0.001:
        break

    x0 = x1
    x1 = x2

print("Root =", round(x2, 2))
