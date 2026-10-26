
def f(x):
    return x**3 - 7*x + 4

def df(x):
    return 3*x**2 - 7

x = float(input("Enter initial value: "))

while True:
    y = x - f(x) / df(x)

    if abs(y - x) < 0.001:
        break

    x = y
print("Root =", round(y, 3))