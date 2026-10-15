# Problem: Nested Lists
# HackerRank: https://www.hackerrank.com/challenges/nested-list/problem
records = []
n = int(input().strip())
for _ in range(n):
    name = input().strip()
    score = float(input().strip())
    records.append((name, score))
scores = sorted(set(score for _, score in records))
second_lowest = scores[1]
for name in sorted(name for name, score in records if score == second_lowest):
    print(name)
