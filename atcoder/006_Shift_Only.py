# Shift Only-------------------------------------------------------------------------

N = int(input())
list = list(map(int, input().split()))
count = []
for i, num in enumerate(list):
    count.append(0)
    while num % 2 == 0:
        num //= 2
        count[i] += 1
print(min(count))
