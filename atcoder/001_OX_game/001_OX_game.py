# https://atcoder.jp/contests/past202012-open/tasks/past202012_a

inputStr = input("OXを入力してください").lower()
win_condition = 3
ans = "draw"

for i in range(len(inputStr) - win_condition + 1):
    if inputStr[i] == inputStr[i + 1] == inputStr[i + 2]:
        ans = inputStr[i]

print("The result is " + ans)
