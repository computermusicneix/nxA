
import random

# 5,7,5

verso1 = []
verso2 = []
verso3 = []

lines = open("palabras.txt").readlines()

for i in range(0,5):
    verso1.append(lines[random.randint(0,len(lines))])

for i in range(0,7):
    verso2.append(lines[random.randint(0,len(lines))])

for i in range(0,5):
    verso3.append(lines[random.randint(0,len(lines))])

print(verso1)
print(verso2)
print(verso3)
