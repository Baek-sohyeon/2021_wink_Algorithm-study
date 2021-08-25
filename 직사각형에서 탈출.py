import sys
x, y, w, h = map(int,sys.stdin.readline().split())
list = [h-y, w-x, x, y]
print(min(list))
