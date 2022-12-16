# https://atcoder.jp/contests/past202012-open/tasks/past202012_c

N = int(input("整数を入力してください。"))
ht_decimal = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""

for i in reversed(range(0, 3)):
    ans = ans + ht_decimal[N // (36**i)]
    N = N % (36**i)

while len(ans) > 1 and ans[0] == "0":
    ans = ans[1:]

print(ans)
