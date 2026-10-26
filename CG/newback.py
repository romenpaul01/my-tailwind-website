
x = [20, 30, 40, 50, 60, 70, 80]
y = [102, 108, 115, 124, 135, 148, 163]

value = 75
h = x[1] - x[0]
u = (value - x[6]) / h

d1 = [y[i+1] - y[i] for i in range(6)]
d2 = [d1[i+1] - d1[i] for i in range(5)]
d3 = [d2[i+1] - d2[i] for i in range(4)]
d4 = [d3[i+1] - d3[i] for i in range(3)]
d5 = [d4[i+1] - d4[i] for i in range(2)]
d6 = d5[1] - d5[0]

ans = (y[6] + u*d1[5]
       + u*(u+1)/2*d2[4]
       + u*(u+1)*(u+2)/6*d3[3]
       + u*(u+1)*(u+2)*(u+3)/24*d4[2]
       + u*(u+1)*(u+2)*(u+3)*(u+4)/120*d5[1]
       + u*(u+1)*(u+2)*(u+3)*(u+4)*(u+5)/720*d6)

print("Answer =", ans)
