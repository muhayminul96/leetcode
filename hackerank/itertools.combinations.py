import itertools

text, n = input().split()
n = int(n)

# Sort characters for lexicographic order
sorted_text = sorted(text)

for i in range(1, n + 1):
    for combo in itertools.combinations(sorted_text, i):
        print(''.join(combo))