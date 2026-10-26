
x = float(input("Enter initial value: "))

while True:
    y = 1 / (1 + x**2)

    if abs(y - x) < 0.001:
        break

    x = y

print("Root =", round(y, 3))
