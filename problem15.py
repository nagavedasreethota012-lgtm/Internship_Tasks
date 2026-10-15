# Problem: Word Order
# HackerRank: https://www.hackerrank.com/challenges/word-order/problem
n = int(input().strip())
counts = {}
order = []
for _ in range(n):
    word = input().strip()
    if word not in counts:
        counts[word] = 0
        order.append(word)
    counts[word] += 1
print(len(order))
print(" ".join(str(counts[word]) for word in order))
