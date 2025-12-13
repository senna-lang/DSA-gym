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


def solve_maze_with_path(maze: list[str]) -> tuple[int, list[tuple[int, int]]] | None:
    """
    迷路の最短経路と経路自体を求める

    Args:
        maze: 迷路を表す文字列のリスト

    Returns:
        (最短経路の長さ, 経路のリスト) または None

    例:
        maze = ["S.", ".G"]
        solve_maze_with_path(maze) -> (2, [(0,0), (0,1), (1,1)])
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

    # 4方向
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # BFS with parent tracking
    dist = [[-1] * W for _ in range(H)]
    parent = [[None] * W for _ in range(H)]
    queue = deque([start])
    dist[start[0]][start[1]] = 0

    while queue:
        y, x = queue.popleft()

        if (y, x) == goal:
            # 経路を復元
            path = []
            current = goal
            while current is not None:
                path.append(current)
                current = parent[current[0]][current[1]]
            path.reverse()
            return (dist[goal[0]][goal[1]], path)

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < H and 0 <= nx < W):
                continue
            if maze[ny][nx] == "#":
                continue
            if dist[ny][nx] != -1:
                continue

            dist[ny][nx] = dist[y][x] + 1
            parent[ny][nx] = (y, x)
            queue.append((ny, nx))

    return None


def visualize_path(maze: list[str], path: list[tuple[int, int]]) -> None:
    """
    経路を可視化

    Args:
        maze: 迷路
        path: 経路のリスト
    """
    H = len(maze)
    W = len(maze[0])

    # 経路をセットに変換
    path_set = set(path)

    # 可視化
    for i in range(H):
        row = []
        for j in range(W):
            if (i, j) in path_set:
                if maze[i][j] == "S":
                    row.append("S")
                elif maze[i][j] == "G":
                    row.append("G")
                else:
                    row.append("*")
            else:
                row.append(maze[i][j])
        print("".join(row))


# 使用例とテスト
if __name__ == "__main__":
    print("=" * 60)
    print("問題 13.4: 迷路の最短経路")
    print("=" * 60)
    print()

    # テストケース1: 単純な迷路
    maze1 = ["S...", "....", "...G"]
    print("テスト1: 単純な迷路（壁なし）")
    for row in maze1:
        print(row)
    result = solve_maze_with_path(maze1)
    if result:
        length, path = result
        print(f"最短経路の長さ: {length}")
        print(f"経路: {path}")
        print("経路を可視化:")
        visualize_path(maze1, path)
    print()

    # テストケース2: 壁がある迷路
    maze2 = ["S.#.", "..#.", ".#.G"]
    print("テスト2: 壁がある迷路")
    for row in maze2:
        print(row)
    result = solve_maze_with_path(maze2)
    if result:
        length, path = result
        print(f"最短経路の長さ: {length}")
        print(f"経路: {path}")
        print("経路を可視化:")
        visualize_path(maze2, path)
    print()

    # テストケース3: 複雑な迷路
    maze3 = ["S.###", ".....#", "###.#", "#...#", "#.#.G"]
    print("テスト3: 複雑な迷路")
    for row in maze3:
        print(row)
    result = solve_maze_with_path(maze3)
    if result:
        length, path = result
        print(f"最短経路の長さ: {length}")
        print(f"経路の頂点数: {len(path)}")
        print("経路を可視化:")
        visualize_path(maze3, path)
    print()

    # テストケース4: ゴールに到達できない迷路
    maze4 = ["S.#", "###", "..G"]
    print("テスト4: ゴールに到達できない迷路")
    for row in maze4:
        print(row)
    result = solve_maze_bfs(maze4)
    print(f"結果: {result} (到達不可)")
    print()

    # テストケース5: 大きな迷路
    maze5 = [
        "S.......#",
        "#.#####.#",
        "#.....#.#",
        "###.#.#.#",
        "#...#...#",
        "#.#####.#",
        "#.......G",
    ]
    print("テスト5: 大きな迷路")
    for row in maze5:
        print(row)
    result = solve_maze_with_path(maze5)
    if result:
        length, path = result
        print(f"最短経路の長さ: {length}")
        print("経路を可視化:")
        visualize_path(maze5, path)
    print()

    print("=" * 60)
    print("アルゴリズムの説明")
    print("=" * 60)
    print("""
なぜBFSを使うのか:
1. BFSは最短経路を保証する
   - 距離順に探索するため
   - 最初にゴールに到達したときが最短経路

2. グリッドを暗黙的なグラフとして扱う
   - 各マス = 頂点
   - 隣接する通行可能なマス間 = 辺

3. 計算量: O(HW)
   - 各マスを最大1回訪問: O(HW)
   - 各マスで4方向チェック: O(4) = O(1)
   - 合計: O(HW)

4方向の定義:
- 上: (-1, 0)
- 右: (0, 1)
- 下: (1, 0)
- 左: (0, -1)

DFSを使わない理由:
- DFSは最短経路を保証しない
- 遠回りの経路を先に見つける可能性がある
""")
