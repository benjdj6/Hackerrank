n = int(raw_input().strip())
grid = []
pairs = []
for i in range(n):
    grid_t = map(int, raw_input().strip())
    grid.append(grid_t)

for j in range(1, n - 1):
    for k in range(1, n - 1):
        curr = grid[j][k]
        if (curr > grid[j][k - 1] and curr > grid[j][k + 1] and
           curr > grid[j + 1][k] and curr > grid[j - 1][k]):
            pairs.append([j, k])
            k += 1

for p in pairs:
    grid[p[0]][p[1]] = 'X'

for x in range(n):
    grid[x] = map(str, grid[x])
    grid[x] = "".join(grid[x])
    print grid[x]
