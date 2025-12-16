"""
問題 13.6: 有向グラフの閉路検出

問題:
有向グラフ G = (V, E) に閉路が存在するかどうかを判定する

閉路とは:
- ある頂点から出発して、同じ頂点に戻ってくる経路
- 有向グラフでは、辺の向きに従って進む必要がある

解法:
1. DFS版（3色法）: 訪問状態を3つに分ける
   - 白（未訪問）
   - 灰（訪問中 - 現在のDFS経路上）
   - 黒（訪問完了）
2. BFS版（Kahn's Algorithm）: トポロジカルソートで検出

計算量: O(V + E)
"""


def has_cycle_dfs(graph: list[list[int]]) -> bool:
    """
    有向グラフの閉路検出（DFS版 - 3色法）

    Args:
        graph: 隣接リスト表現の有向グラフ

    Returns:
        閉路があればTrue、なければFalse

    アルゴリズム（3色法）:
        - 白（0）: 未訪問
        - 灰（1）: 訪問中（現在のDFS経路上にある）
        - 黒（2）: 訪問完了（DFSが完了した）

        閉路の検出:
        - DFS中に「灰色」の頂点に到達したら閉路あり
        - 灰色 = 現在のDFS経路上 = 後戻りしている = 閉路

    例:
        # 閉路あり: 0 → 1 → 2 → 0
        graph = [[1], [2], [0]]
        has_cycle_dfs(graph) -> True

        # 閉路なし: 0 → 1 → 2
        graph = [[1], [2], []]
        has_cycle_dfs(graph) -> False
    """
    N = len(graph)
    # 0: 白（未訪問）, 1: 灰（訪問中）, 2: 黒（訪問完了）
    color = [0] * N

    def dfs(v: int) -> bool:
        """
        DFSで閉路を検出

        Args:
            v: 現在の頂点

        Returns:
            閉路が見つかったらTrue、なければFalse

        処理の流れ:
            1. vを灰色にする（訪問中）
            2. vの各隣接頂点について:
               - 灰色なら閉路発見（後戻り）
               - 白なら再帰的に探索
            3. vを黒色にする（訪問完了）
        """
        # vを灰色にする（訪問中）
        color[v] = 1

        for next_v in graph[v]:
            # 灰色の頂点に到達 = 現在のDFS経路上 = 閉路
            if color[next_v] == 1:
                return True

            # 白色（未訪問）なら再帰的に探索
            if color[next_v] == 0:
                # dfs中に訪問済みに辿りついた場合は閉路
                if dfs(next_v):
                    return True

            # 黒色（訪問完了）は無視
            # すでに探索済みで閉路がないことが確認されている

        # vの探索完了 - 黒色にする
        color[v] = 2
        return False

    # 全頂点について探索（非連結グラフにも対応）
    for v in range(N):
        if color[v] == 0:  # 未訪問なら探索
            if dfs(v):
                return True

    return False


def has_cycle_bfs(graph: list[list[int]]) -> bool:
    """
    有向グラフの閉路検出（BFS版 - Kahn's Algorithm）

    Args:
        graph: 隣接リスト表現の有向グラフ

    Returns:
        閉路があればTrue、なければFalse

    アルゴリズム:
        - トポロジカルソートを試みる
        - 全頂点を処理できなければ閉路あり

    注意:
        - これはtopological.pyのhas_cycle関数と同じ
    """
    from collections import deque

    N = len(graph)
    inDegree = [0] * N

    # 入次数を計算
    for v in range(N):
        for next_v in graph[v]:
            inDegree[next_v] += 1

    # 入次数0の頂点をキューに追加
    queue = deque()
    for v in range(N):
        if inDegree[v] == 0:
            queue.append(v)

    processed = 0  # 処理できた頂点数

    while queue:
        v = queue.popleft()
        processed += 1

        for next_v in graph[v]:
            inDegree[next_v] -= 1
            if inDegree[next_v] == 0:
                queue.append(next_v)

    # 全頂点を処理できなければ閉路あり
    return processed < N


def find_cycle(graph: list[list[int]]) -> list[int] | None:
    """
    有向グラフの閉路を実際に構築する

    Args:
        graph: 隣接リスト表現の有向グラフ

    Returns:
        閉路（頂点のリスト）、閉路がない場合はNone

    例:
        # 0 → 1 → 2 → 0
        graph = [[1], [2], [0]]
        find_cycle(graph) -> [0, 1, 2, 0]
    """
    N = len(graph)
    color = [0] * N  # 0: 白, 1: 灰, 2: 黒
    parent = [-1] * N
    cycle_start = -1
    cycle_end = -1

    def dfs(v: int) -> bool:
        nonlocal cycle_start, cycle_end

        color[v] = 1

        for next_v in graph[v]:
            if color[next_v] == 1:
                # 閉路発見
                cycle_start = next_v
                cycle_end = v
                return True

            if color[next_v] == 0:
                # 訪問時に親を記録しておくことでサイクル発見時に経路を辿れる
                parent[next_v] = v
                if dfs(next_v):
                    return True

        color[v] = 2
        return False

    # 閉路を探す
    for v in range(N):
        if color[v] == 0:
            if dfs(v):
                # 閉路を復元
                cycle = []
                current = cycle_end
                while current != cycle_start:
                    cycle.append(current)
                    current = parent[current]
                cycle.append(cycle_start)
                cycle.append(cycle_end)  # 最初の頂点に戻る
                cycle.reverse()
                return cycle

    return None

