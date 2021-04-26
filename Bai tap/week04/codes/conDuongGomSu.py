import math
n = int(input())
a = [int(x) for x in input().split()]
a = [0] + a
sum = [0]

for i in range(1, len(a)):
    sum.append(sum[i-1] + a[i]**100)

def check(i):
    sumA, cntA, sumB, cntB = sum[i], 1, -1, 0
    for j in range(2*i, len(sum), i):
        if sum[j]-sum[j-i] == sumA:
            cntA += 1
        elif sumB == -1:
            sumB = sum[j]-sum[j-i]
            cntB = 1
        elif sum[j]-sum[j-i] == sumB:
            cntB += 1
        else:
            return
    if cntB > 0:
        res.append([i, cntA, cntB])

res = []
for i in range(1, int(math.sqrt(n))+1):
  if n % i == 0:
      check(i)
      if i**2 == n:
          continue
      check(int(n/i))

print(len(res) if len(res) > 0 else -1)
res.sort(key=lambda k : k[0])
for i in range(len(res)):
    print(res[i][0], res[i][1], res[i][2])