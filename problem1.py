
import sys

def arithmeticSeries(n, d):
    return n * (n + 1) * d // 2

def sumNumbers(n):
    S3 = arithmeticSeries(n // 3, 3)
    S5 = arithmeticSeries(n // 5, 5)
    S15 = arithmeticSeries(n // 15, 15)
    return S3 + S5 - S15

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(sumNumbers(n - 1))
