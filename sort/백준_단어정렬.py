import sys

n = int(sys.stdin.readline())
my_word = []
word = []

for _ in range(n):
    word.append(sys.stdin.readline())

word = list(set(word))

for w in word:
    my_word.append([w, len(w)])

my_word = sorted(my_word, key = lambda x : (x[1], x[0]))

for x, y in my_word:
    print(x, end = "")
