x = input()
res = 0

for i in range(len(x)):
    for digit in range(0, 10):
        if digit != int(x[i]):
            tmp = x[:i] + str(digit) + x[i+1:]
            if int(tmp) % 3 == 0:
                res = max(res, int(tmp))

print(res)