# Problem: Symmetric Difference
# HackerRank: https://www.hackerrank.com/challenges/symmetric-difference/problem
n = int(input().strip())
set_a = set(map(int, input().split()))
m = int(input().strip())
set_b = set(map(int, input().split()))
for value in sorted(set_a.symmetric_difference(set_b)):
    print(value)
