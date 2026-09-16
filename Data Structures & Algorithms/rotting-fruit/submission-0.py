class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    queue.append((r,c))

        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        while queue and fresh>0:
            time+=1
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh-=1

        if fresh > 0: return -1
        else: return time




