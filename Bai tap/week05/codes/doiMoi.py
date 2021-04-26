a, k, b, m, n = [int(x) for x in input().split()]
l, r = 1, 10**18

def check(days):
    if a*(days - days//k) + b*(days - days//m) >= n:
        return True
    else:
        return False

while l <= r:
    mid = (l+r) // 2
    if check(mid):
        res = mid
        r = mid - 1
    else:
        l = mid + 1

print(res)