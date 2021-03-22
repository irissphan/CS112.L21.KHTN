n = int(input())
a = [int(x) for x in input().split()]
a = [0] + a
for i in range(1, n+1):
    a[i] = a[i-1] + a[i]
l, r = 0, 1
lmin, rmax = 0, 1
for i in range(1, n+1):
    if a[lmin] > a[i]:
        lmin = i
    if a[r] - a[l] < a[i] - a[lmin]:
        l = lmin
        r = i
print(l+1, r, a[r]-a[l])