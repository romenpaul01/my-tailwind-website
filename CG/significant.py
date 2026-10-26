
num = input("Enter a number: ")

num = num.strip().lstrip('-')

if 'e' in num.lower():
    num = num.lower().split('e')[0]

if '.' in num:
    num = num.replace('.', '').lstrip('0')
else:
    num = num.strip('0')

print("Significant digits =", len(num))
