import sys

Exp = list(sys.stdin.readline().rstrip().split("-"))

s = sum(list(map(int, Exp.pop(0).split("+"))))

for i in Exp:
    s -= sum(list(map(int, i.split("+"))))

print(s)
