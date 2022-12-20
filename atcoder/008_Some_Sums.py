# Some Sums-------------------------------------------------------------------------

n, a, b = map(int, input().split())
ans = 0

for i in range(1, n + 1):
    sum = 0
    x = str(i)
    for j in range(len(x)):
        sum += int(x[j])
    if a <= sum <= b:
        ans += i

print(ans)
