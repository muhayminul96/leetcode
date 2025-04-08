n = int(input())
dic = {}
for i in range(n):
    text = input()
    if text in dic:
        dic[text] += 1
    else:
        dic[text] = 1
print(len(dic.keys()))


for i in dic.keys():
    print(dic[i], end=' ')

