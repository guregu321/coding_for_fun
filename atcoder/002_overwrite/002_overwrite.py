# https://atcoder.jp/contests/past202012-open/tasks/past202012_b

S = input("文字列を入力してください。").lower()
T = ""

for i in range(len(S)):
    c = S[i]
    T = T.replace(c, "")
    T = T + c

print(T)
