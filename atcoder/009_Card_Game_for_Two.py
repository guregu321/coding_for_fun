# Card Game for Two-------------------------------------------------------------------------

n = int(input())
list = list(map(int, input().split()))
Alice = []
Bob = []

list.sort(reverse=True)

for i, num in enumerate(list):
    if i % 2 == 0:
        Alice.append(num)
    else:
        Bob.append(num)

print(sum(Alice) - sum(Bob))
