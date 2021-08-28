import sys

my_list = list(sys.stdin.readline())

del my_list[-1]

my_list = list(map(int, my_list))

my_list.sort()

print(my_list)

for num in my_list:
    print(num, end = "")
