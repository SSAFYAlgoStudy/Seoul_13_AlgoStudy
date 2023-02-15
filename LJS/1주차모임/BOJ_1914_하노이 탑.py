import sys
input= sys.stdin.readline

def dfs(first, last, N):
    if N == 1:
        print(first,last)
        return

    dfs(first, 6-first-last, N-1) 
    print(first, last) 
    dfs(6-first-last, last, N-1) 

N = int(input())
print(2**N-1)

if N <= 20:
    dfs(1,3,N)