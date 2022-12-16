# Product-------------------------------------------------------------------------

# a, b = map(int, input().split())
# if a * b % 2 == 0:
#     ans = "Even"
# else:
#     ans = "Odd"
# print(ans)


# Placing Marbles-------------------------------------------------------------------------

# a = input()
# ans = int(a[0]) + int(a[1]) + int(a[2])
# print(ans)


# Shift Only-------------------------------------------------------------------------

# N = int(input())
# list = list(map(int, input().split()))
# count = []
# for i, num in enumerate(list):
#     count.append(0)
#     while num % 2 == 0:
#         num //= 2
#         count[i] += 1
# print(min(count))


# Coins-------------------------------------------------------------------------

# a = int(input())
# b = int(input())
# c = int(input())
# n = int(input())
# cnt = 0

# for i in range(a + 1):
#     for j in range(b + 1):
#         for k in range(c + 1):
#             if i * 500 + j * 100 + k * 50 == n:
#                 cnt += 1

# print(cnt)


# Some Sums-------------------------------------------------------------------------

# n, a, b = map(int, input().split())
# ans = 0

# for i in range(1, n + 1):
#     sum = 0
#     x = str(i)
#     for j in range(len(x)):
#         sum += int(x[j])
#     if a <= sum <= b:
#         ans += i

# print(ans)


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
