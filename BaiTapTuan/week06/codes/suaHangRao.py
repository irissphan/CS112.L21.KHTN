import io, os, sys
# input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def solve(n, a, m, b):
    l, r = min(a), min(a) + max(b)
    while l <= r:
        x = (l + r) // 2


        j = 0
        flag = True
        arr = [W for W in a if W < x]
        for wall in arr:
            while j < m and wall + b[j] < x:
                j += 1
            if j < m:
                j += 1
            else:
                flag = False
                break


        if flag:
            l = x + 1
        else:
            r = x - 1
    return r

def get_result(n, a, m, b, r):
    res =  [i for i in range(n) if a[i] < r]
    sys.stdout.write(str(r) + " " + str(len(res)) + "\n")
    j = 0
    for id in res:
        sys.stdout.write(str(id+1) + " ")
        while j < m and a[id] + b[j] < r:
            j += 1
        sys.stdout.write(str(j+1) + "\n")
        j += 1


def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    r = solve(n, a, m, b)
    get_result(n, a, m, b, r)

if __name__ == "__main__":
    main()


# sys.stdout.write("\n".join(map(str, [" ".join(map(str, x)) for x in res])))