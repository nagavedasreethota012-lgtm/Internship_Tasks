# Problem: Mutations
# HackerRank: https://www.hackerrank.com/challenges/python-mutations/problem
string = input().rstrip("\n")
index, character = input().split()
characters = list(string)
characters[int(index)] = character
print("".join(characters))
