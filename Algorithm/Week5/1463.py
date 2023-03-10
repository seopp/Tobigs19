n = int(input())

d = [0] * (n+1) # 인덱스의 숫자가 1이 되는데 필요한 연산의 최솟값을 담고 있는 테이블

for i in range(2,n+1):
    d[i] = d[i-1] + 1  # 우선 1 뺀 값 넣어놓기
    # 이제 d[i]는 위에서 초기화한 d[i-1]+1값이 들어있음
    if i%2 == 0:       # 2로 나누어떨어지면
        d[i] = min(d[i], d[i//2]+1)  # d[i//2]+1은 i를 2로 나눈 값이 1이 되는데 걸리는 최소 연산 횟수 + i를 2로나누는 연산횟수 1회
    if i%3 == 0:       # 3으로 나누어떨어지면
        d[i] = min(d[i], d[i//3]+1)  # d[i//3]+1은 i를 3로 나눈 값이 1이 되는데 걸리는 최소 연산 횟수 + i를 3로나누는 연산횟수 1회

print(d[n]) # d[n]에는 n이 1이 되는데 필요한 연산의 최소 횟수가 들어있음