n = int(input())

dic = {}
for _ in range(n):
    b = input().split(' ')
    k = ' '.join(b[:-1])
    val = int(b[-1])
    if k in dic:
        dic[k] += val
    else:
        dic[k] = val
for key, value in dic.items():
    print(key,value)
