import sys
n = int(input()) # 포도잔의 개수

drink = [0] * (n+1) # 포도주의 양을 담은 리스트 
for i in range(1, n+1):
    drink[i] = int(sys.stdin.readline())

d = [0] * (n+1) # index개의 잔이 있을 때, 최댓값을 담고 있는 DP 테이블
if n>=1:
    d[1] = drink[1]
if n>=2:
    d[2] = drink[1] + drink[2]
if n>=3:
    for i in range(3,n+1):
        d[i] = max(d[i-2]+drink[i], d[i-3]+drink[i-1]+drink[i], d[i-1])

print(max(d))