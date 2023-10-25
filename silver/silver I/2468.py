# 백준 silver I
# 안전 영역

import sys
from collections import deque

N = int(sys.stdin.readline())

max_height = 0
icebergs = []  # icebergs = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    icebergs.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if icebergs[i][j] > max_height:
            max_height = icebergs[i][j]

dh = [1, -1, 0, 0]
dw = [0, 0, 1, -1]


def bfs(h, w, height, N):
    queue = deque()
    queue.append([h, w])
    visited[h][w] = True
  
    while queue:
        h, w = queue.popleft()
    
        for d in range(4):
            nh = h + dh[d]
            nw = w + dw[d]
      
            if 0 <= nh < N and 0 <= nw < N:
                if icebergs[nh][nw] > height and not visited[nh][nw]:
                    visited[nh][nw] = True
                    queue.append([nh, nw])


max_count = 0
for idx in range(max_height):
    visited = [[False] * N for _ in range(N)]
    count = 0
  
    for i in range(N):
        for j in range(N):
            if icebergs[i][j] > idx and not visited[i][j]:
                bfs(i, j, idx, N)
                count += 1
    if max_count < count:
        max_count = count

print(max_count)
