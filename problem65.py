# https://www.hackerrank.com/contests/projecteuler/challenges/euler065/problem

def sum_of_digits(num):
    s = 0
    while num > 0:
        s += (num % 10)
        num = num // 10
    return s

def verige(N):
    
    if N == 1:
        return 2
    if N == 2:
        return 3
    count = 0
        
    C0 = 2
    C1 = 1
    Ck = 0
    
    P0 = C0
    P1 = C0 * C1 + 1
    Q0 = 1
    Q1 = C1
      
    Pk = P0
    Qk = Q0

        
    for k in range(2, N):
        if k % 3 == 2:       
            C = Ck + 2
            Ck += 2
        else:
            C = 1
        
        Pk = C * P1 + P0
        Qk = C * Q1 + Q0
        
        P1, P0 = Pk, P1
        Q1, Q0 = Qk, Q1
            
    return sum_of_digits(Pk)

N = int(input())
print(verige(N))
