import sys
n,k = map(int, input().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]

d = [0] * (k+1) # 가치의 합이 index가 되는 경우의 수를 담고 있는 DP 테이블. 0으로 세팅

d[0] = 1

for i in coins:
    for j in range(i,k+1):
        if j-i>=0:
            d[j] += d[j-i]

print(d[k])