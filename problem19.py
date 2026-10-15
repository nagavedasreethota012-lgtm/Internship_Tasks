# Problem: Collections.Counter()
# HackerRank: https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
x = int(input().strip())
shoe_sizes = Counter(map(int, input().split()))
customers = int(input().strip())
earnings = 0
for _ in range(customers):
    size, price = map(int, input().split())
    if shoe_sizes[size] > 0:
        earnings += price
        shoe_sizes[size] -= 1
print(earnings)
