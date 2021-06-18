n = int(input())
a = [int(x) for x in input().split()]

a.sort(reverse=True)
a = [0] + a
res = 0
for i in range(1, len(a)):
    if a[i] >= i:
        res = i

print(res)