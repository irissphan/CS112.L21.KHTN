import io, os, sys

# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# s = input().decode()
s = sys.stdin.readline().strip()

MOD = [0] * 100
sum = 0

for i in range(len(s)):
    MOD[int(s[i])] += 1
    sum += int(s[i])

if sum % 3 == 1:
    if MOD[1] + MOD[4] + MOD[7] >= 1:
        MOD[1] -= 1
        if MOD[1] < 0:
            MOD[4] += MOD[1]
            MOD[1] = 0
        if MOD[4] < 0:
            MOD[7] += MOD[4]
            MOD[4] = 0
    elif MOD[2] + MOD[5] + MOD[8] >= 2:
        MOD[2] -= 2
        if MOD[2] < 0:
            MOD[5] += MOD[2]
            MOD[2] = 0
        if MOD[5] < 0:
            MOD[8] += MOD[5]
            MOD[5] = 0
elif sum % 3 == 2:
    if MOD[2] + MOD[5] + MOD[8] >= 1:
        MOD[2] -= 1
        if MOD[2] < 0:
            MOD[5] += MOD[2]
            MOD[2] = 0
        if MOD[5] < 0:
            MOD[8] += MOD[5]
            MOD[5] = 0
    elif MOD[1] + MOD[4] + MOD[7] >= 2:
        MOD[1] -= 2
        if MOD[1] < 0:
            MOD[4] += MOD[1]
            MOD[1] = 0
        if MOD[4] < 0:
            MOD[7] += MOD[4]
            MOD[4] = 0

for i in range(9, -1, -1):
    sys.stdout.write(str(i) * MOD[i])