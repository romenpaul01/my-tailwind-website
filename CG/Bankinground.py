
num = float(input("Enter a number: "))

if num == 0:
    print("Rounded number =", 0)
else:
    n = 0
    x = abs(num)

    while x >= 10:
        x = x / 10
        n = n + 1

    while x < 1:
        x = x * 10
        n = n - 1

    d = 3 - n
    x = abs(num) * (10 ** d)

    a = int(x)
    b = x - a

    if b > 0.5 or (b == 0.5 and a % 2 != 0):
        a = a + 1

    result = a / (10 ** d)

    if num < 0:
        result = -result

    print("Rounded number =", result)
