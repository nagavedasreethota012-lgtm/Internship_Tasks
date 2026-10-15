# Problem: Finding the Percentage
# HackerRank: https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input().strip())
marks = {}
for _ in range(n):
    data = input().split()
    marks[data[0]] = list(map(float, data[1:]))
query_name = input().strip()
average = sum(marks[query_name]) / len(marks[query_name])
print(f"{average:.2f}")
