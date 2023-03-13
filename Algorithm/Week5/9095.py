import sys
t = int(input())

for _ in range(t):
    num = int(sys.stdin.readline())
    d = [0] * (num+1) # index수 까지 만들 수 있는 경우의 수를 담고 있는 DP 테이블
    if num>=1:
        d[1] = 1
    if num >=2:
        d[2] = 2
    if num >=3:
        d[3] = 4
    if num>=4:
        for i in range(4,num+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[num])