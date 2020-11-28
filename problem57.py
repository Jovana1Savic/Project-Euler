# Problem statement: https://www.hackerrank.com/contests/projecteuler/challenges/euler057/problem
import math

def verige(N):
    
    count = 0
        
    C0 = 1
    C1 = 2
    
    P0 = C0
    P1 = C0 * C1 + 1
    Q0 = 1
    Q1 = C1
    
    for k in range(2, N + 1):       
        Ck = 2
        
        Pk = Ck * P1 + P0
        Qk = Ck * Q1 + Q0
        
        P1, P0 = Pk, P1
        Q1, Q0 = Qk, Q1
        
        if len(str(Pk)) > len(str(Qk)):
            print(k)
            # count += 1
            
    return count

N = int(input())
count = verige(N)
        
        
