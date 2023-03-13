import sys
n = int(input())
scores = [int(sys.stdin.readline()) for _ in range(n)]

d = [0] * (n+1) # index번째 계단까지에 오를 수 있는 최댓값을 담고 있는 DP 테이블

if n>=1:
    d[1] = scores[0]
if n>=2:
    d[2] = scores[0] + scores[1]
if n>=3:
    for i in range(3,n+1):
        d[i] = max(d[i-2]+scores[i-1], d[i-3]+scores[i-2]+scores[i-1]) 
print(d[n])