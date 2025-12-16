"""
問題 13.4: 迷路の最短経路

問題:
迷路のサイズを H×W として、スタートからゴールまでたどり着く最短路を O(HW) で求める

迷路とは:
- H×Wのグリッド
- 各マスは通行可能('.') or 壁('#')
- スタート('S')からゴール('G')への最短経路を求める

解法:
- BFSを使う（最短経路保証）
- グリッドを暗黙的なグラフとして扱う
- 4方向（上下左右）への移動

計算量: O(HW)
- 各マスを最大1回訪問
- 各辺（隣接マス間）を最大1回チェック
"""

from collections import deque


def solve_maze_bfs(maze: list[str]) -> int:
    """
    迷路の最短経路を求める（BFS版）

    Args:
        maze: 迷路を表す文字列のリスト
              'S': スタート, 'G': ゴール, '.': 通路, '#': 壁

    Returns:
        最短経路の長さ（ゴールに到達できない場合は-1）

    例:
        maze = [
            "S.#.",
            "..#.",
            ".#.G"
        ]
        solve_maze_bfs(maze) -> 6
    """
    H = len(maze)
    W = len(maze[0])

    # スタートとゴールの位置を見つける
    start = goal = None
    for i in range(H):
        for j in range(W):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "G":
                goal = (i, j)

    # 4方向（上、右、下、左）
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # BFS
    dist = [[-1] * W for _ in range(H)]
    queue = deque([start])
    dist[start[0]][start[1]] = 0

    while queue:
        y, x = queue.popleft()

        # ゴールに到達
        if (y, x) == goal:
            return dist[y][x]

        # 4方向を探索
        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            # 範囲外チェック
            if not (0 <= ny < H and 0 <= nx < W):
                continue

            # 壁チェック
            if maze[ny][nx] == "#":
                continue

            # 訪問済みチェック
            if dist[ny][nx] != -1:
                continue

            # 距離を更新
            dist[ny][nx] = dist[y][x] + 1
            queue.append((ny, nx))

    # ゴールに到達できない
    return -1