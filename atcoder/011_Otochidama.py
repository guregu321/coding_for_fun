# Otoshidama -------------------------------------------------------------------------

x, y = map(int, input().split())

for i in range(x + 1):
    if 10000 * i > y:
        continue
    for j in range(x + 1 - i):
        if 10000 * i + 5000 * j > y:
            continue
        else:
            if 10000 * i + 5000 * j + 1000 * (x - i - j) == y:
                print("{} {} {}".format(i, j, x - i - j))
                break
    else:
        continue
    break
else:
    print("-1 -1 -1")
