import sys

n, k = map(int, sys.stdin.readline().split())

coins = [int(sys.stdin.readline()) for _ in range(n)]
coin_dp = [0] * (k+1)
coin_dp[0] = 1

for c in coins:
  for i in range(len(coin_dp)):
    if i >= c:
      coin_dp[i] += coin_dp[i - c]

print(coin_dp[k])
