x = [1, 2, 4]
y = [1, 4, 16]

n = len(x)
d = y.copy()

for j in range(1, n):
    for i in range(n-1, j-1, -1):
        d[i] = (d[i] - d[i-1]) / (x[i] - x[i-j])

value = 3
result = d[n-1]

for i in range(n-2, -1, -1):
    result = result * (value - x[i]) + d[i]

print("Interpolated value =", result)