n = int(input())
h = [[] for i in range(10)]

for i in range(n):
    num = int(input())
    a = h[num % 10]

    l, r = 0, len(a)

    while l < r:
        m = (l + r) // 2

        if a[m] < num:
            l = m + 1
        else:
            r = m

    a.insert(l, num)
    print(h)
