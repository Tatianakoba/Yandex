import math

count = int(input())
num = input().split()
num = list(map(int, num))
num.insert(0, 0)

alfabet = 'abcdefghijklmnopqrstuvwxyz '
l = []

for i in range(len(num)-1, -1, -1):
    f = abs(num[i]-num[i-1])

l = l[-2::-1]
word =''

for i in l:
    word += alfabet[int(math.log2(i))]

print(word)
