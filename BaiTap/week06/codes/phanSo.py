import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if c == d or (d*a-c*b)*(c-d)<0 or (d*a - c*b)%(c-d) != 0 :
    print(0)
else:
    dem = 0
    while (a != c or b != d):
        a = a + 1
        b = b + 1
        tmp = math.gcd(a,b)
        a = a // tmp
        b = b // tmp
        dem = dem +1
        if dem > 1000000:
            break
    if dem > 1000000:
        print(0)
    else:
        print(dem)