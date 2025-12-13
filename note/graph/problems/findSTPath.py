"""
問題 13.2: s-t パスの存在判定

問題:
グラフ G = (V, E) 上の2頂点 s, t ∈ V に対して、s-tパスが存在するかどうかを判定する

s-tパスとは:
- 頂点sから頂点tへ到達する経路
- グラフが連結なら全ての頂点間にパスが存在
- グラフが非連結なら一部の頂点間にパスが存在しない

解法:
1. DFS版: sからDFSを開始し、tに到達できるかチェック
2. BFS版: sからBFSを開始し、tに到達できるかチェック

計算量: O(V + E)
"""

from collections import deque


def has_path_dfs(graph: list[list[int]], s: int, t: int) -> bool:
    """
    s-tパスの存在判定（DFS版）

    Args:
        graph: 隣接リスト表現のグラフ
        s: 始点
        t: 終点

    Returns:
        s-tパスが存在するならTrue、存在しないならFalse

    例:
        # グラフ: 0--1  2--3
        graph = [[1], [0], [3], [2]]
        has_path_dfs(graph, 0, 1) -> True  (同じ連結成分)
        has_path_dfs(graph, 0, 3) -> False (異なる連結成分)
    """
    N = len(graph)
    seen = [False] * N

    def dfs(v: int) -> None:
        """
        深さ優先探索でsから到達可能な頂点を探索

        Args:
            v: 現在の頂点
        """
        seen[v] = True

        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)

    # sから探索開始
    dfs(s)

    # tが訪問済みならs-tパスが存在
    return seen[t]


def has_path_bfs(graph: list[list[int]], s: int, t: int) -> bool:
    """
    s-tパスの存在判定（BFS版）- code 13.4の実装

    Args:
        graph: 隣接リスト表現のグラフ
        s: 始点
        t: 終点

    Returns:
        s-tパスが存在するならTrue、存在しないならFalse

    アルゴリズム:
        1. sを始点としてBFSを実行
        2. BFS中にtに到達したらTrue
        3. BFSが終了してもtに到達しなければFalse
    """
    N = len(graph)
    seen = [False] * N

    # BFSでsから到達可能な頂点を探索
    queue = deque([s])
    seen[s] = True

    while queue:
        v = queue.popleft()

        # tに到達したらTrue（早期終了可能）
        if v == t:
            return True

        for next_v in graph[v]:
            if seen[next_v]:
                continue
            seen[next_v] = True
            queue.append(next_v)

    # BFS終了後もtに到達しなければFalse
    return seen[t]
